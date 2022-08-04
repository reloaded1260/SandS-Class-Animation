import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

fig = plt.figure()
ax1 = plt.subplot(3, 1, 1)
ax2 = plt.subplot(3, 1, 2)
ax3 = plt.subplot(3, 1, 3)

f = 10
t = np.arange(0, 1, 0.01)
y = np.sin(2 * np.pi * f * t + 0.3)
t1 = np.arange(0, 1, 0.1)  # 10s采样
y1 = np.sin(2 * np.pi * f * t1 + 0.3)
line, = ax1.plot(t, y)
line1, = ax2.plot(t, y)
line2, = ax2.plot(t1, y1, 'ro')
line3, = ax3.plot(t1, y1, 'r')


def update(i):
    line.set_ydata(np.sin(2 * np.pi * f * (t + i / 100) + 0.3))
    line1.set_ydata(np.sin(2 * np.pi * f * (t + i / 100) + 0.3))
    line2.set_ydata(np.sin(2 * np.pi * f * (t1 + i / 100) + 0.3))
    line3.set_ydata(np.sin(2 * np.pi * f * (t1 + i / 100) + 0.3))
    return line, line1, line2, line3


ani = animation.FuncAnimation(
    fig, update, interval=20, blit=True, save_count=100)

plt.show()

#https://blog.csdn.net/weixin_43948644/article/details/84938085