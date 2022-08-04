from scipy.io import wavfile
import noisereduce as nr
import pyaudio
import time
import wave

rate, data = wavfile.read("001.wav")
_, noisy_part = wavfile.read("noise.wav")
SAMPLING_FREQUENCY = 16000
reduced_noise = nr.reduce_noise(y=data, y_noise=noisy_part, sr=SAMPLING_FREQUENCY)

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = time
WAVE_OUTPUT_FILENAME = "out_file.wav"

with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(2)
    wf.setframerate(RATE)
    wf.writeframes(b''.join(reduced_noise))

# https://blog.csdn.net/qq_38641985/article/details/121403164
