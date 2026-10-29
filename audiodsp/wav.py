"""WAV file read/write with float signals in the range [-1, 1]."""

import numpy as np
from scipy.io import wavfile


def write_wav(path, x, sample_rate=44100, normalize=True):
    """Write a float signal as 16-bit PCM. Peak-normalizes by default. Returns path."""
    x = np.asarray(x, dtype=float)
    if normalize:
        peak = np.max(np.abs(x))
        if peak > 0:
            x = x / peak
    wavfile.write(path, sample_rate, np.int16(np.clip(x, -1, 1) * 32767))
    return path


def read_wav(path, mono=True):
    """Read a WAV file as float in [-1, 1]. Returns (x, sample_rate).

    Handles 8-bit unsigned, 16/32-bit integer and float files. With mono=True,
    multi-channel files are averaged to one channel.
    """
    sample_rate, x = wavfile.read(path)
    if x.dtype == np.uint8:
        x = (x.astype(np.float64) - 128) / 128
    elif np.issubdtype(x.dtype, np.integer):
        x = x.astype(np.float64) / np.iinfo(x.dtype).max
    else:
        x = x.astype(np.float64)
    if mono and x.ndim > 1:
        x = x.mean(axis=1)
    return x, sample_rate
