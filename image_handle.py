# 图片二值化
import os
from PIL import Image
from numpy import array

# img = Image.open('test_0.png')


def hury(file_path='test_0.png', out_file_path="test_1.png"):
    img = Image.open(file_path)
    # 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
    Img = img.convert('L')
    Img.save(out_file_path)


def twocolor(file_path='test_0.png', out_file_path="test_1.png", threshold=200):
    print(file_path)
    print(out_file_path)
    img = Image.open(file_path)
    img = clean_img(img)
    Img = img.convert('L')
    # 自定义灰度界限，大于这个值为黑色，小于这个值为白色
    # threshold = 90
    # threshold = 150
    threshold = 200
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    # 图片二值化
    photo = Img.point(table, '1')
    # img = photo
    # img = clean_img(img)
    # img = clean_img_eight(img)
    # photo = img
    photo.save(out_file_path)


# 根据图片特点，自己写的降噪算法
def clean_img(img, threshold=100):
    width, height = img.size
    for j in range(height):
        for i in range(width):
            point = img.getpixel((i, j))
            if point == 0:
                for x in range(threshold):
                    if j + x >= height:
                        break
                    else:
                        if point != img.getpixel((i, j + x)):
                            img.putpixel((i, j), 1)
                            break
    return img


# 八值法降噪
def clean_img_eight(img, threshold=100):
    width, height = img.size
    arr = [[0 for col in range(width)] for row in range(height)]
    arr = array(arr)
    for j in range(height):
        for i in range(width):
            point = img.getpixel((i, j))
            if point == 0:
                sum = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if i + x > width - 1 or j + y > height - 1 or \
                                i + x < 0 or j + y < 0:
                            sum += 1
                        else:
                            sum += img.getpixel((i + x, j + y))
                if sum >= threshold:
                    arr[j, i] = 1

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i, j] == 1:
                img.putpixel((j, i), 1)
    return img




files = os.listdir("./images")
for file in files:
    twocolor(file_path="./images/" + file, out_file_path="./new_image_clean/" + file)
