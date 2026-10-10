import math

import numpy as np
import pytest

from hpq import harmonics as H
from hpq import transmon as T


def test_wkb_reduces_to_koch_exponent():
    assert H.wkb_s(0.0) == pytest.approx(math.sqrt(8), rel=1e-8)


def test_levels_reduce_to_transmon_when_r_zero():
    assert np.allclose(H.levels(40.0, 1.0, 0.0, 0.3), T.levels(40.0, 1.0, 0.3, 3), atol=1e-10)


def test_wkb_exponent_matches_numerics_with_harmonic():
    for r in (0.1, 0.0, -0.1, -0.15):
        assert H.numeric_s(r) == pytest.approx(H.wkb_s(r), rel=0.06)


def test_negative_second_harmonic_weakens_exponential_protection():
    # physical sign for a short junction (r<0) lowers the barrier -> larger charge dispersion
    assert H.wkb_s(-0.10) < H.wkb_s(0.0) < H.wkb_s(0.10)
    # measured: x2-3 at E_J1/E_C = 36-64 (prefactor also shifts, so < exp[(s(0)-s(r)) x] ~ 4-5)
    ratio = abs(H.charge_dispersion(49.0, 1.0, -0.10)[0]) / abs(H.charge_dispersion(49.0, 1.0, 0.0)[0])
    assert 1.5 < ratio < 4.0
