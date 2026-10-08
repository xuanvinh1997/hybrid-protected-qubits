"""Cooper-pair box / transmon in the charge basis.

H = 4 E_C (n - n_g)^2 - E_J cos(phi),  [phi, n] = i,  phi compact.
In the charge basis cos(phi) = (|n><n+1| + h.c.)/2, so H is tridiagonal; for E_J/E_C up to
~10^3 a cutoff |n| <= 40 converges far below the energies of interest.
"""
from __future__ import annotations

import math

import numpy as np


def levels(EJ: float, EC: float, ng: float = 0.0, k: int = 4, ncut: int = 40) -> np.ndarray:
    n = np.arange(-ncut, ncut + 1)
    H = np.diag(4 * EC * (n - ng) ** 2) - 0.5 * EJ * (np.eye(2 * ncut + 1, k=1) + np.eye(2 * ncut + 1, k=-1))
    return np.linalg.eigvalsh(H)[:k]


def charge_dispersion(EJ: float, EC: float, k: int = 3) -> np.ndarray:
    """eps_m = E_m(n_g = 1/2) - E_m(n_g = 0)."""
    return levels(EJ, EC, 0.5, k) - levels(EJ, EC, 0.0, k)


def charge_dispersion_asymptotic(EJ: float, EC: float, m: int) -> float:
    """Koch et al. (2007) Eq. (2.5), leading order in sqrt(E_J/E_C) -> infinity."""
    return ((-1) ** m * EC * 2 ** (4 * m + 5) / math.factorial(m) * math.sqrt(2 / math.pi)
            * (EJ / (2 * EC)) ** (m / 2 + 0.75) * math.exp(-math.sqrt(8 * EJ / EC)))


def omega01_asymptotic(EJ: float, EC: float) -> float:
    return math.sqrt(8 * EJ * EC) - EC


def anharmonicity(EJ: float, EC: float) -> float:
    e = levels(EJ, EC, 0.0, 3)
    return (e[2] - e[1]) - (e[1] - e[0])
