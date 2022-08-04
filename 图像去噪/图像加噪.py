import numpy as np
from skimage import io

img = io.imread("LenaRGB.bmp")
rows, cols, dims = img.shape
for i in range(5000):
    x = np.random.randint(0, rows)
    y = np.random.randint(0, cols)
    img[x, y, :] = 255

io.imshow(img)
io.show()
io.imsave('noised.bmp', img)

# https://www.yisu.com/zixun/168820.html
