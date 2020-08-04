#! /env/ python3
# coding=utf-8
# date 2019.11.21
# write graysnow

import sys, os

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
import cv2
import math
import numpy as np


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
    dst1 = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)  # 用于划线分析及返回显示

    zuobiao1 = []  # 左侧坐标
    zuobiao2 = []  # 右侧坐标
    len_contour = []  # 轮廓界面直径，用于求出最长直径
    # flag_compute = True

    "分层计算"
    rows, cols = dst.shape
    for i in range(10, rows, 1):
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
                len_line = round(abs(5.38 * (b[1] - a[1]) / 393), 3)
                len_contour.append(len_line)
                if i % 20 == 0:
                    cv2.line(dst1, (a[1], a[0]), (b[1], b[0]), (255, 0, 0), 1, cv2.LINE_AA)
                    "计算长度，并写在图上"
                    text = str(len_line)
                    cv2.putText(dst1, text, (b[1] + 10, b[0]), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 1)
    '以最长轮廓直径为原点基准'
    if len(zuobiao1) > 0 and len(zuobiao2) > 0:
        flag_compute = 1
        zuobiao2.reverse()
        zuobiao = zuobiao1 + zuobiao2 + [zuobiao1[0]]  # 原像素坐标
        # print(min_len_contour)
        # print(np.where(len_contour==np.max(len_contour)))
        # print(list(np.where(len_contour == np.max(len_contour))))
        tuple_max_len_contour = np.where(len_contour == np.max(len_contour))
        list_max_len_contour = list(tuple_max_len_contour)
        zuobiao_max_len_contour = list_max_len_contour[0][int(len(list_max_len_contour[0]) / 2)]
        # print(zuobiao_max_len_contour)
        # print(len_contour[zuobiao_max_len_contour])  # 求取轮廓直径最大值
        yuandian_zuobiao = [(zuobiao[zuobiao_max_len_contour][0] + zuobiao[-(zuobiao_max_len_contour + 2)][0]) / 2,
                            (zuobiao[zuobiao_max_len_contour][1] + zuobiao[-(zuobiao_max_len_contour + 2)][1]) / 2]
        # print(zuobiao[-(zuobiao_max_len_contour + 2)][0])
        # print(zuobiao[zuobiao_max_len_contour][0])
        zuobiao_xiangdui = zuobiao
        zuobiao_xiangdui = (np.array(zuobiao_xiangdui) - np.array(yuandian_zuobiao)).tolist()
    else:
        flag_compute = 0
        # zuobiao = []
        zuobiao_xiangdui = []
    '''
    # "计算4毫米"
    # cv2.line(dst1, (zuobiao[7][1], zuobiao[7][0]), (zuobiao[36][1], zuobiao[36][0]), (255, 0, 0), 1, cv2.LINE_AA)
    # "计算长度，并写在图上"
    # len = round(abs(5.38 * (zuobiao[7][0] - zuobiao[36][0]) / 194), 3)
    # # text = "len: " + str(len)
    # text = str(len)
    # cv2.putText(dst1, text, (zuobiao[7][0] + 40, zuobiao[7][1] - 20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)

    # "计算2.635毫米"
    # cv2.line(dst1, (zuobiao[12][1], zuobiao[12][0]), (zuobiao[31][1], zuobiao[31][0]), (255, 0, 0), 1, cv2.LINE_AA)
    # "计算长度，并写在图上"
    # len = round(abs(5.38 * (zuobiao[12][0] - zuobiao[31][0]) / 194), 3)
    # # text = "len: " + str(len)
    # text = str(len)
    # cv2.putText(dst1, text, (zuobiao[31][1]-50, zuobiao[31][0]), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)
    "计算1.5毫米"
    # for i in zuobiao[0:105]:
    #     for j in zuobiao:
    #         # if (i[1]-1)<j[0] and j[1]<(i[0]+1):
    #         if i[1]==j[1]:
    #             if abs(i[0]-j[0])==55:
    #                 print(zuobiao.index(i))
    #                 print(zuobiao.index(j))
    #                 break
    #     else:
    #         print("没有找到！")
    cv2.line(dst1, (zuobiao[77][1], zuobiao[77][0]), (zuobiao[132][1], zuobiao[132][0]), (255, 0, 0), 1, cv2.LINE_AA)
    "计算长度，并写在图上"
    len = round(abs(5.38 * (zuobiao[77][0] - zuobiao[132][0]) / 194), 3)
    # text = "len: " + str(len)
    text = str(len)
    cv2.putText(dst1, text, (zuobiao[31][1] - 50, zuobiao[31][0]), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)

    "计算做外侧距离1.5毫米"
    # temp = []
    # for i in zuobiao:
    #     temp.append(i[1])
    # print(temp.index(min(temp)))
    cv2.line(dst1, (zuobiao[102][1], zuobiao[102][0]), (40, zuobiao[102][0]), (255, 0, 0), 1, cv2.LINE_AA)
    "计算长度，并写在图上"
    len = round(abs(5.38 * (zuobiao[77][1] - zuobiao[102][1]) / 194), 3)
    # text = "len: " + str(len)
    text = str(len)
    cv2.putText(dst1, text, (zuobiao[102][1]+50, zuobiao[102][0]), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)
    '''
    return flag_compute, dst1, zuobiao_xiangdui, len_contour[zuobiao_max_len_contour]


