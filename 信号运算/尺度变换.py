import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
from matplotlib.pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
fig = plt.figure()
ax1 = plt.subplot(3, 1, 1)
ax2 = plt.subplot(3, 1, 2)
ax3 = plt.subplot(3, 1, 3)
t = np.arange(0, 2, 0.001)
a = 2
y = np.sin(2 * np.pi * t)
y1 = np.sin(2 * a * np.pi * t)
y2 = np.sin(2 * np.pi * t / a)
line, = ax1.plot(t, y)
line1, = ax2.plot(t, y1)
line2, = ax3.plot(t, y2)


def animate(i):
    line.set_ydata(np.sin(2 * np.pi * t + i / 50))
    line1.set_ydata(np.cos(2 * a * np.pi * t + i / 50))
    line2.set_ydata(np.cos(2 * np.pi * t / a + i / 50))
    return line, line1, line2


ani = animation.FuncAnimation(fig, animate, interval=20, blit=True, save_count=50)

plt.show()
