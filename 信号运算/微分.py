import numpy as np
from matplotlib.pylab import mpl
from matplotlib import animation
from sympy import *
import matplotlib.pyplot as plt

mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
fig, ax = plt.subplots()
t = np.arange(-1, 1, 0.02)
g = t ** 2
t = symbols('t')
d = diff(g, t)

line, = ax.plot(t, g)
line1, = ax.plot(t, d)


def animate(i):
    line.set_ydata(np.sin(t ** 2 + i / 50))
    line1.set_ydata(diff(g, t + i / 50))
    return line, line1,


ani = animation.FuncAnimation(fig, animate, interval=20, blit=True, save_count=50)

plt.show()
