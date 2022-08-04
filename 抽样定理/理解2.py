import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

fig = plt.figure()
ax1 = plt.subplot(2, 1, 1)
ax2 = plt.subplot(2, 1, 2)

t = np.arange(0, 1, 0.01)
t1 = np.arange(0, 1, 0.1)  # 10s采样
y = np.sin(2 * np.pi * 10 * t + 0.3)
y1 = np.sin(2 * np.pi * 3 * t1 + 0.3)
y2 = np.sin(2 * np.pi * 7 * t1 + 0.3)
y3 = np.sin(2 * np.pi * 13 * t1 + 0.3)
y4 = np.sin(2 * np.pi * 16 * t1 + 0.3)

line, = ax1.plot(t, y)
line1, = ax2.plot(t1, y1)
line2, = ax2.plot(t1, y2)
line3, = ax2.plot(t1, y3)
line4, = ax2.plot(t1, y4)


def update(i):
    line.set_ydata(np.sin(2 * np.pi * 10 * (t + i / 2000) + 0.3))
    line1.set_ydata(np.sin(2 * np.pi * 3 * (t1 + i / 2000) + 0.3))
    line2.set_ydata(np.sin(2 * np.pi * 7 * (t1 + i / 2000) + 0.3))
    line3.set_ydata(np.sin(2 * np.pi * 13 * (t1 + i / 2000) + 0.3))
    line4.set_ydata(np.sin(2 * np.pi * 16 * (t1 + i / 2000) + 0.3))
    return line, line1, line2, line3, line4


ani = animation.FuncAnimation(
    fig, update, interval=20, blit=True, save_count=2000)

plt.show()
