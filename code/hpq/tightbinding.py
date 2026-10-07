"""Minimal 1D tight-binding BdG model of an S-N-S junction.

Stepping stone before Kwant (see src/e-numerics/e2-kwant-bdg.md). Spin-degenerate,
2x2 Nambu per site: (c_up, c_down^dagger). Phase difference phi is split
symmetrically: Delta*exp(+i phi/2) on the left lead, Delta*exp(-i phi/2) on the right.

Units: hopping t = 1, lattice constant a = 1.
"""
from __future__ import annotations

import numpy as np


def sns_bdg(phi: float, *, n_lead: int = 400, n_normal: int = 4, mu: float = 0.0,
            delta: float = 0.05, barrier: float = 0.0, t: float = 1.0) -> np.ndarray:
    """Dense BdG matrix (size 2N) of a 1D S-N-S chain.

    The normal region has `n_normal` sites; `barrier` is an on-site potential added
    to the middle normal site (sets the transmission tau).
    """
    n = 2 * n_lead + n_normal
    h = np.zeros((n, n))
    idx = np.arange(n - 1)
    h[idx, idx + 1] = h[idx + 1, idx] = -t
    h -= mu * np.eye(n)
    h[n_lead + n_normal // 2, n_lead + n_normal // 2] += barrier

    d = np.zeros(n, dtype=complex)
    d[:n_lead] = delta * np.exp(+0.5j * phi)
    d[n_lead + n_normal:] = delta * np.exp(-0.5j * phi)

    H = np.zeros((2 * n, 2 * n), dtype=complex)
    H[:n, :n] = h
    H[n:, n:] = -h.conj()
    H[:n, n:] = np.diag(d)
    H[n:, :n] = np.diag(d.conj())
    return H


def transmission_single_site(barrier: float, mu: float = 0.0, t: float = 1.0) -> float:
    """Normal-state transmission through one on-site potential in a 1D chain at energy mu.

    E = -2t cos k  ->  tau = 1 / (1 + (V / (2 t sin k))^2).
    """
    k = np.arccos(-mu / (2 * t))
    return 1.0 / (1.0 + (barrier / (2 * t * np.sin(k))) ** 2)


def lowest_abs(phi: float, **kw) -> float:
    """Smallest positive BdG eigenvalue (the Andreev bound state for a short junction)."""
    from scipy.linalg import eigh

    delta = kw.get("delta", 0.05)
    ev = eigh(sns_bdg(phi, **kw), eigvals_only=True, subset_by_value=(0.0, 1.5 * delta))
    return float(ev.min())


def ground_state_energy(phi: float, **kw) -> float:
    """E_GS(phi) = -sum_{E>0} E  (2x2 Nambu per spin block; factor 2 spin x 1/2)."""
    ev = np.linalg.eigvalsh(sns_bdg(phi, **kw))
    return float(-ev[ev > 0].sum())
