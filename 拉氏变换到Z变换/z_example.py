# 正弦序列
from matplotlib import pyplot as plt
import numpy as np


def sin_z(x, z):
    '''
    :param x: 时间序列
    :param z: 频率序列
    :return:
    '''
    sin_z_values = []
    for zz in z:
        sin_z_values = 0
        for xx in x:
            sin_z_values += np.sin(np.pi * xx) * pow(zz, float(-xx))
        sin_z_values.append(sin_z_values)
    return sin_z_values


x = np.arange(0, 20, 1)
z = np.arange(0, 20, 0.1)
# x = np.arange(0, 20, 1)
sinZV = sin_z(x, z)
plt.subplot(223)
plt.plot(z, sinZV)
plt.show()