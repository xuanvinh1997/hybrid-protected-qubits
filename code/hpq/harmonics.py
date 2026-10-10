"""Charge dispersion of a single-island circuit with Josephson harmonics, and its WKB exponent.

H = 4 E_C (n - n_g)^2 - sum_M E_{J,M} cos(M phi),  E_{J,M} = r_M E_{J,1}.
In the charge basis cos(M phi) = (|n><n+M| + h.c.)/2, so H is banded.

WKB / instanton: the band width of the lowest level is  eps_0 ~ exp(-S),
    S = int_0^{2 pi} dphi sqrt((V(phi) - V(0)) / (4 E_C)),   V = -sum_M E_{J,M} cos(M phi),
(zero-point correction only changes the prefactor and an O(1) shift of S).
With E_{J,2} = r E_{J,1}:  S = sqrt(E_{J,1}/E_C) * s(r),
    s(r) = int_0^{2 pi} dphi sqrt((1 - cos phi)(1 + 2 r (1 + cos phi)) / 4),   s(0) = sqrt(8).
Single well at phi = 0 requires r >= -1/4.  (hypothesis H3 in src/outline-revision.md)
"""
from __future__ import annotations

import numpy as np
from scipy.integrate import quad


def levels(EJ1: float, EC: float, r: float = 0.0, ng: float = 0.0, k: int = 3, ncut: int = 50) -> np.ndarray:
    n = np.arange(-ncut, ncut + 1)
    N = 2 * ncut + 1
    H = np.diag(4 * EC * (n - ng) ** 2).astype(float)
    H -= 0.5 * EJ1 * (np.eye(N, k=1) + np.eye(N, k=-1))
    H -= 0.5 * r * EJ1 * (np.eye(N, k=2) + np.eye(N, k=-2))
    return np.linalg.eigvalsh(H)[:k]


def charge_dispersion(EJ1: float, EC: float, r: float = 0.0, k: int = 1) -> np.ndarray:
    return levels(EJ1, EC, r, 0.5, k) - levels(EJ1, EC, r, 0.0, k)


def wkb_s(r: float) -> float:
    if r < -0.25:
        raise ValueError("r < -1/4: phi=0 is no longer the global minimum")
    f = lambda p: np.sqrt(max((1 - np.cos(p)) * (1 + 2 * r * (1 + np.cos(p))), 0.0) / 4)
    return quad(f, 0, 2 * np.pi, limit=200)[0]


def numeric_s(r: float, x_lo: float = 4.0, x_hi: float = 7.0, npts: int = 7) -> float:
    """-d ln|eps_0| / d x,  x = sqrt(E_J1/E_C), by least squares on ln(eps) + 0.75*... prefactor-corrected.

    The prefactor scales ~ x^{3/2} (Koch 2007, Eq. 2.5); we fit ln|eps| - 1.5 ln x linearly in x.
    """
    xs = np.linspace(x_lo, x_hi, npts)
    y = [np.log(abs(charge_dispersion(x**2, 1.0, r)[0])) - 1.5 * np.log(x) for x in xs]
    return -np.polyfit(xs, y, 1)[0]
