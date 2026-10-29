"""Oscillators, envelopes and drum sounds."""

import numpy as np
from scipy import signal

from .signals import time_axis


def polyblep_saw(frequency, fs, n_samples, phase=0.0):
    """Band-limited sawtooth using PolyBLEP correction of the jump at each cycle start.

    `frequency` is a number or an array of n_samples per-sample frequencies.
    """
    dt = np.broadcast_to(np.asarray(frequency, dtype=float) / fs, (n_samples,))
    t = (phase + np.cumsum(dt) - dt) % 1.0          # phase in cycles, 0 <= t < 1
    y = 2 * t - 1
    start = t < dt                                   # just after the jump
    u = t[start] / dt[start]
    y[start] -= 2 * u - u * u - 1
    end = t > 1 - dt                                 # just before the jump
    u = (t[end] - 1) / dt[end]
    y[end] -= u * u + 2 * u + 1
    return y


def adsr(duration, fs, attack=0.01, decay=0.1, sustain=0.7, release=0.2):
    """Attack-decay-sustain-release envelope for a note held `duration` seconds.

    The result is `duration + release` seconds long.
    """
    a, d, hold, r = int(attack * fs), int(decay * fs), int(duration * fs), int(release * fs)
    held = np.concatenate((np.linspace(0, 1, a, endpoint=False),
                           np.linspace(1, sustain, d, endpoint=False),
                           np.full(max(hold - a - d, 0), sustain)))[:hold]
    last = held[-1] if hold else 0.0
    return np.concatenate((held, np.linspace(last, 0, r)))


def kick(fs, duration=0.4):
    """Sine whose pitch drops quickly from 150 to 50 Hz, plus a short click."""
    t = time_axis(duration, fs)
    freq = 50 + 100 * np.exp(-t / 0.03)
    body = np.sin(2 * np.pi * np.cumsum(freq) / fs) * np.exp(-t / 0.15)
    click = np.exp(-t / 0.002) * np.sin(2 * np.pi * 1500 * t)
    return body + 0.3 * click


def snare(fs, rng, duration=0.25):
    """A 185 Hz drum tone plus band-passed noise for the snare wires."""
    t = time_axis(duration, fs)
    tone = np.sin(2 * np.pi * 185 * t) * np.exp(-t / 0.05)
    wires = signal.sosfilt(signal.butter(2, [1000, 8000], btype='bandpass', fs=fs, output='sos'),
                           rng.normal(0, 1, len(t))) * np.exp(-t / 0.06)
    return 0.5 * tone + 0.6 * wires


def hat(fs, rng, duration=0.08):
    """High-passed noise with a very short decay."""
    t = time_axis(duration, fs)
    noise = signal.sosfilt(signal.butter(4, min(7000, 0.4 * fs), btype='highpass', fs=fs, output='sos'),
                           rng.normal(0, 1, len(t)))
    return noise * np.exp(-t / 0.015)


def drum_loop(bpm, bars, fs, rng=None, timing_jitter=0.0):
    """A rock beat: kick on beats 1 and 3 (and the "and" of 3), snare on 2 and 4, hi-hat on every eighth note.

    timing_jitter is the standard deviation, in seconds, of random hit timing errors.
    Returns (audio, beat_times): the loop and the times of its quarter-note beats.
    """
    rng = np.random.default_rng() if rng is None else rng
    step = 60 / bpm / 4                                    # one sixteenth note
    n_steps = 16 * bars
    x = np.zeros(int((n_steps * step + 0.5) * fs))
    sounds = {'kick': kick(fs), 'snare': snare(fs, rng), 'hat': hat(fs, rng)}
    pattern = {'kick': {0, 8, 10}, 'snare': {4, 12}, 'hat': {0, 2, 4, 6, 8, 10, 12, 14}}
    levels = {'kick': 1.0, 'snare': 0.8, 'hat': 0.25}
    for s in range(n_steps):
        for name, steps in pattern.items():
            if s % 16 in steps:
                start = int(max(0.0, s * step + rng.normal(0, timing_jitter)) * fs)
                sound = sounds[name][:len(x) - start]
                x[start:start + len(sound)] += levels[name] * sound
    beat_times = np.arange(0, n_steps, 4) * step
    return 0.8 * x / np.max(np.abs(x)), beat_times
