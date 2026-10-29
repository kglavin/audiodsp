"""Noise reduction and adaptive filtering."""

import numpy as np
from scipy import signal


def nlms(reference, primary, n_taps, step=0.5, eps=1e-6, adapt=None):
    """Normalized LMS adaptive filter.

    Learns the filter that turns `reference` into the part of `primary` that is
    correlated with it, and subtracts that part. Returns (error, weights), where
    error = primary - prediction is the cleaned signal. Where the optional boolean
    array `adapt` is False, the weights are held (used to pause adaptation).
    """
    w = np.zeros(n_taps)
    history = np.zeros(n_taps)          # reference[n], reference[n-1], ...
    error = np.empty(len(primary))
    for n in range(len(primary)):
        history[1:] = history[:-1]
        history[0] = reference[n]
        e = primary[n] - w @ history
        error[n] = e
        if adapt is None or adapt[n]:
            w += step * e * history / (history @ history + eps)
    return error, w


def noise_reduction(x, noise, fs, method='wiener', nperseg=512, floor=0.1, over_subtraction=1.0, dd_alpha=0.98):
    """STFT noise reduction, using a recording of the noise alone to estimate its spectrum.

    method='subtraction': power spectral subtraction, gain sqrt(1 - over_subtraction * N / |X|^2).
    method='wiener': Wiener gain xi / (1 + xi), with the a priori SNR xi estimated by the
    decision-directed rule (Ephraim and Malah), which suppresses musical noise.
    Gains never go below `floor`.
    """
    stft_args = dict(fs=fs, window='hann', nperseg=nperseg, noverlap=3 * nperseg // 4)
    _, _, X = signal.stft(x, **stft_args)
    _, _, N = signal.stft(noise, **stft_args)
    noise_psd = np.mean(np.abs(N) ** 2, axis=1) + 1e-20
    power = np.abs(X) ** 2
    if method == 'subtraction':
        gain = np.sqrt(np.maximum(1 - over_subtraction * noise_psd[:, None] / (power + 1e-20), floor ** 2))
    elif method == 'wiener':
        gain = np.empty_like(power)
        previous = np.zeros(len(noise_psd))           # |G X|^2 / N of the previous frame
        for m in range(power.shape[1]):
            snr_post = power[:, m] / noise_psd
            snr_prior = dd_alpha * previous + (1 - dd_alpha) * np.maximum(snr_post - 1, 0)
            gain[:, m] = np.maximum(snr_prior / (1 + snr_prior), floor)
            previous = gain[:, m] ** 2 * snr_post
    else:
        raise ValueError(f"unknown method {method!r}")
    _, y = signal.istft(gain * X, **stft_args)
    return y[:len(x)]
