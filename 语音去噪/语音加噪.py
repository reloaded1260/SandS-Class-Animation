import librosa
import numpy as np
import soundfile as sf


def add_noise(data):
    wn = np.random.normal(0, 2, len(data))
    data_noise = np.where(data != 0.0, data.astype('float64') + 0.02 * wn, 0.0).astype(np.float32)
    return data_noise


data, fs = librosa.core.load('C:/Users/Administrator/AppData/Local/Programs/Python/蓝色多瑙河.wav')
data_noise = add_noise(data)
sf.write('noised.wav', data_noise, fs)
# librosa.output.write_wav('audio1.wav', data_noise, fs)
