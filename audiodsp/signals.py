"""Test-signal generation and spectrum helpers shared by the project notebooks."""

import numpy as np


def time_axis(duration, sample_rate=44100):
    """Sample times in seconds for a signal of the given duration."""
    return np.arange(int(round(duration * sample_rate))) / sample_rate


def sine(frequency, duration, sample_rate=44100, amplitude=1.0, phase=0.0):
    """A single sine wave."""
    t = time_axis(duration, sample_rate)
    return amplitude * np.sin(2 * np.pi * frequency * t + phase)


def multi_sine(frequencies, duration, sample_rate=44100, amplitudes=None, phases=None):
    """Sum of sine waves. Amplitudes default to 1, phases to 0."""
    if amplitudes is None:
        amplitudes = [1.0] * len(frequencies)
    if phases is None:
        phases = [0.0] * len(frequencies)
    t = time_axis(duration, sample_rate)
    x = np.zeros_like(t)
    for f, a, p in zip(frequencies, amplitudes, phases):
        x += a * np.sin(2 * np.pi * f * t + p)
    return x


def add_noise(x, noise_level, rng=None):
    """Add white Gaussian noise with standard deviation noise_level."""
    rng = np.random.default_rng() if rng is None else rng
    return x + rng.normal(0, noise_level, len(x))


def spectrum_db(x, sample_rate, window="hann"):
    """One-sided magnitude spectrum in dB relative to the largest bin.

    Returns (frequencies_hz, magnitude_db).
    """
    from scipy.signal import get_window

    w = get_window(window, len(x))
    X = np.abs(np.fft.rfft(x * w))
    freqs = np.fft.rfftfreq(len(x), 1 / sample_rate)
    return freqs, 20 * np.log10(X / (X.max() + 1e-20) + 1e-12)
