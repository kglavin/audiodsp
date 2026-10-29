Module 06: Psychoacoustics and Audio Coding

Psychoacoustics is taught here, at the start of the coding module, because perceptual coding depends on it.

Notebook:
- [psychoacoustics_and_coding.ipynb](psychoacoustics_and_coding.ipynb): threshold of hearing and critical bands, a masking model with a listening test, mu-law companding, a FLAC-style lossless coder (prediction and Rice coding), and a small MDCT perceptual coder compared with a coder that ignores hearing. Real MP3/AAC/FLAC encoders are not used, because they need external programs.

Here are some software mini projects that can be used to educate about the topic of Psychoacoustics and Audio Coding and its sub-topics:

## Hearing and Masking Explorer:
 Build a tool that demonstrates the basic properties of hearing that audio coding relies on. Users should be able to play tones across the audible range at controlled levels, compare them with equal-loudness contours, and hear masking: a quiet tone close in frequency to a loud one becomes inaudible, while the same quiet tone further away stays audible. The tool should display critical bands on the Bark scale. This project will help understand why the ear ignores some parts of a signal, which lossy codecs exploit.

## Compression Ratio Comparison:
 Create a software tool that allows users to compare the compression ratios achieved by different audio compression algorithms. Users can input audio files of varying lengths and complexities. The tool should apply different compression algorithms, such as lossless and lossy compression, and display the resulting file sizes. Users can observe and analyze the trade-offs between compression ratio and audio quality for each algorithm. This project will help understand the principles of audio coding and compression, as well as the differences between lossless and lossy compression algorithms.

## Audio Codec Player:
 Develop a software application that supports different audio codecs, such as MP3, AAC, and FLAC, and allows users to compare their performance and audio quality. Users can input audio files and select different codecs to encode and decode the audio. The application should provide options to adjust encoding settings, such as bit rate or compression level. Users can listen to the encoded audio and compare the perceptual quality between different codecs. This project will help understand the characteristics and trade-offs of popular audio codecs and the impact of compression settings on audio quality.

## Psychoacoustic Model Analysis:
 Create a software tool that analyzes and visualizes psychoacoustic models and their impact on audio coding and compression. Users can input audio files and observe the psychoacoustic model's analysis results, such as auditory masking thresholds or critical bands. The tool should provide visualizations to help students understand how the psychoacoustic model influences the allocation of bits for different audio components. Users can also compare the original and compressed audio files to observe the perceptual coding effects. This project will help explore the principles of perceptual coding and its role in achieving efficient audio compression.

## Lossless Compression Demonstration:
 Build a software tool that demonstrates the principles and effectiveness of lossless compression algorithms on audio signals. Users can input audio files or generate audio sequences. The tool should apply lossless compression algorithms, such as Huffman coding or Lempel-Ziv-Welch (LZW) algorithm, and display the resulting compressed file size. Users can also observe and analyze the compression and decompression processes step by step. This project will help understand the concepts of lossless compression, entropy coding, and the preservation of audio fidelity in lossless compression algorithms.
