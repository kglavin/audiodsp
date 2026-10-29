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


def pluck(frequency, duration, sample_rate=44100, n_harmonics=6, decay=0.25):
    """A plucked note: harmonics at 1/k amplitude, a 3 ms attack and an exponential decay."""
    t = time_axis(duration, sample_rate)
    note = sum(np.sin(2 * np.pi * k * frequency * t) / k
               for k in range(1, n_harmonics + 1) if k * frequency < sample_rate / 2)
    return note * (1 - np.exp(-t / 0.003)) * np.exp(-t / decay)


# (F1, F2, F3) in Hz: average adult male formants (Peterson and Barney, 1952)
VOWEL_FORMANTS = {
    'a': (730, 1090, 2440),   # as in "father"
    'e': (530, 1840, 2480),   # as in "bed"
    'i': (270, 2290, 3010),   # as in "beet"
    'o': (570, 840, 2410),    # as in "bought"
    'u': (300, 870, 2240),    # as in "boot"
}


def synthetic_vowels(vowels='aeiou', sample_rate=16000, f0=120.0, vowel_duration=0.35, gap=0.15, lead_in=0.5):
    """Speech-like test signal built with the source-filter model of the voice.

    A glottal pulse train (with falling pitch, as at the end of a sentence) is shaped by
    three formant resonators per vowel. Vowels are separated by silences, and the signal
    starts with `lead_in` seconds of silence. Returns (x, active): the signal, peak 0.5,
    and a boolean mask that is True where a vowel sounds.
    """
    from scipy.signal import lfilter

    fs = sample_rate
    seg, gap_n, pos = int(vowel_duration * fs), int(gap * fs), int(lead_in * fs)
    x = np.zeros(pos + len(vowels) * (seg + gap_n))
    active = np.zeros(len(x), dtype=bool)
    t = np.arange(seg) / fs
    ramp = np.minimum(1, np.minimum(t, t[::-1]) / 0.02)       # 20 ms fade in and out
    for v in vowels:
        f = f0 * (1.1 - 0.2 * t / vowel_duration)              # pitch falls by about 20%
        phase = np.cumsum(f / fs)
        pulses = np.diff(np.floor(phase), prepend=0.0)        # one impulse per glottal cycle
        source = lfilter([1.0], [1.0, -0.97], lfilter([1.0], [1.0, -0.97], pulses))   # glottal pulse shape
        y = lfilter([1.0, -1.0], [1.0], source)                # radiation from the lips
        for F, B in zip(VOWEL_FORMANTS[v], (60, 90, 120)):
            r, theta = np.exp(-np.pi * B / fs), 2 * np.pi * F / fs
            a = [1.0, -2 * r * np.cos(theta), r * r]
            y = lfilter([sum(a)], a, y)                        # resonator with gain 1 at 0 Hz
        x[pos:pos + seg] = y * ramp
        active[pos:pos + seg] = True
        pos += seg + gap_n
    return 0.5 * x / np.max(np.abs(x)), active


def spectrum_db(x, sample_rate, window="hann"):
    """One-sided magnitude spectrum in dB relative to the largest bin.

    Returns (frequencies_hz, magnitude_db).
    """
    from scipy.signal import get_window

    w = get_window(window, len(x))
    X = np.abs(np.fft.rfft(x * w))
    freqs = np.fft.rfftfreq(len(x), 1 / sample_rate)
    return freqs, 20 * np.log10(X / (X.max() + 1e-20) + 1e-12)
