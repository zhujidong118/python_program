#! /usr/bin/env python3
# coding=utf-8
# date 2019.10.30
# writer graysnow

import cv2


def image_jiachuang(image0):
    '''
    在读取图片上画出特定大小及位置的框
    :param image0:
    :return:
    '''
    ptLeftTop = (102, 188)
    ptRightBottom = (463, 447)
    point_color = (0, 0, 255)
    thickness = 1
    lineType = 8
    cv2.rectangle(image0, ptLeftTop, ptRightBottom, point_color, thickness, lineType)
    cv2.imshow("jiachuang", image0)


if __name__ == "__main__":
    print("--------------------opencv-python------------------------")
    image0 = cv2.imread("E:\\python\\capture_picture\\pic_data\\jiashi\\4_siji\\siji_1.jpg")
    if image0 is None:
        print('could not load image...\\')
    else:
        image_jiachuang(image0)
        print(image0.shape[0])
        cv2.waitKey(0)
        cv2.destroyAllWindows()
