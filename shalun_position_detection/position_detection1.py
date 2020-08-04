#! /env/ python3
# coding=utf-8
# date 2019.11.21
# write graysnow

import cv2
import math
import numpy as np
import sys, os

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']

from shalun_position_detection.rotate_image import rotate, rotate_bound


def compute_contour(image, thresh=80, rho=1, theta=np.pi / 180, threshold=20, minLineLength=100, maxLineGap=100):
    '''
    :param image: 输入图像
    :param thresh: 二值化阈值，100
    :param rho: 参数极径 r 以像素值为单位的分辨率. 我们使用 1 像素，1
    :param theta: 参数极角 \theta 以弧度为单位的分辨率. 我们使用 1度 (即CV_PI/180)，np.pi/180
    :param threshold: 设置阈值： 一条直线所需最少的的曲线交点。超过设定阈值才被检测出线段，值越大，
    基本上意味着检出的线段越长，检出的线段个数越少，200
    :param minLinLength: 能组成一条直线的最少点的数量. 点数量不足的直线将被抛弃，300
    :param maxLlineGap: 能被认为在一条直线上的两点的最大距离，200
    :return:
    '''
    # blur_src = cv2.GaussianBlur(src, (3, 3), 0)
    gray_src = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thre_src = cv2.threshold(gray_src, thresh, 255, cv2.THRESH_BINARY_INV)
    contours, hierachy = cv2.findContours(thre_src, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    blank_src = np.zeros((image.shape[0], image.shape[1]), np.uint8)  # 创建一个空白图片
    blank_src1 = np.zeros((image.shape[0], image.shape[1]), np.uint8)  # 创建一个空白图片
    cv2.drawContours(blank_src, contours, -1, (255, 255, 255), 2)  # 用于查找直线
    cv2.drawContours(blank_src1, contours, -1, (255, 255, 255), 1)  # 用于显示

    dst = cv2.bitwise_not(blank_src1)  # 用于计算
    dst1 = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)

    zuobiao1 = []
    zuobiao2 = []
    flag_compute = True

    "分层计算"
    rows, cols = dst.shape
    for i in range(15, rows, 10):
        a = [0, 0]
        b = [0, 0]
        for j in range(cols - 20):
            if dst[i, j] != 255:
                b = [i, j]
        for k in range(cols - 20, 20, -1):
            if dst[i, k] != 255:
                a = [i, k]

        "画直线"
        if a[0] == 255 and b[0] == 255:
            pass
        else:
            if a == [0, 0]:
                pass
            else:
                zuobiao1.append(a)
                zuobiao2.append(b)

                cv2.line(dst1, (a[1], a[0]), (b[1], b[0]), (255, 0, 0), 1, 8)
        "计算长度，并写在图上"
        len = round(abs(5.5 * (b[1] - a[1]) / 423), 3)
        # text = "len: " + str(len)
        text = str(len)
        cv2.putText(dst1, text, (b[1] + 10, b[0]), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    zuobiao2.reverse()
    zuobiao = zuobiao1 + zuobiao2

    return flag_compute, dst1, zuobiao


def compute_angle(point1=[0, 0], point2=[0, 0]):
    a = [(point1[0] - point2[0]), (point1[1] - point2[1])]
    b = [(50 - 50), (0 - 100)]
    len_a = math.sqrt(pow(a[0], 2) + pow(a[1], 2))
    len_b = math.sqrt(pow(b[0], 2) + pow(b[1], 2))
    cos_value = (a[0] * b[0] + a[1] * b[1]) / (len_a * len_b)
    cos_value = round(cos_value, 3)
    angle_value = round(np.arccos(cos_value) * (180 / np.pi), 3)
    return angle_value


def contour_interpolation(zuobiao):
    import numpy as np
    import scipy.interpolate as spi
    import matplotlib.pyplot as plt

    plt.rcParams['savefig.dpi'] = 300
    plt.rcParams['figure.dpi'] = 300
    # 生成[-10,10]内长度为41的序列
    # x = np.linspace(-10, 10, 41)
    # y = np.sin(x ** 3) / np.cos(x ** 2)

    x = []
    y = []
    for X, Y in zuobiao:
        x.append(X)
        y.append(Y)
    if len(x) == 0:
        image1 = cv2.imread("E:\\python\\shalun_position_detection\\pic_data\\result.jpg")
    else:

        # 观测数据点
        ix3 = np.linspace(x[0], x[-1], 200)
        # 三次样条插值
        # ipo3 = spi.splrep(x, y, k=3)  # 生成模型参数
        # iy3 = spi.splev(ix3, ipo3)  # 生成插值点

        plt.axis("equal")
        plt.plot(x, y)
        # plt.plot(iy3, -ix3)

        plt.legend(['origin', 'interp'], loc='upper left')
        plt.savefig("E:\\python\\shalun_position_detection\\pic_data\\nihe.png")
        plt.show()
        plt.close()
        image1 = cv2.imread("E:\\python\\shalun_position_detection\\pic_data\\nihe.png")
    return image1


if __name__ == "__main__":
    # src = cv2.imread(".\\pic_data\\WIN_20191127_10_05_15_Pro.jpg")
    src = cv2.imread("C:\\Users\\graysnow\\Pictures\\Camera Roll\\WIN_20191216_10_22_15_Pro1.jpg")
    # src = cv2.resize(src, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
    if src is None:
        print("could not load imgae...\n")
    else:
        src = cv2.resize(src, (0, 0), fx=0.5, fy=0.5)
        flag_compute, dst, zuobiao = compute_contour(src)
        cv2.imshow("src", src)
        cv2.imshow("dst", dst)
        cv2.imwrite("./pic_data/result.jpg", dst)
        print(zuobiao)
        contour_interpolation(zuobiao)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
