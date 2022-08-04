import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)  # plt.axes(projection='3d')
x11 = np.zeros(100)
y11 = np.linspace(1, 10, 10)
x12 = np.linspace(0, 2 * np.pi, 100, endpoint=False)
y12 = np.linspace(-100 / 2, 100 / 2 - 1, 100)

j = 0
while j < 10:
    z11 = abs(np.fft.fftshift(abs(np.fft.fft(np.sin(x12 * y11[j])))))
    ax.plot3D(x11, y12 + y11[j], z11)
    j += 1

plt.show()

# N = 100
# fs = 1
# n = np.linspace(0, 2 * np.pi, 100, endpoint=False)
# x = np.sin(n)
#
# xf_abs = np.fft.fft-shift(abs(np.fft.fft(x)))
# axis_xf = np.linspace(-N / 2, N / 2 - 1, num=N)
# plt.plot(axis_xf, xf_abs)
# plt.show()