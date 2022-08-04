from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax1)  # plt.axes(projection='3d')
theta = np.linspace(-2 * np.pi, 2 * np.pi, 100)
x = np.linspace(0, 500, 100)
# x = np.sin(theta)
x1 = np.linspace(0, 2, 100)
y = np.cos(theta)
y1 = y * x1
z = np.sin(theta)
z1 = z * x1
line1, = ax1.plot3D(x, y, z, label="FT")
line2, = ax1.plot3D(x, y, z, 'ro',label="DTFT")
line3, = ax1.plot3D(x, y1, z1,label="LT")
line4, = ax1.plot3D(x, y1, z1, 'bo',label="ZT")


def update(i):
    line1.set_xdata(x[:i + 1])
    line1.set_ydata(y[:i + 1])
    line1.set_3d_properties(z[:i + 1])
    line2.set_xdata(x[:i + 1])
    line2.set_ydata(y[:i + 1])
    line2.set_3d_properties(z[:i + 1])
    line3.set_xdata(x[:i + 1])
    line3.set_ydata(y1[:i + 1])
    line3.set_3d_properties(z1[:i + 1])
    line4.set_xdata(x[:i + 1])
    line4.set_ydata(y1[:i + 1])
    line4.set_3d_properties(z1[:i + 1])
    return line1, line2, line3, line4,


# 图像配置
ax1.get_proj = lambda: np.dot(Axes3D.get_proj(ax1), np.diag([0.8, 1, 0.5, 1]))
ax1.grid(False)  # 隐藏网格线
ax1.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax1.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax1.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax1.view_init(32, -32)  # 坐标轴转向
ax1.legend()

ani = animation.FuncAnimation(
    fig=fig, func=update, frames=100, interval=20, blit=True, repeat=True)
plt.show()

# list1 = [1, 2, 3]
# list2 = [3, 4, 5]
# list3 = []
# for i in range(0, len(list1)):
#     t = list1[i] * list2[i]
#     list3.insert(i, t)
# print('list3=', list3)
