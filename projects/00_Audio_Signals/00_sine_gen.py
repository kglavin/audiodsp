import math
import wave
import pyaudio

# Audio settings
sample_rate = 44100  # Number of samples per second
duration = 5  # Duration in seconds

# Frequencies
#frequencies = [100, 300, 900, 2200]
frequencies = [ 900]

# Calculate the number of frames
num_frames = int(sample_rate * duration)

# Generate the mixed sine wave data
data = []
for i in range(num_frames):
    sample = sum(math.sin(2 * math.pi * freq * i / sample_rate) for freq in frequencies)
    data.append(sample)

# Configure the wave file
wave_file = wave.open("mixed_sine_wave.wav", "w")
wave_file.setnchannels(1)  # Mono audio
wave_file.setsampwidth(2)  # 2 bytes per sample
wave_file.setframerate(sample_rate)  # Sample rate
wave_file.setcomptype("NONE", "Uncompressed")

# Write the audio data to the file
wave_file.writeframes(b"".join([wave_file.struct.pack("<h", int(sample * 32767)) for sample in data]))
wave_file.close()

# Play the generated audio sample
p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wave_file.getsampwidth()),
                channels=wave_file.getnchannels(),
                rate=wave_file.getframerate(),
                output=True)

wave_file.open("mixed_sine_wave.wav", "rb")
data = wave_file.readframes(num_frames)

stream.write(data)
stream.stop_stream()
stream.close()

p.terminate()

print("Audio sample generated and played.")

