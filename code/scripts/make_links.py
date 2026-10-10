"""Build src/papers/links.md: verified arXiv links + APS DOIs for the reading list.

arXiv IDs are resolved by title through the arXiv API and accepted only if the title
similarity >= 0.85 AND the first-author surname appears in the author list.
APS DOIs are constructed (10.1103/<Journal>.<vol>.<page>) from volume/page and are NOT
checked against the publisher; everything else gets a Google Scholar search link.

Run:  SSL_CERT_FILE=/root/.ccr/ca-bundle.crt python -I code/scripts/make_links.py
(takes ~4 min: the arXiv API asks for >= 3 s between requests)
"""
import difflib
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

APS = {"PRA": "PhysRevA", "PRB": "PhysRevB", "PRL": "PhysRevLett", "PRX": "PhysRevX",
       "PRXQ": "PRXQuantum", "RMP": "RevModPhys", "PRApplied": "PhysRevApplied"}

# (tier, first-author surname, title, year, venue string, aps (journal, vol, page) or None, known arXiv id or None)
P = [
 ("T0", "Vool", "Introduction to quantum electromagnetic circuits", 2017, "Int. J. Circ. Theor. Appl. 45, 897", None, None),
 ("T0", "Rasmussen", "Superconducting circuit companion - an introduction with worked examples", 2021, "PRX Quantum 2, 040204", ("PRXQ", 2, "040204"), None),
 ("T0", "Krantz", "A quantum engineer's guide to superconducting qubits", 2019, "Appl. Phys. Rev. 6, 021318", None, None),
 ("T0", "Blais", "Circuit quantum electrodynamics", 2021, "Rev. Mod. Phys. 93, 025005", ("RMP", 93, "025005"), None),
 ("T0", "Clerk", "Introduction to quantum noise, measurement and amplification", 2010, "Rev. Mod. Phys. 82, 1155", ("RMP", 82, "1155"), None),
 ("T0", "Golubov", "The current-phase relation in Josephson junctions", 2004, "Rev. Mod. Phys. 76, 411", ("RMP", 76, "411"), None),
 ("T0", "Aguado", "A perspective on semiconductor-based superconducting qubits", 2020, "Appl. Phys. Lett. 117, 240501", None, None),
 ("T0", "Gyenis", "Moving beyond the transmon: Noise-protected superconducting quantum circuits", 2021, "PRX Quantum 2, 030101", ("PRXQ", 2, "030101"), None),
 ("T0", "Burkard", "Circuit theory for decoherence in superconducting charge qubits", 2004, "PRB 69, 064503", ("PRB", 69, "064503"), None),
 ("T1", "Koch", "Charge-insensitive qubit design derived from the Cooper pair box", 2007, "PRA 76, 042319", ("PRA", 76, "042319"), None),
 ("T1", "Brooks", "Protected gates for superconducting qubits", 2013, "PRA 87, 052306", ("PRA", 87, "052306"), None),
 ("T1", "Dempster", "Understanding degenerate ground states of a protected quantum circuit in the presence of disorder", 2014, "PRB 90, 094518", ("PRB", 90, "094518"), None),
 ("T1", "Groszkowski", "Coherence properties of the 0-pi qubit", 2018, "New J. Phys. 20, 043053", None, None),
 ("T1", "Gyenis", "Experimental realization of a protected superconducting circuit derived from the 0-pi qubit", 2021, "PRX Quantum 2, 010339", ("PRXQ", 2, "010339"), "1910.07542"),
 ("T1", "Di Paolo", "Control and coherence time enhancement of the 0-pi qubit", 2019, "New J. Phys. 21, 043002", None, None),
 ("T1", "Beenakker", "Universal limit of critical-current fluctuations in mesoscopic Josephson junctions", 1991, "PRL 67, 3836", ("PRL", 67, "3836"), None),
 ("T1", "Larsen", "Semiconductor-nanowire-based superconducting qubit", 2015, "PRL 115, 127001", ("PRL", 115, "127001"), None),
 ("T1", "de Lange", "Realization of microwave quantum circuits using hybrid superconducting-semiconducting nanowire Josephson elements", 2015, "PRL 115, 127002", ("PRL", 115, "127002"), None),
 ("T1", "Casparis", "Superconducting gatemon qubit based on a proximitized two-dimensional electron gas", 2018, "Nat. Nanotechnol. 13, 915", None, None),
 ("T1", "Kringhoj", "Anharmonicity of a superconducting qubit with a few-mode Josephson junction", 2018, "PRB 97, 060508", ("PRB", 97, "060508"), None),
 ("T1", "Larsen", "Parity-protected superconductor-semiconductor qubit", 2020, "PRL 125, 056801", ("PRL", 125, "056801"), None),
 ("T1", "Ciaccia", "Charge-4e supercurrent in a two-dimensional InAs-Al superconductor-semiconductor heterostructure", 2024, "Commun. Phys. 7, 41", None, None),
 ("T1", "Schrade", "Protected hybrid superconducting qubit in an array of gate-tunable Josephson interferometers", 2022, "PRX Quantum 3, 030303", ("PRXQ", 3, "030303"), None),
 ("T1", "Smith", "Superconducting circuit protected by two-Cooper-pair tunneling", 2020, "npj Quantum Inf. 6, 8", None, None),
 ("T1", "Clerk", "Using a qubit to measure photon-number statistics of a driven thermal oscillator", 2007, "PRA 75, 042302", ("PRA", 75, "042302"), None),
 ("T1", "Ithier", "Decoherence in a superconducting quantum bit circuit", 2005, "PRB 72, 134519", ("PRB", 72, "134519"), None),
 ("T1", "Catelani", "Relaxation and frequency shifts induced by quasiparticles in superconducting qubits", 2011, "PRB 84, 064517", ("PRB", 84, "064517"), None),
 ("T1", "Doucot", "Physical implementation of protected qubits", 2012, "Rep. Prog. Phys. 75, 072001", None, None),
 ("T1", "Kitaev", "Protected qubit based on a superconducting current mirror", 2006, "arXiv:cond-mat/0609441", None, "cond-mat/0609441"),
 ("T1", "Schoelkopf", "Qubits as spectrometers of quantum noise", 2003, "in Quantum Noise in Mesoscopic Physics", None, "cond-mat/0210247"),
 ("T1", "Sears", "Photon shot noise dephasing in the strong-dispersive limit of circuit QED", 2012, "PRB 86, 180504", ("PRB", 86, "180504"), None),
 ("T2", "Bagwell", "Suppression of the Josephson current through a narrow, mesoscopic, semiconductor channel by a single impurity", 1992, "PRB 46, 12573", ("PRB", 46, "12573"), None),
 ("T2", "Pientka", "Topological superconductivity in a planar Josephson junction", 2017, "PRX 7, 021032", ("PRX", 7, "021032"), None),
 ("T2", "Shabani", "Two-dimensional epitaxial superconductor-semiconductor heterostructures: A platform for topological superconducting networks", 2016, "PRB 93, 155402", ("PRB", 93, "155402"), None),
 ("T2", "Kjaergaard", "Quantized conductance doubling and hard gap in a two-dimensional semiconductor-superconductor heterostructure", 2016, "Nat. Commun. 7, 12841", None, None),
 ("T2", "Mayer", "Gate controlled anomalous phase shift in Al/InAs Josephson junctions", 2020, "Nat. Commun. 11, 212", None, "1905.12670"),
 ("T2", "Yokoyama", "Anomalous Josephson effect induced by spin-orbit interaction and Zeeman effect in semiconductor nanowires", 2014, "PRB 89, 195407", ("PRB", 89, "195407"), None),
 ("T2", "Reeg", "Metallization of a Rashba wire by a superconducting layer in the strong-proximity regime", 2018, "PRB 97, 165425", ("PRB", 97, "165425"), None),
 ("T2", "Antipov", "Effects of gate-induced electric fields on semiconductor Majorana nanowires", 2018, "PRX 8, 031041", ("PRX", 8, "031041"), None),
 ("T2", "Zazunov", "Andreev level quantum dynamics in Josephson junctions", 2003, "PRL 90, 087003", ("PRL", 90, "087003"), None),
 ("T2", "Bargerbos", "Observation of vanishing charge dispersion of a nearly open superconducting island", 2020, "PRL 124, 246802", ("PRL", 124, "246802"), None),
 ("T2", "Kringhoj", "Suppressed charge dispersion via resonant tunneling in a single-channel transmon", 2020, "PRL 124, 246803", ("PRL", 124, "246803"), None),
 ("T2", "Danilenko", "Few-mode to mesoscopic junctions in gatemon qubits", 2023, "PRB", None, "2209.03688"),
 ("T2", "Groth", "Kwant: a software package for quantum transport", 2014, "New J. Phys. 16, 063065", None, None),
 ("T2", "Furusaki", "Dc Josephson effect and Andreev reflection", 1991, "PRB 43, 10164", ("PRB", 43, "10164"), None),
 ("T2", "Winkler", "Unified numerical approach to topological semiconductor-superconductor heterostructures", 2019, "PRB 99, 245408", ("PRB", 99, "245408"), None),
 ("T3", "Willsch", "Observation of Josephson harmonics in tunnel junctions", 2024, "Nat. Phys.", None, "2302.09192"),
 ("T3", "Messelot", "Direct measurement of a sin(2phi) current phase relation in a graphene superconducting quantum interference device", 2024, "PRL 133, 106001", ("PRL", 133, "106001"), "2405.13642"),
 ("T3", "Leblanc", "Gate- and flux-tunable sin(2phi) Josephson element with planar-Ge junctions", 2025, "Nat. Commun. 16", None, "2405.14695"),
 ("T3", "Smith", "Magnifying quantum phase fluctuations with Cooper-pair pairing", 2022, "PRX 12, 021002", ("PRX", 12, "021002"), None),
 ("T3", "Kalashnikov", "Bifluxon: Fluxon-parity-protected superconducting qubit", 2020, "PRX Quantum 1, 010307", ("PRXQ", 1, "010307"), None),
 ("T3", "You", "Circuit quantization in the presence of time-dependent external flux", 2019, "PRB 99, 174512", ("PRB", 99, "174512"), "1902.04734"),
 ("T3", "Riwar", "Circuit quantization with time-dependent magnetic fields for realistic geometries", 2022, "npj Quantum Inf. 8, 36", None, None),
 ("T3", "Anonymous", "The tunable 0-pi qubit: Dynamics and Relaxation", 2022, "arXiv:2211.09333", None, "2211.09333"),
 ("T3", "Giavaras", "Flux-tunable parity-protected qubit based on a single full-shell nanowire Josephson junction", 2025, "arXiv:2503.05284", None, "2503.05284"),
 ("T3", "Hays", "Direct microwave measurement of Andreev-bound-state dynamics in a semiconductor-nanowire Josephson junction", 2018, "PRL 121, 047001", ("PRL", 121, "047001"), None),
 ("T3", "Hays", "Coherent manipulation of an Andreev spin qubit", 2021, "Science 373, 430", None, None),
 ("T3", "Janvier", "Coherent manipulation of Andreev states in superconducting atomic contacts", 2015, "Science 349, 1199", None, None),
 ("T3", "Manucharyan", "Fluxonium: Single Cooper-pair circuit free of charge offsets", 2009, "Science 326, 113", None, None),
 ("T3", "Somoroff", "Millisecond coherence in a superconducting qubit", 2023, "PRL 130, 267001", ("PRL", 130, "267001"), None),
 ("T3", "Earnest", "Realization of a Lambda system with metastable states of a capacitively shunted fluxonium", 2018, "PRL 120, 150504", ("PRL", 120, "150504"), None),
 ("T3", "Motzoi", "Simple pulses for elimination of leakage in weakly nonlinear qubits", 2009, "PRL 103, 110501", ("PRL", 103, "110501"), None),
 ("T3", "Fowler", "Surface codes: Towards practical large-scale quantum computation", 2012, "PRA 86, 032324", ("PRA", 86, "032324"), None),
 ("T3", "Bonilla Ataides", "The XZZX surface code", 2021, "Nat. Commun. 12, 2172", None, None),
]

