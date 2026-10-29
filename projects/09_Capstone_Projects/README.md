Module 09: Capstone Projects

Each capstone combines several earlier modules into a complete application. The modules each one draws on are listed with it.

Notebook:
- [capstones.ipynb](capstones.ipynb): compact versions of all five, each measured against a known ground truth: a McLeod pitch tuner, a spectral-flux beat tracker, a speech front end (VAD, noise reduction, MFCCs), a telephone channel with echo cancellation and double-talk detection, and a moving source rendered for headphones. They run offline, frame by frame or block by block; live input would use the approach of `04_Real_time_Audio_Processing` section 7.

## Instrument Tuner:
 Build a tuner that listens to a microphone and shows the pitch of a played note and how far it is from the nearest equal-tempered note, in cents. Estimate pitch with autocorrelation or zero crossings, and check it against an FFT peak. Smooth the display so it does not jitter. Uses modules 01 (time-domain frequency measurement), 02 (FFT), 03 (filtering out hum and noise) and 04 (real-time input).

## Beat and Tempo Tracker:
 Develop a tool that finds the beats in a music recording and estimates its tempo in beats per minute. Compute an onset strength signal from frame-to-frame increases in spectral energy (spectral flux), then find its dominant periodicity with autocorrelation. Mark the detected beats on the waveform and play them back as clicks over the music. Uses modules 01 (envelopes, autocorrelation), 02 (STFT) and 03 (smoothing filters).

## Speech Front End:
 Build the signal-processing front end of a speech recognizer: voice activity detection, noise reduction, pre-emphasis, and mel-frequency features computed from the STFT. Show how each stage changes the features for clean and noisy speech. Optionally, feed the features into an off-the-shelf speech recognition model and compare accuracy with and without noise reduction. Uses modules 02 (STFT), 03 (filters), 06 (mel scale and critical bands) and 07 (noise reduction).

## Telephone Channel Simulator:
 Develop a tool that passes audio through a simulated telephone channel: band-limit to 300-3400 Hz, resample to 8 kHz, compress with mu-law companding, add line noise and echo, then cancel the echo with an adaptive filter and reduce the noise at the receiver. Let users switch each stage on and off and listen to the result. Uses modules 03 (filters, resampling), 05 (echo), 06 (coding) and 07 (adaptive filtering, noise reduction).

## Game Audio Scene:
 Create an interactive audio scene in which sound sources move around a listener. Position each source with panning or binaural rendering, add distance-dependent level and filtering, place the scene in a room with convolution reverb, and run it all in real time. Uses modules 03 (filters), 04 (real-time processing), 05 (spatial audio, reverb) and 08 (synthesized sound sources).
