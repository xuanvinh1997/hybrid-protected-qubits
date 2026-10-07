import numpy as np

from hpq import dephasing as D
from hpq import tightbinding as TB


def test_shot_noise_limits():
    kappa, nbar = 1.0, 0.05
    assert np.isclose(D.photon_shot_dephasing(1e-3, kappa, nbar), D.photon_shot_weak(1e-3, kappa, nbar), rtol=1e-3)
    assert np.isclose(D.photon_shot_dephasing(1e3, kappa, 1e-3), D.photon_shot_strong(kappa, 1e-3), rtol=1e-2)


def test_shot_noise_large_nbar_departs_from_small_nbar_formula():
    """The proposal's chi^2 nbar kappa/(chi^2+kappa^2) form fails once nbar ~ 1."""
    chi, kappa, nbar = 0.1, 1.0, 1.0
    full = D.photon_shot_dephasing(chi, kappa, nbar)
    approx = chi**2 * nbar * kappa / (chi**2 + kappa**2)
    assert full / approx > 1.5


def test_tight_binding_abs_converges_to_beenakker():
    """Error vs Beenakker scales ~ L/xi ~ Delta: halving Delta halves the error."""
    phi, V = 1.5, 1.0
    tau = TB.transmission_single_site(V)
    exact = np.sqrt(1 - tau * np.sin(phi / 2) ** 2)
    errs = []
    for d, nl in ((0.08, 260), (0.04, 520)):
        errs.append(TB.lowest_abs(phi, delta=d, n_lead=nl, n_normal=2, barrier=V) / d - exact)
    assert abs(errs[1]) < abs(errs[0])
    assert np.isclose(errs[0] / errs[1], 2.0, rtol=0.15)
