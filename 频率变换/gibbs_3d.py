import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
fig = plt.figure()
ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)  # plt.axes(projection='3d')
x = np.linspace(-6, 6, 100)
y1 = np.linspace(1, 1, 100)
z1 = np.sin(1 * 2 * np.pi * x)
line1, = ax.plot3D(x, y1, z1)
y2 = np.linspace(2, 2, 100)
z2 = np.sin(2 * 2 * np.pi * x)
line2, = ax.plot3D(x, y2, z2)
y3 = np.linspace(3, 3, 100)
z3 = np.sin(3 * 2 * np.pi * x)
line3, = ax.plot3D(x, y3, z3)
y4 = np.linspace(4, 4, 100)
z4 = np.sin(4 * 2 * np.pi * x)
line4, = ax.plot3D(x, y4, z4)
y5 = np.linspace(5, 5, 100)
z5 = np.sin(5 * 2 * np.pi * x)
line5, = ax.plot3D(x, y5, z5)
y6 = np.linspace(6, 6, 100)
z6 = np.sin(6 * 2 * np.pi * x)
line6, = ax.plot3D(x, y6, z6)
y7 = np.linspace(7, 7, 100)
z7 = np.sin(7 * 2 * np.pi * x)
line7, = ax.plot3D(x, y7, z7)
y8 = np.linspace(8, 8, 100)
z8 = np.sin(8 * 2 * np.pi * x)
line8, = ax.plot3D(x, y8, z8)
y9 = np.linspace(9, 9, 100)
z9 = np.sin(9 * 2 * np.pi * x)
line9, = ax.plot3D(x, y9, z9)
y10 = np.linspace(10, 10, 100)
z10 = np.sin(10 * 2 * np.pi * x)
line10, = ax.plot3D(x, y10, z10)

x11 = np.linspace(-6, -6, 100)
y11 = np.linspace(1, 10, 10)
x12 = np.linspace(0, 2 * np.pi, 100, endpoint=False)
y12 = np.linspace(-100 / 2, 100 / 2 - 1, 100)

j = 0
while j < 10:
    z11 = np.fft.fftshift(abs(np.fft.fft(np.sin(x12 * y11[j]))))
    ax.plot3D(x11, y12 + y11[j], z11)
    j += 1


def update(i):
    line1.set_xdata(x[:i + 1])
    line1.set_ydata(y1[:i + 1])
    line1.set_3d_properties(z1[:i + 1])
    line2.set_xdata(x[:i + 1])
    line2.set_ydata(y2[:i + 1])
    line2.set_3d_properties(z2[:i + 1])
    line3.set_xdata(x[:i + 1])
    line3.set_ydata(y3[:i + 1])
    line3.set_3d_properties(z3[:i + 1])
    line4.set_xdata(x[:i + 1])
    line4.set_ydata(y4[:i + 1])
    line4.set_3d_properties(z4[:i + 1])
    line5.set_xdata(x[:i + 1])
    line5.set_ydata(y5[:i + 1])
    line5.set_3d_properties(z5[:i + 1])
    line6.set_xdata(x[:i + 1])
    line6.set_ydata(y6[:i + 1])
    line6.set_3d_properties(z6[:i + 1])
    line7.set_xdata(x[:i + 1])
    line7.set_ydata(y7[:i + 1])
    line7.set_3d_properties(z7[:i + 1])
    line8.set_xdata(x[:i + 1])
    line8.set_ydata(y8[:i + 1])
    line8.set_3d_properties(z8[:i + 1])
    line9.set_xdata(x[:i + 1])
    line9.set_ydata(y9[:i + 1])
    line9.set_3d_properties(z9[:i + 1])
    line10.set_xdata(x[:i + 1])
    line10.set_ydata(y10[:i + 1])
    line10.set_3d_properties(z10[:i + 1])
    return line1, line2, line3, line4, line5, line6, line7, line8, line9, line10


# 图像配置
ax.get_proj = lambda: np.dot(Axes3D.get_proj(ax), np.diag([0.8, 1, 0.5, 1]))
ax.grid(False)  # 隐藏网格线
ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.view_init(32, -32)  # 坐标轴转向
# ax.set_ylim(-0.5, 10.5)
# ax.set_ylim(-10, 10)
ax.set_xlabel("时间方向")
ax.set_ylabel("频率方向")

ax.text(-6, 20, 50, "频域图像", color='black')
# ax.text2D(0.05, 0.5, "频域图像", transform=ax.transAxes)

ani = animation.FuncAnimation(
    fig=fig, func=update, frames=100, interval=20, blit=True, repeat=True)

plt.show()
