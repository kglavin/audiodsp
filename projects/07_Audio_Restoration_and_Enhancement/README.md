Module 07: Audio Restoration and Enhancement

Notebook:
- [restoration.ipynb](restoration.ipynb): spectral subtraction and decision-directed Wiener noise reduction (on synthetic speech), adaptive noise cancellation with NLMS, click detection with linear prediction and least-squares AR interpolation, and de-clipping. Covers all four projects below.

Here are some software mini projects that can be used to educate about the topic of Audio Restoration and Enhancement and its sub-topics:

## Noise Reduction Tool: Develop a software tool that allows users to apply different noise reduction techniques to audio signals. Users can input audio files with varying levels of background noise. The tool should provide options for adaptive filtering, spectral subtraction, or other noise reduction algorithms. Users can adjust parameters such as noise estimation, suppression levels, and observe the effects on the audio signal in real-time. This project will help understand different noise reduction techniques and their applications in audio restoration.

## De-clicking and De-noising Application: Create a software application that focuses on removing clicks, pops, and other impulsive noise from audio signals. Users can input audio files with such artifacts. The application should provide options for de-clicking and de-noising algorithms, such as median filtering or spectral editing. Users can adjust parameters to control the aggressiveness of the removal and listen to the processed audio in real-time. This project will help understand the specific challenges of removing impulsive noise and the techniques employed for de-clicking and de-noising.

## De-clipping: Build a software tool that restores audio signals that have been clipped. Users can input audio files with clipping distortion. The tool should detect clipped samples and provide options for de-clipping algorithms, such as peak restoration or waveform reconstruction by interpolation. This project will help understand the techniques used to restore clipped audio. (Dynamic range compression and expansion moved to `05_Audio_Effects`.)

## Speech Enhancement Software: Develop a software application that focuses on enhancing speech intelligibility in audio recordings. Users can input audio files with speech in noisy or reverberant environments. The application should provide options for speech enhancement algorithms, such as noise reduction, dereverberation, and speech-specific enhancement techniques. Users can adjust parameters and observe the effects on the speech clarity in real-time. This project will help understand the challenges of speech enhancement and the techniques employed to improve speech intelligibility.

## Further reading

**Start here**
- [Noise reduction](https://en.wikipedia.org/wiki/Noise_reduction) (Wikipedia).

**Background**
- S. Boll, [Suppression of acoustic noise in speech using spectral subtraction](https://doi.org/10.1109/TASSP.1979.1163209), IEEE Transactions on Acoustics, Speech, and Signal Processing, 1979.
- Y. Ephraim and D. Malah, [Speech enhancement using a minimum mean-square error short-time spectral amplitude estimator](https://doi.org/10.1109/TASSP.1984.1164453), IEEE Transactions on Acoustics, Speech, and Signal Processing, 1984: the source of the decision-directed method.
- B. Widrow and others, [Adaptive noise cancelling: Principles and applications](https://doi.org/10.1109/PROC.1975.10036), Proceedings of the IEEE, 1975.

**Going further**
- *Digital Audio Restoration* (Simon J. Godsill and Peter J. W. Rayner, book): click removal, interpolation and noise reduction with statistical models.
- *Speech Enhancement: Theory and Practice* (Philipos C. Loizou, book).
