#! /usr/bin/env/ python3
# coding=utf-8
# date 2019.11.20
# wirte zhujidong

import os


def count_file_and_dir_num(path):
    '''
    获取path路径下的文件夹及文件数量，但不包括子文件夹的内容
    :param path: 文件路径字符串
    :return: 返回path路径下的文件夹及文件的数量，dirnum:文件夹数量，filenum:文件数量
    '''
    dirnum = 0  # 文件夹数量
    filenum = 0  # 文件数量
    for lists in os.listdir(path):
        sub_path = os.path.join(path, lists)
        print(sub_path)
        if os.path.isfile(sub_path):
            filenum = filenum + 1
        elif os.path.isdir(sub_path):
            dirnum = dirnum + 1
    # print('dirnum: ', dirnum)
    # print('filenum: ', filenum)
    return dirnum, filenum


if __name__ == '__main__':
    path = 'E:\\python\\capture_picture\\pic_data\\geban\\0_wu\\'
    count_file_and_dir_num(path)
    print(type(count_file_and_dir_num))
    help(count_file_and_dir_num)
