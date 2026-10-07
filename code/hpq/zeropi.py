"""(theta, phi) block of the 0-pi qubit with arbitrary Josephson harmonics per junction.

H = 4 E_Ct (n_t - n_g)^2 + 4 E_Cp n_p^2 + E_L phi^2
    - sum_{j in {A,B}} sum_M E^{(j)}_{J,M} cos(M (theta + s_j phi'))  ,   s_A = +1, s_B = -1,
    phi' = phi - phi_ext / 2.

For a single harmonic and E^A = E_J(1 + d), E^B = E_J(1 - d) this reduces to
    -2 E_J cos(theta) cos(phi') + 2 E_J d sin(theta) sin(phi'),
which is the proposal's Eq. (13) with dE_J = d.

Basis: charge states |n>, |n| <= ncut for theta (compact); uniform grid for phi (extended),
three-point finite-difference Laplacian with Dirichlet boundaries.
The zeta mode and the dC_J, dC, dE_L disorder terms are NOT included here; see
scripts/check_zeta_coupling.py and src/derivations/dv3-zeta-coupling.md.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla


@dataclass
class HybridZeroPi:
    EJA: list[float]                 # [E_{J,1}, E_{J,2}, ...] of junction A
    EJB: list[float]                 # same for junction B
    EL: float
    ECt: float                       # E_C,theta
    ECp: float                       # E_C,phi
    ng: float = 0.0
    phi_ext: float = 0.0             # reduced external flux 2 pi Phi_ext / Phi_0
    ncut: int = 20
    n_phi: int = 201
    phi_max: float = 5 * np.pi
    _grid: np.ndarray = field(init=False, repr=False)

    def __post_init__(self):
        self._grid = np.linspace(-self.phi_max, self.phi_max, self.n_phi)

    @classmethod
    def symmetric(cls, EJ: float, dEJ: float, r: float = 0.0, dEJ2: float | None = None, **kw):
        """Two-harmonic junctions: E^{A,B}_{J,1} = EJ(1 +- dEJ), E^{A,B}_{J,2} = r EJ (1 +- dEJ2)."""
        dEJ2 = dEJ if dEJ2 is None else dEJ2
        A = [EJ * (1 + dEJ), r * EJ * (1 + dEJ2)]
        B = [EJ * (1 - dEJ), r * EJ * (1 - dEJ2)]
        return cls(EJA=A, EJB=B, **kw)

    # ---- operators -------------------------------------------------------------
    @property
    def grid(self) -> np.ndarray:
        return self._grid

    @property
    def dim(self) -> int:
        return (2 * self.ncut + 1) * self.n_phi

    def _theta_shift(self, m: int) -> sp.csr_matrix:
        """e^{i m theta}: |n> -> |n+m>."""
        size = 2 * self.ncut + 1
        return sp.eye(size, k=-m, format="csr")

    def n_theta(self) -> sp.csr_matrix:
        n = np.arange(-self.ncut, self.ncut + 1, dtype=float)
        return sp.kron(sp.diags(n), sp.eye(self.n_phi), format="csr")

    def phi_operator(self) -> sp.csr_matrix:
        return sp.kron(sp.eye(2 * self.ncut + 1), sp.diags(self._grid), format="csr")

    def hamiltonian(self) -> sp.csr_matrix:
        nt = 2 * self.ncut + 1
        n = np.arange(-self.ncut, self.ncut + 1, dtype=float)
        h = self._grid[1] - self._grid[0]
        lap = sp.diags([np.ones(self.n_phi - 1), -2 * np.ones(self.n_phi), np.ones(self.n_phi - 1)],
                       [-1, 0, 1]) / h**2
        It, Ip = sp.eye(nt), sp.eye(self.n_phi)

        H = sp.kron(sp.diags(4 * self.ECt * (n - self.ng) ** 2), Ip)
        H = H + sp.kron(It, -4 * self.ECp * lap + sp.diags(self.EL * self._grid**2))

        phip = self._grid - self.phi_ext / 2
        for coeffs, s in ((self.EJA, +1), (self.EJB, -1)):
            for m, e in enumerate(coeffs, start=1):
                if e == 0:
                    continue
                term = sp.kron(self._theta_shift(m), sp.diags(np.exp(1j * s * m * phip)))
                H = H - 0.5 * e * (term + term.getH())
        return H.tocsr()

    def eigensys(self, k: int = 6):
        H = self.hamiltonian()
        e0 = -sum(abs(x) for x in self.EJA + self.EJB) - 1.0
        vals, vecs = spla.eigsh(H, k=k, sigma=e0, which="LM")
        order = np.argsort(vals)
        return vals[order], vecs[:, order]

    def eigenvals(self, k: int = 6) -> np.ndarray:
        return self.eigensys(k)[0]

    def matrix_element(self, op: sp.spmatrix, vecs: np.ndarray, i: int, j: int) -> complex:
        return complex(vecs[:, i].conj() @ (op @ vecs[:, j]))
