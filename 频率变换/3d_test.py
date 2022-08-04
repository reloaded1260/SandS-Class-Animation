# 导入三维工具包mplot3d
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
# 创建3d绘图区域
ax = plt.axes(projection='3d')
# 从三个维度构建
z = np.linspace(0, 1, 100)
x = z * np.sin(20 * z)
y = z * np.cos(20 * z)
# 调用 ax.plot3D创建三维线图
ax.plot3D(x, y, z, 'gray')
ax.set_title('3D line plot')
plt.show()
