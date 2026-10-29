Module 01: Discrete-Time Signals and LTI Systems

Notebook:
- [signals_and_systems.ipynb](signals_and_systems.ipynb): waveform visualization, frequency and phase measured in the time domain, sequences, LTI properties, convolution and difference equations. Covers all five projects below.

Here are some software mini projects that can be used to educate about the topic of Discrete-Time Signals and LTI Systems and its sub-topics:

## Waveform Visualization:
 Create a software tool that allows users to visualize and analyze audio waveforms in the time domain. Users can input an audio file or generate simple audio signals of different frequencies and amplitudes. The tool should display the waveform graphically, with options to zoom in and out, adjust the time scale, and observe the changes in amplitude and duration. This project will help students understand the time-domain representation of audio signals and how changes in amplitude and duration affect the waveform.

## Frequency and Phase Analysis:
 Develop a software application that measures the frequency and phase of audio signals directly from the waveform, without a Fourier transform. Users can input an audio file or generate audio signals of different frequencies. The application should estimate frequency over time from the spacing of zero crossings, and measure the phase difference between two signals from the lag that maximizes their cross-correlation. This project will help students explore the concepts of amplitude, frequency, and phase in the time domain representation of audio signals. Spectrum-based analysis follows in `02_Frequency_Domain_Analysis`.

## Continuous and Discrete-Time Signals:
 Create a software tool that illustrates the differences between continuous-time and discrete-time signals. Users can input an audio signal and observe its continuous-time representation on a waveform graph. The tool should also allow users to sample the continuous-time signal and visualize the resulting discrete-time representation using sequences of samples. This project will help students understand the distinction between continuous and discrete-time signals and the process of converting from one to the other through sampling.

## Discrete-Time Signal Processing:
 Build a software application that demonstrates the basics of discrete-time signal processing using sequences of audio samples. Users can input an audio signal or generate simple audio sequences. The application should provide options to perform operations such as time shifting, amplitude scaling, and convolution on the input signal and visualize the resulting output signal. This project will help students understand how discrete-time signals are manipulated and processed in the time domain.

## LTI System Explorer:
 Build a software tool that tests whether a system is linear and time-invariant. Users can choose from systems such as a moving average, an echo, a distortion curve or a tremolo, or define their own. The tool should apply the superposition and time-shift tests to random inputs, report which properties hold, and show the impulse response of LTI systems. It should also run difference equations such as y[n] = x[n] + a y[n-1] and show how the feedback coefficient decides whether the impulse response decays or grows. This project will help students understand why LTI systems are described completely by their impulse response, and prepares the ground for IIR filters.

