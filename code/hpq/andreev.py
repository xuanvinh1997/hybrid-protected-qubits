"""Short-junction Andreev physics: Beenakker spectrum and Fourier harmonics.

Convention (matches the thesis proposal, Eq. 12):
    U(phi) = -Delta * sum_n sqrt(1 - tau_n sin^2(phi/2))  =  const - sum_{M>=1} E_{J,M} cos(M phi)
    E_{J,M}(tau) = (Delta/pi) * int_{-pi}^{pi} sqrt(1 - tau sin^2(phi/2)) cos(M phi) dphi
Each channel index n is spin-degenerate.
"""
from __future__ import annotations

import numpy as np


def abs_energy(phi, tau, delta: float = 1.0):
    """Positive Andreev bound-state energy E_A^+(phi) of one spin-degenerate channel."""
    return delta * np.sqrt(1.0 - tau * np.sin(np.asarray(phi) / 2.0) ** 2)


def junction_potential(phi, taus, delta: float = 1.0):
    """Ground-state energy U(phi) = -Delta sum_n sqrt(1 - tau_n sin^2(phi/2))."""
    taus = np.atleast_1d(taus)
    phi = np.asarray(phi)
    return -delta * np.sum(np.sqrt(1.0 - taus[:, None] * np.sin(phi.ravel() / 2.0) ** 2), axis=0).reshape(phi.shape)


def fourier_coefficients(tau, m_max: int = 4, delta: float = 1.0, n_grid: int = 4096) -> np.ndarray:
    """E_{J,M}(tau) for M = 1..m_max.

    The integrand is smooth and 2pi-periodic, so the trapezoidal rule on a uniform grid
    converges exponentially (except at tau = 1, where it is algebraic; use n_grid large
    or `fourier_coefficients_transparent`).
    """
    phi = np.linspace(-np.pi, np.pi, n_grid, endpoint=False)
    f = np.sqrt(1.0 - tau * np.sin(phi / 2.0) ** 2)
    ms = np.arange(1, m_max + 1)
    return delta * 2.0 * (np.cos(np.outer(ms, phi)) @ f) / n_grid


def fourier_coefficients_transparent(m_max: int = 4, delta: float = 1.0) -> np.ndarray:
    """Exact tau = 1 result: E_{J,M} = (4 Delta / pi) (-1)^{M+1} / (4 M^2 - 1)."""
    ms = np.arange(1, m_max + 1)
    return delta * 4.0 / np.pi * (-1.0) ** (ms + 1) / (4.0 * ms**2 - 1.0)


def tunnel_limit(tau, delta: float = 1.0):
    """Leading small-tau expansion: E_{J,1} ~ Delta(tau/4 + tau^2/16), E_{J,2} ~ -Delta tau^2/64."""
    return delta * (tau / 4 + tau**2 / 16), -delta * tau**2 / 64


def harmonic_ratio(tau) -> float:
    """r = E_{J,2} / E_{J,1} for a single channel."""
    e = fourier_coefficients(tau, m_max=2)
    return float(e[1] / e[0])


def multichannel_coefficients(taus, m_max: int = 4, delta: float = 1.0) -> np.ndarray:
    """Sum_n E_{J,M}(tau_n) over channels."""
    return sum(fourier_coefficients(t, m_max, delta) for t in np.atleast_1d(taus))


def effective_ratio(taus) -> float:
    """r_eff = sum_n E_{J,2}(tau_n) / sum_n E_{J,1}(tau_n)."""
    e = multichannel_coefficients(taus, m_max=2)
    return float(e[1] / e[0])


def sample_dorokhov(n: int, tau_min: float = 1e-3, rng=None) -> np.ndarray:
    """Draw n transmissions from the diffusive Dorokhov density rho(tau) ~ 1/(tau sqrt(1-tau)).

    Uses tau = 1/cosh^2(x) with x uniform on [0, x_max], which maps exactly onto the
    Dorokhov density; tau_min sets the cutoff x_max = arccosh(1/sqrt(tau_min)).
    """
    rng = np.random.default_rng(rng)
    x_max = np.arccosh(1.0 / np.sqrt(tau_min))
    x = rng.uniform(0.0, x_max, size=n)
    return 1.0 / np.cosh(x) ** 2
