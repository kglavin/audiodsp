Module 05: Audio Effects

Notebook:
- [effects.ipynb](effects.ipynb): a three-band equalizer from Audio EQ Cookbook biquads, convolution reverb with a synthetic room impulse response and a measured reverb time, and saturation with oversampling. Covers the equalizer, reverberation, and saturation projects below.

Here are some software mini projects that can be used to educate about the topic of Audio Effects and its sub-topics:

## Equalizer Simulator:
 Develop a software tool that simulates an equalizer and allows users to manipulate the frequency response of an audio signal. Users can select different types of equalizers such as parametric, graphic, or shelving equalizers. The tool should provide control over the equalizer's parameters, such as center frequency, bandwidth, and gain. Users can input an audio signal and observe the effects of equalization on different frequency ranges. This project will help students understand the basic concepts of equalization and the different types of equalizers.

## Echo and Reverberation Effect Generator:
 Create a software application that generates echo and reverberation effects on audio signals. Users can input an audio file or generate simple audio sequences. The application should provide control over parameters such as delay time, feedback, and decay time to simulate echo and reverberation effects. Users can adjust these parameters and listen to the modified audio signal in real-time. This project will help students understand the principles of echo and reverberation effects and how they contribute to the sense of space and ambiance in audio.

## Pitch Shifter and Time Stretcher:
 Build a software tool that allows users to manipulate the pitch and duration of audio signals. Users can input an audio file or generate simple audio sequences. The tool should provide options to shift the pitch up or down and stretch or compress the duration of the audio signal. Users can adjust these parameters and observe the changes in the audio signal in real-time. This project will help students understand the concepts of pitch shifting and time stretching and their applications in music production and sound design.

## Audio Modulation Effect Generator:
 Develop a software application that generates audio modulation effects such as ring modulation, flanging, and chorus. Users can input an audio file or generate simple audio sequences. The application should provide control over modulation parameters such as modulation frequency, depth, and feedback. Users can adjust these parameters and listen to the modified audio signal in real-time. The application should also provide visualizations to help students understand the characteristics of each modulation effect. This project will help students explore different audio modulation techniques and their creative applications.

## Spatial Audio Processor:
 Create a software tool that simulates spatial audio processing techniques such as panning, surround sound, and binaural audio. Users can input an audio file or generate audio sequences. The tool should provide options to position audio sources in the stereo or surround sound field, adjust panning and balance, and apply binaural rendering for headphone listening. Users can adjust these parameters and listen to the modified audio signal, experiencing the spatial audio effects. This project will help students understand the principles of spatial audio processing and its applications in creating immersive audio experiences.

## Dynamics Processor:
 Build a compressor, limiter and expander. Users should control threshold, ratio, attack, release and makeup gain, and see the gain reduction over time alongside the input and output waveforms. The tool should show how fast attack and release times distort low-frequency waveforms, and how a limiter catches peaks. This project will help students understand dynamic range control, its use in music production and broadcasting, and the trade-offs between transparency and loudness.

## Saturation and Oversampling:
 Create a saturation effect based on a nonlinear curve such as tanh. Users should be able to vary the drive and the oversampling factor, and see and hear the harmonics it creates and the aliased components that fold back below the Nyquist frequency. The tool should measure the largest aliased component, so users can compare oversampling factors and downsampling filters. This project will help students understand why nonlinear effects alias and how oversampling controls it.

## Further reading

**Start here**
- Wikipedia: [Audio equalization](https://en.wikipedia.org/wiki/Equalization_(audio)), [Reverberation](https://en.wikipedia.org/wiki/Reverberation) and [Dynamic range compression](https://en.wikipedia.org/wiki/Dynamic_range_compression).

**Background**
- [Audio EQ Cookbook](https://www.w3.org/TR/audio-eq-cookbook/) (Robert Bristow-Johnson, W3C note): peaking and shelving filters.
- [Artificial Reverberation](https://ccrma.stanford.edu/~jos/pasp/Artificial_Reverberation.html), in *Physical Audio Signal Processing* (Julius O. Smith III, free online book).
- V. Välimäki, J. D. Parker, L. Savioja and others, [Fifty Years of Artificial Reverberation](https://doi.org/10.1109/TASL.2012.2189567), IEEE Transactions on Audio, Speech, and Language Processing, 2012.

**Going further**
- *DAFX: Digital Audio Effects* (Udo Zölzer, editor, book) and *Audio Effects: Theory, Implementation and Application* (Joshua D. Reiss and Andrew McPherson, book).
- [DAFx conference](https://www.dafx.de/): the yearly research conference on digital audio effects, with open paper archives.
