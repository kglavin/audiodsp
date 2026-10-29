Module 00: Audio Signals, Sampling and Quantization

Notebook:
- [sampling_and_quantization.ipynb](sampling_and_quantization.ipynb): sampling and sinc reconstruction, spectral images and aliasing, the ADC/DAC chain and the aperture effect, mid-tread and mid-riser quantizers, SQNR, and RPDF vs TPDF dither. Covers all three projects below.

Audio signal visualization in the time and frequency domains moved to `01_Discrete_Time_Signals_and_Systems` (waveforms) and `02_Frequency_Domain_Analysis` (spectra), because it relies on material taught there.

Here are some software mini projects that can be used to educate about the topic of Audio Signals and its sub-topics:

## Audio Sampling and Reconstruction:
 Create a software application that demonstrates the process of audio sampling and reconstruction based on the Nyquist-Shannon sampling theorem. Users can select an audio signal and adjust the sampling rate to observe the effects on the reconstructed signal. The application should show the original and reconstructed waveforms to illustrate the importance of sampling at a rate higher than the Nyquist frequency. This project will help students grasp the concepts of audio digitization, quantization, and the sampling theorem.

## Analog and Digital Audio Conversion:
 Build a software tool that allows users to convert audio signals between analog and digital representations. Users can input an analog signal through a microphone or generate a digital signal using a synthesizer. The application should provide options to apply analog-to-digital conversion or digital-to-analog conversion and visualize the resulting signals. This project will help students understand the differences between analog and digital representations of audio signals and the process of converting between the two.

## Audio Quantization Effects:
 Develop a software application that demonstrates the effects of audio quantization on signal quality. Users can input an audio signal and adjust the bit depth to observe the impact on signal fidelity and dynamic range. The application should provide visual and audible comparisons between the original and quantized signals to illustrate the effects of quantization error. This project will help students grasp the basic concepts of audio digitization, quantization, and the trade-off between signal resolution and quantization noise.
