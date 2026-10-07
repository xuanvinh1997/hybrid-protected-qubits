"""OQ-1: which disorder parameters couple the zeta mode to the 0-pi qubit?

Uses scqubits.FullZeroPi (Groszkowski et al. 2018 Hamiltonian):
    H_int = 2 E_CS dC d_theta d_zeta + E_L dE_L phi zeta
and second-order perturbation theory for the qubit dispersive shift
    chi_l = sum_{l'} |g_{l l'}|^2 * 2 D / (D^2 - w_zeta^2),  D = E_l - E_l',
    chi_qz = chi_1 - chi_0.

Expected (structural argument in src/derivations/dv3-zeta-coupling.md):
    chi_qz is (almost) independent of dE_J and vanishes when dE_L = dC = 0.
Parameters are illustrative (GHz), not a fitted device; change BASE to test soft 0-pi.
"""
import warnings

import numpy as np

warnings.filterwarnings("ignore")
import scqubits as scq  # noqa: E402

scq.settings.PROGRESSBAR_DISABLED = True
BASE = dict(grid=scq.Grid1d(-6 * np.pi, 6 * np.pi, 170), EJ=10.0, EL=0.04, ECJ=20.0, EC=0.04,
            ECS=None, ng=0.0, flux=0.0, ncut=30, zeropi_cutoff=12, zeta_cutoff=10)


def chi_qz(dEJ, dEL, dC, dCJ=0.0):
    q = scq.FullZeroPi(dEJ=dEJ, dEL=dEL, dC=dC, dCJ=dCJ, **BASE)
    ev, vecs = q._zeropi.eigensys(evals_count=12)
    g = q.g_coupling_matrix(vecs)
    w = q.E_zeta

    def shift(l):
        return sum(abs(g[l, k]) ** 2 * 2 * (ev[l] - ev[k]) / ((ev[l] - ev[k]) ** 2 - w**2)
                   for k in range(len(ev)) if k != l)

    return shift(1) - shift(0), ev[1] - ev[0], w


if __name__ == "__main__":
    _, w01, wz = chi_qz(0, 0.05, 0.05)
    print(f"omega_01 = {w01*1e3:.2f} MHz, omega_zeta = {wz*1e3:.1f} MHz")
    print("\nchi_qz [kHz] vs dE_J (dE_L = dC = 0.05):")
    for d in (0.0, 0.02, 0.05, 0.1):
        print(f"  dE_J = {d:4.2f}:  {chi_qz(d, 0.05, 0.05)[0]*1e6:9.3f}")
    print("\nchi_qz [kHz] vs dE_L = dC (dE_J = 0.1):")
    for d in (0.0, 0.01, 0.02, 0.05):
        print(f"  dE_L = dC = {d:4.2f}:  {chi_qz(0.1, d, d)[0]*1e6:9.3f}")
    print("\nseparately (dE_J = 0):")
    print(f"  dE_L only 0.05: {chi_qz(0, 0.05, 0.0)[0]*1e6:9.3f}")
    print(f"  dC   only 0.05: {chi_qz(0, 0.0, 0.05)[0]*1e6:9.3f}")
