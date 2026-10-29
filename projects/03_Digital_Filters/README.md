Module 03: Digital Filters

Notebooks, in order:
- [filter_design_foundations.ipynb](filter_design_foundations.ipynb): windowed-sinc FIR design, window trade-offs, spectral inversion, the z-transform, the bilinear transform and pre-warping.
- [digital_filters.ipynb](digital_filters.ipynb): an FIR/IIR design and analysis tool, block-based (real-time) filtering, a design method comparison, and poles, zeros and stability.
- [resampling.ipynb](resampling.ipynb): decimation, interpolation and polyphase rate conversion.

Here are some software mini projects that can be used to educate about the topic of Digital Filters and its sub-topics:

## Filter Design and Analysis Tool: Develop a software application that allows users to design and analyze digital filters. Users can choose between FIR and IIR filter types and specify filter characteristics such as cutoff frequency, filter order, and filter type (e.g., low-pass, high-pass, bandpass, etc.). The application should provide options to visualize the frequency response, impulse response, and phase response of the designed filter. Users can also input audio signals and observe the effect of the filter on the signal. This project will help understand the concepts of filter design, characteristics, and their impact on audio signals.

## Real-time Filter Implementation: Create a software tool that enables real-time implementation of digital filters on audio signals. Users can input audio files or generate audio sequences. The tool should provide options to select filter parameters such as filter type, cutoff frequency, and order. Users can observe the real-time filtering effect on the audio signal, and the tool should display the filtered waveform and its frequency response. This project will help understand the practical implementation of digital filters and how they can shape the frequency content of audio signals.

## Filter Design Comparison: Build a software application that allows users to compare different filter design methods and their characteristics. Users can select a filter design method such as windowing, frequency sampling, or optimization techniques. The application should generate and display the frequency response, impulse response, and phase response of filters designed using different methods. Users can observe the trade-offs in terms of filter performance, complexity, and filter length. This project will help understand the design considerations and trade-offs involved in creating digital filters.

## Filter Visualization and Analysis: Develop a software tool that visualizes the frequency response, impulse response, and phase response of digital filters. Users can input filter coefficients or design parameters, and the tool should display the corresponding filter characteristics. Users can interactively adjust filter parameters and observe the changes in filter response in real-time. The tool can also provide analysis features such as magnitude and phase plots, filter stability checks, and pole-zero diagrams. This project will help explore the filter characteristics and gain insights into how different filter designs affect the frequency and temporal response of audio signals.

## Windowed-Sinc FIR Designer:
 Build a tool that designs FIR filters from first principles: compute the ideal sinc impulse response, truncate it, and taper it with a selectable window. Users should see the taps and the magnitude response side by side, measure stopband attenuation and transition width for each window, and turn a low-pass into a high-pass by spectral inversion. This project will help understand what library functions such as `firwin` do, and why windows trade stopband attenuation against transition width.

## Bilinear Transform Explorer:
 Create a tool that converts analog filter prototypes into digital biquads with the bilinear transform. Users should be able to switch pre-warping on and off and watch where the center or cutoff frequency lands, especially close to the Nyquist frequency. This project will help understand frequency warping and how classic analog filter designs become digital IIR filters.

## Sample-Rate Converter:
 Develop a converter between common sample rates such as 44.1 kHz and 48 kHz. Users should be able to compare naive decimation with filtered decimation, see the images created by zero-stuffing, and measure how the converter treats tones near the Nyquist frequency. This project will help understand anti-aliasing and anti-imaging filters and polyphase implementation.