NS = {"a": "http://www.w3.org/2005/Atom"}


def norm(s):
    return re.sub(r"[^a-z0-9 ]", "", s.lower().replace("-", " ").replace("pi", "pi"))


def arxiv_lookup(title, surname):
    q = urllib.parse.quote(f'ti:"{title}"')
    url = f"https://export.arxiv.org/api/query?search_query={q}&max_results=3"
    try:
        data = urllib.request.urlopen(url, timeout=30).read()
    except Exception as e:  # noqa: BLE001
        return None, f"error {e}"
    for e in ET.fromstring(data).findall("a:entry", NS):
        t = " ".join(e.find("a:title", NS).text.split())
        authors = " ".join(a.find("a:name", NS).text for a in e.findall("a:author", NS)).lower()
        ratio = difflib.SequenceMatcher(None, norm(t), norm(title)).ratio()
        key = surname.lower().replace("kringhoj", "kringh").replace("doucot", "dou")
        if ratio >= 0.85 and (surname == "Anonymous" or key.split()[-1] in authors):
            aid = re.sub(r"v\d+$", "", e.find("a:id", NS).text.split("/abs/")[-1])
            return aid, f"match {ratio:.2f}"
    return None, "no match"


def main():
    out = Path(__file__).resolve().parents[2] / "src" / "papers" / "links.md"
    rows, stats = [], {"arxiv": 0, "doi": 0, "search": 0}
    for i, (tier, au, title, year, venue, aps, aid) in enumerate(P):
        status = "known"
        if aid is None:
            time.sleep(3.2)
            aid, status = arxiv_lookup(title, au)
        print(f"[{i+1}/{len(P)}] {au} {year}: {aid} ({status})", file=sys.stderr, flush=True)
        links = []
        if aid:
            links.append(f"[arXiv:{aid}](https://arxiv.org/abs/{aid})")
            stats["arxiv"] += 1
        if aps:
            j, v, p = aps
            links.append(f"[DOI](https://doi.org/10.1103/{APS[j]}.{v}.{p})")
            stats["doi"] += 1
        if not links:
            q = urllib.parse.quote(f"{title} {au} {year}")
            links.append(f"[tìm kiếm](https://scholar.google.com/scholar?q={q})")
            stats["search"] += 1
        rows.append((tier, f"{au} ({year})", title, venue, " · ".join(links)))
    names = {"T0": "T0 — Nền & tổng quan", "T1": "T1 — Lõi luận án (G1)", "T2": "T2 — Vi mô (G2, ND1)",
             "T3": "T3 — Mở rộng & cạnh tranh (G3)"}
    md = ["# Liên kết tài liệu", "",
          "Sinh bởi `code/scripts/make_links.py`. **arXiv**: ID được xác minh qua arXiv API (khớp tiêu đề ≥ 0,85 và tên tác giả đầu) hoặc lấy từ kết quả tìm kiếm trước đó. "
          "**DOI** (chỉ tạp chí APS): dựng từ tập/số trang, đúng quy tắc đặt DOI của APS nhưng chưa kiểm tra trực tiếp với nhà xuất bản. "
          "**tìm kiếm**: liên kết Google Scholar theo tiêu đề (không phải liên kết trực tiếp); các bài này không có bản arXiv khớp trong lần tra cứu hoặc nằm ở tạp chí không đặt DOI theo quy tắc.", "",
          f"Tổng: {len(P)} bài — {stats['arxiv']} có arXiv, {stats['doi']} có DOI APS, {stats['search']} chỉ có liên kết tìm kiếm.", ""]
    for t in ("T0", "T1", "T2", "T3"):
        md += [f"## {names[t]}", "", "| Tác giả | Tiêu đề | Nơi đăng | Liên kết |", "|---|---|---|---|"]
        md += [f"| {a} | {ti} | {v} | {l} |" for tt, a, ti, v, l in rows if tt == t]
        md.append("")
    md += ["## Sách (không có liên kết)", "",
           "- Tinkham, *Introduction to Superconductivity*, 2nd ed., McGraw-Hill (1996).",
           "- Nazarov & Blanter, *Quantum Transport: Introduction to Nanoscience*, Cambridge University Press (2009).",
           "- de Gennes, *Superconductivity of Metals and Alloys*, Benjamin (1966).",
           "- Breuer & Petruccione, *The Theory of Open Quantum Systems*, Oxford University Press (2002).", ""]
    out.write_text("\n".join(md), encoding="utf-8")
    print(f"wrote {out}", stats)


if __name__ == "__main__":
    main()
