"""Reproduce proposal Fig. 3 and add the multichannel (Dorokhov) comparison.

Output: src/figures/beenakker_harmonics.png (committed, used by the book)
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from hpq import andreev as A

out = Path(__file__).resolve().parents[2] / "src" / "figures"
out.mkdir(exist_ok=True)

taus = np.linspace(1e-3, 0.999, 300)
E = np.array([A.fourier_coefficients(t, m_max=4) for t in taus])

fig, ax = plt.subplots(1, 2, figsize=(10, 3.8))
for m in range(4):
    ax[0].semilogy(taus, np.abs(E[:, m]), label=f"$|E_{{J,{m+1}}}|/\\Delta$")
ax[0].set_xlabel(r"$\tau$"); ax[0].legend(); ax[0].set_title("Single-channel harmonics")

ax[1].plot(taus, E[:, 1] / E[:, 0], label="single channel $r(\\tau)$")
ax[1].plot(taus, -taus / 16, "--", label=r"tunnel limit $-\tau/16$")
rng = np.random.default_rng(0)
for tmin in (1e-3, 1e-2, 0.1):
    t = A.sample_dorokhov(2000, tau_min=tmin, rng=rng)
    ax[1].plot(t.mean(), A.effective_ratio(t), "o", label=f"Dorokhov, $\\tau_{{min}}$={tmin:g}")
ax[1].axhline(-0.2, color="gray", lw=0.5)
ax[1].set_xlabel(r"$\tau$ (or $\langle\tau\rangle$)"); ax[1].set_ylabel(r"$E_{J,2}/E_{J,1}$")
ax[1].legend(fontsize=8); ax[1].set_title("Harmonic ratio")
fig.tight_layout()
fig.savefig(out / "beenakker_harmonics.png", dpi=150)
print("saved", out / "beenakker_harmonics.png")
