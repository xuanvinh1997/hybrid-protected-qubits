"""H3 check: how Josephson harmonics (r = E_J2/E_J1) change the exponential protection exponent.

Prints WKB s(r) vs the exponent extracted from exact diagonalisation of the charge dispersion.
Physical sign for a short junction: r ~ -tau/16 (small tau), r = -1/5 at tau = 1, r_eff ~ -0.10 (diffusive),
see src/derivations/dv1-beenakker-fourier.md.
"""
import numpy as np

from hpq import harmonics as H

if __name__ == "__main__":
    print(f"{'r':>7} {'s_WKB':>8} {'s_num':>8} {'rel.err':>8} {'eps0(EJ/EC=36)':>16}")
    for r in (0.1, 0.0, -0.05, -0.10, -0.15, -0.20):
        sw, sn = H.wkb_s(r), H.numeric_s(r)
        e36 = abs(H.charge_dispersion(36.0, 1.0, r)[0])
        print(f"{r:7.2f} {sw:8.4f} {sn:8.4f} {sn / sw - 1:8.2%} {e36:16.3e}")
    # suppression of protection by the physical (negative) second harmonic, at fixed E_J1/E_C
    for x in (6.0, 8.0):
        d0 = abs(H.charge_dispersion(x**2, 1.0, 0.0)[0])
        d1 = abs(H.charge_dispersion(x**2, 1.0, -0.10)[0])
        print(f"E_J1/E_C={x**2:.0f}: eps(r=-0.10)/eps(r=0) = {d1 / d0:.1f}  "
              f"(exp[(s(0)-s(-0.1)) x] = {np.exp((H.wkb_s(0) - H.wkb_s(-0.10)) * x):.1f})")
