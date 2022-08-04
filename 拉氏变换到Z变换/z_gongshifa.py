import numpy as np
from matplotlib import pyplot as plt
from sympy import *

fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 100)
# axis_x = np.linspace(-50, 49, 100)
# plot(axis_x, ftt_f)
f = np.sin(x)
ftt_f = np.fft.fftshift(abs(fft(f)))
t = symbols("t")
e = np.exp(1)
theta = np.linspace(0, 2 * np.pi, 100)
w = np.ones(100)
i = 0
f_w = list[range(100)]
F_w = list[range(100)]
while i < 100:
    i += 1
    f_w[i] = ftt_f * (e ** (-1 * theta * t))
    F_w[i] = integrate(f_w[i], t)

ax.plot(F_w, t)
plt.show()
