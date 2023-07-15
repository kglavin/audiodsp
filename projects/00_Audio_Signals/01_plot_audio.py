import wave
import numpy as np
import matplotlib.pyplot as plt

# Open the audio file
wave_file = wave.open("mixed_sine_wave.wav", "rb")

# Get the audio file parameters
num_channels = wave_file.getnchannels()
sample_width = wave_file.getsampwidth()
sample_rate = wave_file.getframerate()
num_frames = wave_file.getnframes()

# Read the audio data
audio_data = wave_file.readframes(num_frames)

# Convert the audio data to a NumPy array
if sample_width == 2:
    audio_data = np.frombuffer(audio_data, dtype=np.int16)
elif sample_width == 4:
    audio_data = np.frombuffer(audio_data, dtype=np.int32)

# Normalize the audio data (optional)
audio_data = audio_data / np.max(np.abs(audio_data))

# Close the audio file
wave_file.close()

# Calculate the time axis
duration = num_frames / sample_rate
time = np.linspace(0, duration, num=num_frames)

# Plot the audio waveform
plt.plot(time, audio_data)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Audio Waveform")
plt.grid(True)
plt.show()

