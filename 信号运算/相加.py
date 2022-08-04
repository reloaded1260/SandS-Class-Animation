import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig = plt.figure()
ax1 = plt.subplot(3, 1, 1)
ax2 = plt.subplot(3, 1, 2)
ax3 = plt.subplot(3, 1, 3)
x = np.arange(0, 10, 0.01)
line, = ax1.plot(x, np.sin(2 * np.pi * x), color="red")
line1, = ax2.plot(x, np.sin(2 * np.pi * x), color="blue")
line2, = ax3.plot(x, np.sin(2 * np.pi * x) + np.sin(2 * np.pi * x), color="green")


def update(i):
    line.set_ydata(np.cos(x + i / 50))
    line1.set_ydata(np.sin(x + i / 50))
    line2.set_ydata(np.sin(2 * np.pi * x + i / 50) + np.sin(2 * np.pi * x + i / 50))
    return line, line1, line2,


ani = animation.FuncAnimation(
    fig, update, interval=20, blit=True, save_count=50)

plt.show()
