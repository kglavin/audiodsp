import math
import wave
import pyaudio
import struct
import libaudio

filename="sine300.wav"
num_frames = libaudio.simple_sine(frequency=300, name=filename,duration=duration, sample_rate=sample_rate)

# Play the generated audio sample
p = pyaudio.PyAudio()

wave_file = wave.open(filename, "r")
stream = p.open(format=p.get_format_from_width(wave_file.getsampwidth()),
                channels=wave_file.getnchannels(),
                rate=wave_file.getframerate(),
                output=True)

data = wave_file.readframes(num_frames)

stream.write(data)
stream.stop_stream()
stream.close()

p.terminate()

print("Audio sample generated and played.")

