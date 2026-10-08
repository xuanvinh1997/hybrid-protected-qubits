import numpy as np

from hpq import transmon as T


def test_ground_charge_dispersion_matches_asymptotic():
    for r, tol in ((50, 0.06), (100, 0.04)):
        num = abs(T.charge_dispersion(r, 1.0)[0])
        asy = abs(T.charge_dispersion_asymptotic(r, 1.0, 0))
        assert abs(asy / num - 1) < tol


def test_excited_state_dispersion_converges_slowly_but_sign_alternates():
    d = T.charge_dispersion(100.0, 1.0)
    assert d[0] > 0 and d[1] < 0 and d[2] > 0
    # m=2 asymptotic is only an order-of-magnitude guide at E_J/E_C=100
    ratio = T.charge_dispersion_asymptotic(100.0, 1.0, 2) / d[2]
    assert 1.0 < ratio < 2.0


def test_transmon_frequency_and_anharmonicity():
    EJ, EC = 100.0, 1.0
    e = T.levels(EJ, EC, 0.0, 2)
    assert abs((e[1] - e[0]) / T.omega01_asymptotic(EJ, EC) - 1) < 2e-3
    assert abs(T.anharmonicity(EJ, EC) / (-EC) - 1) < 0.12


def test_gauge_equivalence_of_ng_periodicity():
    # spectrum is periodic in n_g with period 1
    assert np.allclose(T.levels(30, 1, 0.3), T.levels(30, 1, 1.3), atol=1e-10)
