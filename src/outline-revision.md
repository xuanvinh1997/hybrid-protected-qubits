# Điều chỉnh đề cương theo ba hướng H1 / H3 / H5

Trạng thái: **bản nháp 11/10/2026**. Căn cứ: [OQ-1](open-questions.md), [DV3](derivations/dv3-zeta-coupling.md), kết quả số mới ở [`check_instanton_harmonics.py`](../code/scripts/check_instanton_harmonics.py), và kiểm chứng trích dẫn bên dưới. Ánh xạ "Nội dung 1–3" lấy từ [lộ trình](roadmap.md) (ND1 = vi mô → mạch; ND2 = thiết kế cos2φ lai và độ bền rối loạn; ND3 = động lực học cổng chuyển mức bảo vệ). **Cần đối chiếu với văn bản đề cương gốc** vì kho này không chứa nó.

## 1. Kết luận ngắn

1. **H1 là hướng thay đổi đề cương nhiều nhất**, vì nó là khung chặt chẽ cho đúng chỗ OQ-1 đã làm lung lay: lập luận trung tâm "cân bằng $dE_J$ bằng cổng nâng $T_{2R}$ lên ≈ 1,08 ms" không đứng được trong mô hình Groszkowski ($dE_J$ không ghép tới ζ). Thay vì sửa một con số, đề cương nên đổi **luận điểm** thành: *phân loại các tham số rối loạn theo cách chúng phá đối xứng, và chỉ ra tham số nào điều khiển được bằng cổng.*
2. **H3 là phép đo độ bền định lượng** cho ND1→ND2: mối nối vi mô cho ra $r=E_{J,2}/E_{J,1}$ (âm), và $r$ đi thẳng vào hành động instanton $S$. Đã kiểm số cho mô hình một đảo (xem §3); phần cho 0-π (hai giếng, tách miền) **chưa làm**.
3. **H5 là công cụ, không phải mục tiêu mới.** Không thêm Nội dung thứ tư. Đưa vào phần phương pháp của ND2–ND3 (kiểm chứng số cho mạch có chuỗi JJ, và Lindblad dạng MPO nếu cần cho cổng).

Khuyến nghị cho đợt trả lời hội đồng: giữ nguyên tên đề tài và ba Nội dung; chỉ đổi cách phát biểu luận điểm của ND2 và thêm các câu hỏi kiểm chứng được. Không thay cấu trúc.

## 2. H1 — quy tắc chọn lọc cho rối loạn

**Đã có (DV3):** biến đổi $(\varphi_1..\varphi_4)\to(\theta,\varphi,\zeta,\Sigma)$ cố định, nên pha mối nối là $\theta\pm\varphi$ chính xác; $dE_J$ và mọi $d_M$ chỉ nằm trong khối $(\theta,\varphi)$. ζ chỉ ghép qua $dC$ (động năng) và $dE_L$ (thế điện cảm). Kiểm số: $\chi_{q\zeta}$ đổi 0,6% khi $dE_J:0\to0{,}1$.

**H1 thêm được gì (cần dẫn xuất, chưa có):** phát biểu lại kết quả trên như một quy tắc chọn lọc nhóm: nhóm đối xứng $G$ của mạch danh định (phản xạ $\varphi\to-\varphi$, hoán vị nhánh, tịnh tiến $\theta$), mỗi tham số rối loạn $\delta p$ biến đổi theo một biểu diễn bất khả quy của $G$, và phần tử ma trận $\langle l|\partial_{\delta p}H|l'\rangle$ giữa các mức bảo vệ bị cấm trừ khi biểu diễn của $\delta p$ chứa tích $\Gamma_l\otimes\Gamma_{l'}$ (Wigner–Eckart). Hệ quả cần kiểm: bảng *tham số rối loạn × biểu diễn × kênh nhiễu nó mở ra*, trong đó $dE_J$ (cổng: có), $dE_L$, $dC$, $dC_J$ (cổng: không), $\varphi_0$ (cổng + $B$) nằm ở các hàng khác nhau. Đây chính là "ba câu hỏi xuyên suốt" của [bản đồ khái niệm](concept-map.md) được làm thành định lý có điều kiện.

**Thay đổi đề cương:**
- ND2: bỏ mục tiêu "tối ưu $dE_J\to0$ để đạt $T_{2R}$ cỡ ms". Thay bằng: (a) bảng quy tắc chọn lọc cho 0-π lai và cos2φ lai; (b) với mỗi kênh còn sống, tham số điều khiển được nào (nếu có) triệt nó; (c) giữ $dE_L$ là tham số điều khiển bằng cách thay siêu điện cảm bằng phần tử điều chỉnh được (hướng đã nêu ở DV3 §4.3).
- Giữ các lợi ích độc lập với OQ-1: điều hòa cos2φ, điều chỉnh $\bar E_J$.

## 3. H3 — ước lượng bảo vệ theo hàm mũ (đã kiểm số một phần)

Mô hình một đảo $H=4E_C(n-n_g)^2-E_{J,1}\cos\phi-E_{J,2}\cos2\phi$, $r=E_{J,2}/E_{J,1}$. WKB cho độ rộng dải $\varepsilon_0\sim e^{-S}$, $S=\sqrt{E_{J,1}/E_C}\;s(r)$,
$$s(r)=\int_0^{2\pi}\!d\phi\,\sqrt{\tfrac14(1-\cos\phi)\,[1+2r(1+\cos\phi)]},\qquad s(0)=\sqrt8 .$$

