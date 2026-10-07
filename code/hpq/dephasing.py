"""Dephasing formulas.

Photon shot noise (Clerk & Utami, PRA 75, 042302 (2007)): a mode with decay rate kappa and
thermal occupation nbar, dispersively coupled so that the qubit frequency shifts by 2*chi per
photon. All rates in angular-frequency units of the inputs.
"""
from __future__ import annotations

import numpy as np


def photon_shot_dephasing(chi, kappa, nbar):
    """Full Clerk-Utami result, valid for any chi/kappa and nbar."""
    chi = np.asarray(chi, dtype=float)
    z = np.sqrt((1 + 2j * chi / kappa) ** 2 + 8j * chi * nbar / kappa)
    return 0.5 * kappa * np.real(z - 1)


def photon_shot_weak(chi, kappa, nbar):
    """chi << kappa limit: 4 chi^2 nbar (nbar + 1) / kappa."""
    return 4 * np.asarray(chi) ** 2 * nbar * (nbar + 1) / kappa


def photon_shot_strong(kappa, nbar):
    """chi >> kappa, nbar << 1 limit: kappa * nbar."""
    return kappa * nbar


def bose(freq_hz, temp_k):
    """Thermal occupation of a mode at frequency f (Hz) and temperature T (K)."""
    h, kb = 6.62607015e-34, 1.380649e-23
    return 1.0 / np.expm1(h * np.asarray(freq_hz) / (kb * temp_k))
