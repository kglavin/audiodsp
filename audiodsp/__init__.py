"""Shared helpers for the audiodsp project notebooks."""

from .coding import mu_law_compress, mu_law_expand
from .eq import rbj_biquad
from .restoration import nlms, noise_reduction
from .signals import (VOWEL_FORMANTS, add_noise, multi_sine, pluck, sine, spectrum_db,
                      synthetic_vowels, time_axis)
from .synthesis import adsr, drum_loop, hat, kick, polyblep_saw, snare
from .wav import read_wav, write_wav

__all__ = [
    "VOWEL_FORMANTS",
    "add_noise",
    "adsr",
    "drum_loop",
    "hat",
    "kick",
    "mu_law_compress",
    "mu_law_expand",
    "multi_sine",
    "nlms",
    "noise_reduction",
    "pluck",
    "polyblep_saw",
    "rbj_biquad",
    "read_wav",
    "sine",
    "snare",
    "spectrum_db",
    "synthetic_vowels",
    "time_axis",
    "write_wav",
]
