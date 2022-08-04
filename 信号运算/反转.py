import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
from matplotlib.pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

fig, ax = plt.subplots()

t = np.arange(0, 2, 0.001)
y = np.sin(2 * np.pi * t)
y2 = np.sin(-2 * np.pi * t)
line, = ax.plot(t, y)
line1, = ax.plot(t, y2)


def animate(i):
    line.set_ydata(np.sin(2 * np.pi * (t + i / 50)))
    line1.set_ydata(np.sin(-2 * np.pi * (t + i / 50)))
    return line, line1,


ani = animation.FuncAnimation(fig, animate, interval=20, blit=True, save_count=50)

plt.show()
