Module 04: Real-time Audio Processing

This module comes before effects, restoration and synthesis because they all run in real time in practice. It builds on section 2 of `03_Digital_Filters/digital_filters.ipynb`, which filters audio block by block and carries filter state between blocks.

Notebook:
- [realtime_processing.ipynb](realtime_processing.ipynb): the callback model and latency, stateful block processors (filter, feedback delay, gain smoothing), deadlines and dropouts on a simulated audio device, ring buffers and jitter buffers for streaming, partitioned convolution reverb, a phase-continuous synthesizer voice, and an optional live-audio cell using `sounddevice`. Covers all four projects below.

Here are some software mini projects that can be used to educate about the topic of Real-time Audio Processing and its sub-topics:

## Real-time Audio Effects Processor: Develop a software application that allows users to apply real-time audio effects to incoming audio streams. Users can select different audio effects, such as reverb, delay, or distortion, and adjust the effect parameters in real-time. The application should interface with audio interfaces or microphone inputs, process the audio data in real-time, and output the processed audio. This project will help understand the basics of real-time audio processing systems and the application of audio effects in real-time scenarios.

## Audio Streaming and Recording Tool: Create a software tool that demonstrates audio streaming and recording capabilities. Users can select an audio input device, such as a microphone or line-in, and stream the audio data in real-time to a destination, such as a file or network stream. The tool should provide options to adjust streaming parameters like sample rate, buffer size, and latency. Users can also record the audio stream and save it as a file. This project will help understand the concepts of audio interfaces, data streaming, and the challenges associated with real-time audio processing.

## Buffering and Latency Analyzer: Build a software application that visualizes buffering and latency in real-time audio processing systems. Users can generate audio signals or input audio files and observe the buffering and latency effects. The application should display visualizations and metrics to help understand the buffer size, buffer fill level, and latency introduced by the processing system. Users can adjust the buffer size and observe the impact on audio quality and latency. This project will help grasp the importance of buffering and latency management in real-time audio processing.

## Real-time Audio Synthesizer: Develop a software tool that enables real-time audio synthesis using software or hardware platforms. Users can generate audio signals or play MIDI input and observe the synthesized audio output in real-time. The tool should provide options for adjusting synthesis parameters such as oscillator types, waveforms, envelopes, and effects. Users can also experiment with different software or hardware platforms for real-time audio synthesis. This project will help understand the software and hardware platforms used for real-time audio processing and gain practical experience in real-time audio synthesis.

## Further reading

**Start here**
- [Real-time audio programming 101: time waits for nothing](http://www.rossbencina.com/code/real-time-audio-programming-101-time-waits-for-nothing) (Ross Bencina): why audio callbacks must avoid locks, allocation and I/O.

**Background**
- [python-sounddevice](https://python-sounddevice.readthedocs.io/) documentation, used in the notebook's live-audio cell, and the [PortAudio](https://www.portaudio.com/) library underneath it.

**Going further**
- [JUCE tutorials](https://juce.com/learn/tutorials/): the C++ framework most audio plug-ins and applications are built with.
- W. G. Gardner, "Efficient Convolution without Input-Output Delay", Journal of the Audio Engineering Society, 1995: non-uniformly partitioned convolution for zero-latency reverb.
