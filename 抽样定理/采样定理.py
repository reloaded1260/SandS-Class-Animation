import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()  # 建立一个画板
ax = fig.add_subplot(1, 1, 1)

x = np.linspace(0, 1, 500)
xdata = np.linspace(0, 1, 21)
ydata = np.cos(80 * np.pi * xdata)
sample, = ax.plot([], [], 'o')

line1, = ax.plot(x, np.cos(80 * np.pi * x), 'r--', lw=0.5)

ax.grid()

ax.set_xlim(0, 1)


def run(data):
    xdata = np.linspace(0, 1, data)
    ydata = np.cos(80 * np.pi * xdata)
    if data <= 81:
        sample.set_data(xdata, ydata)
        sample.set_color('r')
    else:
        sample.set_data(xdata, ydata)
        sample.set_color('k')
    return sample,


ani = animation.FuncAnimation(fig, run, frames=np.arange(41, 162, 2), blit=False, interval=600, repeat=True)

plt.show()
