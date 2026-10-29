Module 08: Audio Synthesis and Sound Design

Notebook:
- [synthesis.ipynb](synthesis.ipynb): aliasing in naive, PolyBLEP and additive oscillators, ADSR envelopes, additive, subtractive (state-variable filter) and FM synthesis, the Karplus-Strong string with all-pass tuning, granular time stretching and pitch shifting, and drum sound design. Covers all four projects below.

Here are some software mini projects that can be used to educate about the topic of Audio Synthesis and Sound Design and its sub-topics:

## Synthesizer Simulator: Develop a software tool that simulates a synthesizer and allows users to explore different audio synthesis techniques. Users can experiment with additive, subtractive, and granular synthesis methods. The tool should provide controls for adjusting parameters such as oscillator types, waveforms, envelope shapes, and filter characteristics. Users can play with these parameters in real-time and listen to the resulting synthesized sounds. This project will help understand the basics of audio synthesis techniques and their application in sound design.

## Physical Modeling Synthesis Engine: Create a software application that implements physical modeling synthesis techniques. Users can interact with virtual instruments that emulate real-world acoustic instruments such as guitars, pianos, or drums. The application should provide options to adjust parameters that affect the instrument's characteristics, such as string tension, body size, or resonator properties. Users can play the virtual instruments and observe how the physical modeling synthesis engine generates realistic sounds based on the underlying physics models. This project will help understand the principles of physical modeling synthesis and its application in creating realistic instrument sounds.

## Sound Effects Design Tool: Build a software tool that focuses on sound design principles for creating virtual instruments and sound effects. Users can input audio files or generate simple audio signals. The tool should provide options to apply various sound design techniques, such as layering, modulation, filtering, and effects processing. Users can experiment with these techniques, adjust parameters, and listen to the modified sounds in real-time. The tool can also include visualization features to help understand the changes in the spectral content and dynamics of the sounds. This project will help explore the creative aspects of sound design and gain practical experience in designing virtual instruments and sound effects.

## Granular Synthesis Generator: Develop a software application that generates sounds using granular synthesis techniques. Users can input audio files or generate audio sequences. The application should provide controls for adjusting parameters such as grain size, density, pitch, and spatialization. Users can experiment with these parameters and listen to the resulting granulated sounds. The application should also provide visualizations to help understand the relationship between the input audio and the granular synthesis output. This project will help understand the principles of granular synthesis and its creative applications in sound design and audio synthesis.

## Further reading

**Start here**
- [Learning Synths](https://learningsynths.ableton.com/) (Ableton): an interactive, in-browser introduction to synthesizers.
- [Synth Secrets](https://www.soundonsound.com/series/synth-secrets-sound-sound) (Gordon Reid, Sound On Sound): a long-running article series on how synthesizers create sound.

**Background**
- [The Theory and Technique of Electronic Music](http://msp.ucsd.edu/techniques.htm) (Miller Puckette, free online book): oscillators, modulation, filters and sampling.
- [The Karplus-Strong Algorithm](https://ccrma.stanford.edu/~jos/pasp/Karplus_Strong_Algorithm.html), in *Physical Audio Signal Processing* (Julius O. Smith III, free online book).
- [Linear trapezoidal integrated state variable filter](https://cytomic.com/files/dsp/SvfLinearTrapOptimised2.pdf) (Andrew Simper, Cytomic, PDF): the SVF used in the subtractive synthesis section.

**Going further**
- V. Välimäki and A. Huovilainen, [Antialiasing Oscillators in Subtractive Synthesis](https://doi.org/10.1109/MSP.2007.323276), IEEE Signal Processing Magazine, 2007.
- K. Karplus and A. Strong, [Digital Synthesis of Plucked-String and Drum Timbres](https://doi.org/10.2307/3680062), Computer Music Journal, 1983.
- *Microsound* (Curtis Roads, book): granular synthesis in depth.
