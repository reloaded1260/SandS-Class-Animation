import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl
from matplotlib import animation

mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

fig, ax = plt.subplots()

t = np.arange(0, 2, 0.0001)
f = np.sin(2 * np.pi * t)
f1 = np.sin(2 * np.pi * (t - 0.2))
line, = ax.plot(t, f, linestyle='-')
line1, = ax.plot(t, f1, linestyle='-')


def animate(i):
    line.set_ydata(np.sin(2 * np.pi * t + i / 50))
    line1.set_ydata(np.cos(2 * np.pi * (t - 0.2) + i / 50))
    return line, line1


ani = animation.FuncAnimation(fig, animate, interval=20, blit=True, save_count=50)

plt.show()