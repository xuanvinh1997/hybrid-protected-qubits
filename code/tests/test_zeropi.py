import numpy as np
import pytest

from hpq.zeropi import HybridZeroPi

# Moderate (fast) parameters; not a physical device.
BASE = dict(EL=0.04, ECt=0.02, ECp=10.0, ncut=18, n_phi=161, phi_max=5 * np.pi)
EJ = 10.0


def q01(**kw):
    q = HybridZeroPi.symmetric(EJ, **kw, **BASE)
    e = q.eigenvals(4)
    return e[1] - e[0]


def test_hermitian():
    H = HybridZeroPi.symmetric(EJ, dEJ=0.1, r=-0.125, **BASE).hamiltonian()
    assert abs(H - H.getH()).max() < 1e-12


def test_flux_sweet_spot_any_dEJ_and_r():
    """d omega / d phi_ext = 0 at phi_ext = 0 by phi -> -phi (with theta -> -theta) symmetry."""
    h = 1e-3
    for kw in (dict(dEJ=0.0, r=0.0), dict(dEJ=0.1, r=-0.125)):
        up = q01(phi_ext=+h, **kw)
        dn = q01(phi_ext=-h, **kw)
        assert abs(up - dn) / (2 * h) < 1e-6 * abs(up) / h


def test_symmetry_forbids_phi_expectation():
    q = HybridZeroPi.symmetric(EJ, dEJ=0.1, r=-0.125, **BASE)
    _, v = q.eigensys(4)
    P = q.phi_operator()
    for i in range(2):
        assert abs(q.matrix_element(P, v, i, i)) < 1e-6


def test_matches_scqubits_zeropi():
    scq = pytest.importorskip("scqubits")
    scq.settings.PROGRESSBAR_DISABLED = True
    # scqubits: -2 E_CJ d_phi^2 + 2 E_CS (i d_theta - ng)^2 ...  ->  ECp = E_CJ/2, ECt = E_CS/2
    zp = scq.ZeroPi(grid=scq.Grid1d(-5 * np.pi, 5 * np.pi, 321), ncut=18, EJ=EJ, EL=0.04,
                    ECJ=2 * BASE["ECp"], EC=None, ECS=2 * BASE["ECt"], ng=0.0, flux=0.0, dEJ=0.0, dCJ=0.0)
    ref = zp.eigenvals(4)
    # scqubits uses a higher-order phi stencil; our 3-point stencil needs a finer grid (O(h^2)).
    ours = HybridZeroPi.symmetric(EJ, dEJ=0.0, r=0.0, **{**BASE, "n_phi": 641}).eigenvals(4)
    assert np.allclose(np.diff(ours), np.diff(ref), rtol=1e-3, atol=1e-6)
