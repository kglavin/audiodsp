"""Equalizer biquads from Robert Bristow-Johnson's Audio EQ Cookbook."""

import numpy as np


def rbj_biquad(kind, f0, fs, q=1 / np.sqrt(2), gain_db=0.0):
    """Biquad coefficients (b, a), normalized so a[0] = 1.

    kind is 'peaking', 'lowshelf' or 'highshelf'. f0 is the center (peaking) or
    midpoint (shelf) frequency in Hz. The cookbook formulas are the bilinear
    transform of an analog prototype with f0 pre-warped, so f0 lands exactly.
    """
    A = 10 ** (gain_db / 40)
    w0 = 2 * np.pi * f0 / fs
    cos_w0 = np.cos(w0)
    alpha = np.sin(w0) / (2 * q)
    if kind == 'peaking':
        b = [1 + alpha * A, -2 * cos_w0, 1 - alpha * A]
        a = [1 + alpha / A, -2 * cos_w0, 1 - alpha / A]
    elif kind in ('lowshelf', 'highshelf'):
        sign = 1 if kind == 'lowshelf' else -1
        k = 2 * np.sqrt(A) * alpha
        b = [A * ((A + 1) - sign * (A - 1) * cos_w0 + k),
             sign * 2 * A * ((A - 1) - sign * (A + 1) * cos_w0),
             A * ((A + 1) - sign * (A - 1) * cos_w0 - k)]
        a = [(A + 1) + sign * (A - 1) * cos_w0 + k,
             -sign * 2 * ((A - 1) + sign * (A + 1) * cos_w0),
             (A + 1) + sign * (A - 1) * cos_w0 - k]
    else:
        raise ValueError(f"unknown kind {kind!r}")
    b, a = np.array(b), np.array(a)
    return b / a[0], a / a[0]
