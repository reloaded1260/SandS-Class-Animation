import skimage
import os
from skimage import io
import random


def addGaussNoise(s):
    var = random.uniform(0.0001, 0.04)
    origin = skimage.io.imread(s)
    noisy = skimage.util.random_noise(origin, mode='gaussian', var=var)
    return noisy


def addSaltNoise(s):
    var = random.uniform(0.01, 0.2)
    origin = skimage.io.imread(s)
    noisy = skimage.util.random_noise(origin, mode='s&p', amount=var)
    noisy = (noisy*255.0).astype('uint8')
    return noisy


def addSpeckleNoise(s):
    var = random.uniform(0.0001, 0.04)
    origin = skimage.io.imread(s)
    noisy = skimage.util.random_noise(origin, mode='speckle', var=var)
    return noisy


if __name__ == '__main__':
    file_pathname = "LenaRGB.bmp"
    save_pathname = "noised.bmp"
    # for filename in os.listdir(file_pathname):
    #     index = random.randint(0, 3)
    #     if index == 0:  # 如果是0，什么都不做
    #         continue
    #     elif index == 1:  # 添加高斯噪声
    #         res = addGaussNoise(file_pathname + '/' + filename)
    #         io.imsave(save_pathname + filename, res)
    #     elif index == 2:  # 添加椒盐噪声
    #         res = addGaussNoise(file_pathname + '/' + filename)
    #         io.imsave(save_pathname + filename, res)
    #     elif index == 3:  # 添加乘法噪声
    #         res = addGaussNoise(file_pathname + '/' + filename)
    #         io.imsave(save_pathname + filename, res)
    res = addSaltNoise(file_pathname)
    io.imsave(save_pathname, res)
