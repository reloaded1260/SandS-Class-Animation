import matplotlib.pyplot as plt
import numpy as np

# r = 1
from matplotlib import animation

t = np.linspace(0, 2 * np.pi, 200)
y = np.sin(t)
y1 = np.sin(t) + np.sin(3 * t) / 3
y2 = np.sin(t) + np.sin(3 * t) / 3 + np.sin(5 * t) / 5
y3 = np.sin(t) + np.sin(3 * t) / 3 + np.sin(5 * t) / 5 + np.sin(7 * t) / 7
y4 = np.sin(t) + np.sin(3 * t) / 3 + np.sin(5 * t) / 5 + np.sin(7 * t) / 7 + np.sin(9 * t) / 9

fig = plt.figure()
ax1 = plt.subplot(5, 1, 1)
line1, = ax1.plot(t, y)
ax2 = plt.subplot(5, 1, 2)
line2, = ax2.plot(t, y1)
ax3 = plt.subplot(5, 1, 3)
line3, = ax3.plot(t, y2)
ax4 = plt.subplot(514)
# ax4.set_ylim([-2, 2])
line4, = ax4.plot(t, y3)
ax5 = plt.subplot(5, 1, 5)
# ax5.set_ylim([-2, 2])
line5, = ax5.plot(t, y4)


def update(i):
    line1.set_ydata(np.sin(t + i / 50))
    line2.set_ydata(np.sin(t + i / 50) + np.sin(3 * (t + i / 50)) / 3)
    line3.set_ydata(np.sin(t + i / 50) + np.sin(3 * (t + i / 50)) / 3 + np.sin(5 * (t + i / 50)) / 5)
    line4.set_ydata(np.sin(t + i / 50) + np.sin(3 * (t + i / 50)) / 3 + np.sin(5 * (t + i / 50)) / 5 + np.sin(
        7 * (t + i / 50)) / 7)
    line5.set_ydata(np.sin(t + i / 50) + np.sin(3 * (t + i / 50)) / 3 + np.sin(5 * (t + i / 50)) / 5 + np.sin(
        7 * (t + i / 50)) / 7 + np.sin(9 * (t + i / 50)) / 9)
    return line1, line2, line3, line4, line5


ani = animation.FuncAnimation(
    fig, update, interval=20, blit=True, save_count=50)

plt.show()
