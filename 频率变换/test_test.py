import matplotlib.pyplot as plt
import numpy as np
fs = np.linspace(1, 10, 10)
x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)
i = 1
while i < 9:
    i += 1
    y += np.sin(x * fs[i])
plt.plot(x, y)
plt.show()