def compute_angle(point1=[0, 0], point2=[0, 0]):
    a = [(point1[0] - point2[0]), (point1[1] - point2[1])]
    b = [(50 - 50), (0 - 100)]
    len_a = math.sqrt(pow(a[0], 2) + pow(a[1], 2))
    len_b = math.sqrt(pow(b[0], 2) + pow(b[1], 2))
    cos_value = (a[0] * b[0] + a[1] * b[1]) / (len_a * len_b)
    cos_value = round(cos_value, 3)
    angle_value = round(np.arccos(cos_value) * (180 / np.pi), 3)
    return angle_value


def contour_interpolation(zuobiao, path):
    import numpy as np
    import matplotlib.pyplot as plt

    plt.rcParams['savefig.dpi'] = 300
    plt.rcParams['figure.dpi'] = 300

    x = []
    y = []
    for X, Y in zuobiao:
        x.append(Y)
        y.append(X)
    if len(x) == 0:
        # image1 = cv2.imread("E:\\python\\shalun_position_detection\\pic_data\\result_detection\\result.jpg")
        image1 = np.zeros([640, 480, 3], np.uint8)
    else:
        plt.axis("equal")
        plt.plot(x, y)
        ax = plt.gca()
        ax.xaxis.set_ticks_position('top')
        ax.invert_yaxis()
        ax.spines['right'].set_color('none')
        ax.spines['bottom'].set_color('none')
        ax.spines['left'].set_position(('data', 0))
        ax.spines['top'].set_position(('data', 0))

        plt.legend(['interpolation'], loc='upper left')
        plt.savefig(path + "nihe.png")
        plt.show()
        plt.close()
        image1 = cv2.imread(path + "nihe.png")
    return image1


def save_zuobiao_xiangdui_txt(filename, data):
    file = open(filename, 'w')
    for i in range(len(data)):
        s = str(data[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        s = str(i) + '  ' + s.replace(',', '') + ' 0.00' + '\n'  # 去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    # print("保存文件成功")


def mkdir(path):
    # 引入模块

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        # print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        # print(path + ' 目录已存在')
        return False


if __name__ == "__main__":
    # src = cv2.imread(".\\pic_data\\wait_detection\\20191217-103730-993.jpg")
    src = cv2.imread(".\\jiemian\\pic_data\\wait_detection\\2.jpg")
    # src = cv2.imread("C:\\Users\\graysnow\\Pictures\\Camera Roll\\WIN_20191216_10_22_15_Pro1.jpg")
    # src = (cv2.resizesrc, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
    if src is None:
        print("could not load imgae...\n")
    else:
        # src = cv2.resize(src, (0, 0), fx=0.5, fy=0.5)
        flag_compute, dst, zuobiao_xiangdui, max_len_contour = compute_contour(src)
        cv2.imshow("src", src)
        cv2.imshow("dst", dst)
        cv2.imwrite("./jiemian/pic_data/result_detection/result.jpg", dst)
        # print(zuobiao_xiangdui)
        contour_interpolation(zuobiao_xiangdui, "./jiemian/pic_data/result_detection/")

        save_zuobiao_xiangdui_txt(
            "E:\\python\\shalun_position_detection\\jiemian\\pic_data\\result_detection\\zuobiao_xiangdui.txt",
            zuobiao_xiangdui)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