Kết quả (`code/hpq/harmonics.py`, `tests/test_harmonics.py`, 8 test xanh):

| $r$ | $s_{WKB}$ | $s$ từ chéo hoá | sai lệch |
|---|---|---|---|
| +0,10 | 3,007 | 2,985 | −0,8% |
| 0 | 2,828 | 2,816 | −0,5% |
| −0,10 | 2,627 | 2,636 | +0,4% |
| −0,20 | 2,383 | 2,447 | +2,7% |

Đọc kết quả:
- WKB đúng cho **số mũ** trong 3% trên $r\in[-0{,}2,0{,}1]$. $r=-0{,}10$ (giá trị hiệu dụng của phân bố Dorokhov, [DV1](derivations/dv1-beenakker-fourier.md)) giảm $S$ khoảng 7%; $r=-0{,}2$ (kênh trong suốt $\tau=1$) giảm 16%.
- Tác động lên $\varepsilon_0$ **ở E_J/E_C = 36–64 chỉ ×2–3** (r = −0,10) và ×4 (r = −0,20, E_J/E_C = 36), nhỏ hơn $e^{\Delta s\,x}$ ≈ 3–14 vì tiền thừa số cũng đổi. Không được ngoại suy tỉ số này sang E_J/E_C khác mà chưa chạy lại.
- Hàm ý: điều hòa âm của mối nối bán dẫn làm **yếu** bảo vệ kiểu transmon một cách vừa phải. Trong cos2φ thì điều hòa là tài nguyên, nên cùng hiệu ứng đổi dấu vai trò — cần phát biểu riêng cho từng thiết kế.

**Chưa làm (OQ-9):** hành động instanton cho 0-π thật (hai giếng $\theta$, bảo vệ do hai hàm sóng có giá đỡ rời nhau), và ước lượng chặn bằng Agmon / Helffer–Sjöstrand. Phần Agmon là toán thuần; chỉ nên đưa vào đề cương nếu muốn nhánh vật lý toán — đây là quyết định phạm vi, không phải kỹ thuật.

**Thay đổi đề cương:** ND1 đầu ra không chỉ là $\{E_{J,M}(V_g)\}$ mà cả $r(V_g)$ kèm thanh sai số, vì $r$ đi vào $S$; ND2 có một mục "ngân sách bảo vệ $e^{-S(r,E_J/E_C)}$ so với các kênh rối loạn của H1".

## 4. H5 — mạng tensor

Xác minh: Di Paolo et al. (arXiv:1912.01018) dùng DMRG đa mục tiêu cho Hamiltonian đầy đủ của fluxonium, mảng $N_J>200$ mối nối, so với mô hình một mode. Viola & Catelani (PRB 92, 224511): mode tập thể của mảng không giới hạn kết hợp đáng kể nếu ghép với môi trường yếu hơn qubit. Cả hai là **fluxonium**; chưa thấy kết quả cho 0-π trong phạm vi đã tra, nên không khẳng định đã có.

**Thay đổi đề cương:** không thêm mục tiêu. Thêm vào phương pháp: (i) chéo hoá phân cấp (scqubits `Circuit` + `HilbertSpace`) làm đường chuẩn cho 0-π có siêu điện cảm là mảng; (ii) MPO/Lindblad chỉ khi mô phỏng cổng ND3 vượt khả năng chéo hoá trực tiếp. Cổng quyết định ở [roadmap G1](roadmap.md): nếu mô hình 0-π đầy đủ + vài mode mảng chéo hoá được, **bỏ H5**.

## 5. Trạng thái kiểm chứng trích dẫn trong tài liệu H1/H3/H5

Tài liệu nêu một số trích dẫn "theo trí nhớ"; kết quả tra:

| Mục | Kết quả |
|---|---|
| Ferguson, Houck, Koch, PRX 3, 011003 (2013) | Có, arXiv:1208.5747. Trang abstract chỉ nói dùng đối xứng gần đúng cho mạch lớn, áp dụng fluxonium; **chưa xác minh** nó có quy tắc chọn lọc theo biểu diễn nhóm — đọc bài trước khi dựa vào |
| Ding et al. 2021 | Có, arXiv:2011.10564, tác giả Ding, Ku, Shi, Zhao (Alibaba). **Tạp chí chưa xác minh**; ghi "PRB" trong tài liệu là chưa kiểm |
| Osborne et al. 2024 | Có, arXiv:2304.08531; PRX Quantum 5, 020309 (theo URL APS trong kết quả tìm kiếm). Tác giả: Osborne, Larson, Jones, Simmonds, Gyenis, Lucas |
| Kerman 2020 | Có, arXiv:2010.14929; **không thấy tạp chí** |
| Viola & Catelani 2015 | Đúng: PRB 92, 224511, "Collective modes in the fluxonium qubit" |
| Di Paolo et al. (tensor network) | Có, arXiv:1912.01018, ghi npj Quantum Inf. 2021 (theo DOAJ); tác giả Di Paolo, Baker, Foley, Sénéchal, Blais. **Không nhầm** với Di Paolo 2019 NJP về 0-π đã có trong `refs.bib` |
| Rymarz et al. PRX 11, 011032 (2021) | Có, arXiv:2002.07718 |
| Le, Grimsmo, Müller, ~~Blais~~ **Stace** 2019 | Tài liệu H3 ghi sai tác giả cuối. arXiv:1904.01843, tác giả Le, Grimsmo, Müller, Stace; DOI 10.1103/PhysRevA.100.062321 (PRA 100, 062321 — suy từ DOI, trang arXiv không nêu tạp chí) |
