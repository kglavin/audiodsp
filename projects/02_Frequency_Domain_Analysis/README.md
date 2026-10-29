Module 02: Frequency-Domain Analysis

Notebooks, in order:
- [frequency_domain.ipynb](frequency_domain.ipynb): Fourier series, Fourier transform and windowing, DFT, FFT, and the short-time Fourier transform (STFT).
- [spectral_analysis_examples.ipynb](spectral_analysis_examples.ipynb): the tools above applied to chords, harmonics, beats, noise, sweeps and your own WAV files.

Here are some software mini projects that can be used to educate about the topic of Frequency Domain Analysis and its sub-topics:

## Fourier Series Visualization:
 Develop a software tool that allows users to visualize and understand the Fourier series representation of periodic signals. Users can input a periodic signal or select from predefined signals with different waveforms and frequencies. The tool should display the original periodic signal in the time domain and its corresponding Fourier series representation in the frequency domain. Users should have control over the number of harmonics used in the Fourier series expansion to observe how the reconstructed signal evolves. This project will help comprehend the concept of representing periodic signals using a sum of sinusoidal components.

## Fourier Transform Spectrum Analysis:
 Create a software application that enables users to perform Fourier transform spectrum analysis on audio signals. Users can input an audio file or generate simple audio signals of different frequencies and amplitudes. The application should provide options to compute and display the magnitude and phase spectra of the signal using the Fourier transform. Users should be able to adjust the frequency resolution and observe the spectral content of the signal in real-time. This project will help explore the properties of the Fourier transform and understand how it reveals the frequency components of a signal.

## Discrete Fourier Transform (DFT) Implementation:
 Build a software tool that allows users to perform the Discrete Fourier Transform (DFT) on audio signals. Users can input an audio file or generate audio sequences. The tool should compute and display the magnitude and phase spectra of the signal using the DFT algorithm. Users should have control over the DFT parameters such as the window size and overlap, and be able to observe the spectral content of the signal. This project will help understand the applications of the DFT in analyzing and visualizing the frequency components of discrete-time signals.

## Fast Fourier Transform (FFT) Visualization:
 Develop a software application that demonstrates the Fast Fourier Transform (FFT) algorithm and its efficiency compared to the DFT. Users can input an audio signal or generate audio sequences. The application should compute and display the magnitude and phase spectra using both the FFT and DFT algorithms. Users should be able to compare the computation time and observe the similarity of the results between the two algorithms. This project will help understand the advantages of the FFT algorithm and its wide application in efficient spectral analysis.

## Short-Time Fourier Transform and Spectrograms:
 Build a software tool that computes the STFT of an audio signal and displays it as a spectrogram. Users should control the frame length, hop size and window, and see the trade-off between time and frequency resolution. The tool should invert the STFT by overlap-add, verify that the reconstruction is exact when the windows meet the constant overlap-add (COLA) condition, and allow simple processing between the two steps, such as zeroing or scaling bins. This project will help understand the representation that most spectral audio processing is built on.

## Audio Signal Visualization:
 Develop a software tool that allows users to visualize audio signals in the time and frequency domains. Users can input an audio file or generate audio signals of different frequencies and amplitudes. The tool should display the waveform of the audio signal in the time domain and provide a spectrogram or frequency spectrum representation in the frequency domain. This project will help students understand the characteristics of audio signals, such as amplitude, frequency, and phase, and how they are represented in different domains.
