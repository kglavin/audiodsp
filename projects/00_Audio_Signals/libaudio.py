import math
import wave
import pyaudio
import struct

def simple_sine(frequency,filename='sine.wav', duration=1, sample_rate=44100) -> int:

    # Calculate the number of frames
    num_frames = int(sample_rate * duration)

    # Generate the mixed sine wave data
    data = []
    for i in range(num_frames):
        # add the samples but divide by number of freqs to keep value in range ( short )
        sample = math.sin(2 * math.pi * frequency * i / sample_rate)
        data.append(sample)

    # Configure the wave file
    wave_file = wave.open(filename, "w")
    wave_file.setnchannels(1)  # Mono audio
    wave_file.setsampwidth(2)  # 2 bytes per sample
    wave_file.setframerate(sample_rate)  # Sample rate
    wave_file.setcomptype("NONE", "Uncompressed")

    # Write the audio data to the file
    wave_file.writeframes(b"".join([struct.pack("<h", int(sample * 32767)) for sample in data]))
    wave_file.close()
    return num_frames

def multi_sine(frequencies=[300,2000],filename='sine.wav', duration=1, sample_rate=44100) -> int: 

    # Calculate the number of frames
    num_frames = int(sample_rate * duration)

    # Generate the mixed sine wave data
    data = []
    for i in range(num_frames):
        # add the samples but divide by number of freqs to keep value in range ( short )
        sample = sum(math.sin(2 * math.pi * frequency * i / sample_rate) for frequency in frequencies)/len(frequencies)
        data.append(sample)

    # Configure the wave file
    wave_file = wave.open(filename, "w")
    wave_file.setnchannels(1)  # Mono audio
    wave_file.setsampwidth(2)  # 2 bytes per sample
    wave_file.setframerate(sample_rate)  # Sample rate
    wave_file.setcomptype("NONE", "Uncompressed")

    # Write the audio data to the file
    wave_file.writeframes(b"".join([struct.pack("<h", int(sample * 32767)) for sample in data]))
    wave_file.close()
    return num_frames
