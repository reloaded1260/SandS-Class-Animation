from PIL import Image


# 求图像img中(x,y)处像素的中值c
def median(img, x, y):
    # Begin
    L = []
    xl = [x - 1, x, x + 1]
    yl = [y - 1, y, y + 1]
    for i in xl:
        for j in yl:
            gray = img.getpixel((i, j))  # 取出灰度值
            L.append(gray)
    L.sort()
    c = L[4]
    # End
    return c


# 对图像文件1进行降噪，并将结果保存为图像文件2
# 图像文件1和2的路径分别为path1和path2
def denoise(path1, path2):
    img1 = Image.open(path1)  # 图像1
    img1 = img1.convert('L')  # 将图像1转换为灰度图
    w, h = img1.size
    img2 = Image.new('L', (w, h), 'white')  # 图像2
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            c = median(img1, x, y)  # 求中值
            img2.putpixel((x, y), c)  # 将灰度设置为中值
    img2.save(path2)


path1 = 'noised.bmp'  # 带噪声的图像
path2 = 'filter.bmp'  # 降噪后的图像
denoise(path1, path2)

# https://blog.csdn.net/qq_42833469/article/details/121581439
