import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft

x = np.linspace(0, 1, 25)
y = np.sin(2 * np.pi * 1 * x) \
    + np.sin(2 * np.pi * 2 * x) + np.sin(2 * np.pi * 3 * x) + np.sin(2 * np.pi * 4 * x) \
    + np.sin(2 * np.pi * 5 * x) + np.sin(2 * np.pi * 6 * x) + np.sin(2 * np.pi * 7 * x) + np.sin(2 * np.pi * 8 * x) \
    + np.sin(2 * np.pi * 9 * x) + np.sin(2 * np.pi * 10 * x)

yy = fft(y)  # 快速傅里叶变换
yreal = yy.real  # 获取实数部分
yimag = yy.imag  # 获取虚数部分

yf = abs(fft(y))  # 取模
yf1 = abs(fft(y)) / (len(x) / 2)  # 归一化处理
yf2 = yf1[range(int(len(x) / 2))]  # 由于对称性，只取一半区间

xf = np.arange(len(y))  # 频率
xf1 = xf
xf2 = xf[range(int(len(x) / 2))]  # 取一半区间

plt.plot(xf, yf, 'r')
plt.title('FFT of Mixed wave)', fontsize=10, color='#F08080')

plt.show()


