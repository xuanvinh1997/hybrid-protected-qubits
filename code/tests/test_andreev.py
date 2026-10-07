import numpy as np
import pytest

from hpq import andreev as A


def test_table1_of_proposal():
    # Proposal Table 1 (units of Delta, 3 decimals)
    expected = {0.50: (0.146, -0.006, 0.001), 0.90: (0.330, -0.041, 0.011), 0.99: (0.408, -0.074, 0.028)}
    for tau, ref in expected.items():
        e = A.fourier_coefficients(tau, m_max=3)
        assert np.allclose(e, ref, atol=6e-4), (tau, e)


def test_transparent_closed_form():
    e_num = A.fourier_coefficients(1.0, m_max=4, n_grid=2**16)
    e_ex = A.fourier_coefficients_transparent(4)
    assert np.allclose(e_num, e_ex, rtol=1e-6)
    assert np.isclose(e_ex[1] / e_ex[0], -0.2)


def test_tunnel_limit_and_ambegaokar_baratoff():
    tau = 1e-3
    e1, e2 = A.tunnel_limit(tau)
    num = A.fourier_coefficients(tau, m_max=2)
    assert np.isclose(num[0], e1, rtol=1e-6)
    assert np.isclose(num[1], e2, rtol=1e-3)
    # E_J = Delta * tau / 4 at leading order  <=>  I_c R_N = pi Delta / 2e
    assert np.isclose(num[0], tau / 4, rtol=1e-3)
    assert np.isclose(A.harmonic_ratio(tau), -tau / 16, rtol=1e-2)


def test_ratio_monotone_negative():
    taus = np.linspace(0.05, 0.99, 30)
    r = np.array([A.harmonic_ratio(t) for t in taus])
    assert np.all(r < 0) and np.all(np.diff(r) < 0)


def test_series_reconstructs_potential():
    tau, phi = 0.9, np.linspace(-np.pi, np.pi, 101)
    e = A.fourier_coefficients(tau, m_max=40)
    u_series = -np.cos(np.outer(phi, np.arange(1, 41))) @ e
    u_exact = A.junction_potential(phi, [tau])
    diff = (u_series - u_series.mean()) - (u_exact - u_exact.mean())
    assert np.max(np.abs(diff)) < 1e-6


def test_dorokhov_sampler_density():
    t = A.sample_dorokhov(200_000, tau_min=1e-4, rng=1)
    # P(tau > 1/2) for rho ~ 1/(tau sqrt(1-tau)) on [tau_min, 1]: x < arccosh(sqrt 2)
    x_max = np.arccosh(1 / np.sqrt(1e-4))
    assert np.isclose(np.mean(t > 0.5), np.arccosh(np.sqrt(2)) / x_max, atol=5e-3)


@pytest.mark.parametrize("tau_mean", [0.5])
def test_multichannel_is_not_bounded_by_single_channel(tau_mean):
    """Counter-example to 'single-channel r is an upper bound for |r_eff|' (see B2)."""
    t = A.sample_dorokhov(400, tau_min=1e-3, rng=0)
    # Dorokhov ensemble with comparable mean transmission
    r_eff = A.effective_ratio(t)
    r_single = A.harmonic_ratio(float(np.mean(t)))
    assert abs(r_eff) > abs(r_single)
