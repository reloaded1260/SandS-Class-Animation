import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

fig, ax = plt.subplots()
f = 10
t = np.arange(0, 1, 0.01)
y = np.sin(2 * np.pi * f * t + 0.3)  # 振幅amp = 1;频率f = 10hz;相位 = 0.3;原始信号0.01s采样，0.1s采样
line, = ax.plot(t, y)
t1 = np.arange(0, 1, 0.1)  # 10s采样
y1 = np.sin(2 * np.pi * f * t1 + 0.3)
line1, = ax.plot(t, y)
line1, = ax.plot(t1, y1, 'ro')
line2, = ax.plot(t1, y1, 'r')
plt.ylim(-1, 1)


def animate(i):
    line.set_ydata(np.sin(2 * np.pi * t + i / 50))
    line1.set_ydata(np.cos(2 * np.pi * t1 * f + i / 50))
    return line, line1


plt.show()
