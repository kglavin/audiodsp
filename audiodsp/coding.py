"""Companding used in telephone audio."""

import numpy as np


def mu_law_compress(x, mu=255):
    """Map [-1, 1] to [-1, 1] with fine steps near zero and coarse steps near full scale.

    This is the continuous mu-law curve. The G.711 telephone standard uses a
    segmented approximation of it.
    """
    return np.sign(x) * np.log1p(mu * np.abs(x)) / np.log1p(mu)


def mu_law_expand(y, mu=255):
    """Inverse of mu_law_compress."""
    return np.sign(y) * np.expm1(np.abs(y) * np.log1p(mu)) / mu
