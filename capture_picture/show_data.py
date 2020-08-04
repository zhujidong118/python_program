#! /usr/bin/env python3
# coding=utf-8
# writer zhujidong

import xlrd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


def read_excel(path):
    # 打开文件
    workbook = xlrd.open_workbook(path)
    # 获取所有sheet
    print(workbook.sheet_names())  # [u'sheet0', u'sheet2']
    list_sheet = workbook.sheet_names()  # 获取sheet的数目，即雾等级数
    num_fogleval = len(list_sheet)  # 雾等级数
    # 根据sheet索引或者名称获取sheet内容
    for i in range(num_fogleval):
        locals()['sheet' + str(i)] = workbook.sheet_by_index(i)

    num_channels = locals()['sheet0'].ncols  # 六种通道图片
    print(num_channels)
    '''
    # sheet的名称，行数，列数
    # print(sheet0.name, sheet0.nrows, sheet0.ncols)
    # 获取整行和整列的值（数组）
    # rows = sheet0.row_values(3)  # 获取第四行内容
    '''
    for i in range(num_fogleval):
        for j in range(num_channels):
            locals()['cols' + str(i) + str(j)] = locals()['sheet' + str(i)].col_values(j)  # cols[i][j]表示第i级雾图的第j通道值

    '产生data_Y0——data_Y1的数据'
    for i in range(num_fogleval):
        locals()['data_Y' + str(i)] = []
        for j in range(num_channels):
            locals()['data_Y' + str(i)].append(locals()['cols' + str(i) + str(j)])

    # Y_data = [Y0_data, Y1_data, Y2_data, Y3_data, Y4_data]  # 五个等级图像
    '产生Y_data'
    Y_data = []
    for i in range(num_fogleval):
        Y_data.append(locals()['data_Y' + str(i)])
    return Y_data, num_fogleval, num_channels


def show_datas(Y_data, nrows, ncols):
    x_data = list(range(1, nrows))  # 产生(1, nrows-1)的区间序列列表
    plt.rcParams['savefig.dpi'] = 300
    plt.rcParams['figure.dpi'] = 300
    '获取无雾图像'
    y_data00 = Y_data[0][0][1:]  # 获取表格中sheet0的第一列第二行到最后一行的数据
    y_data01 = Y_data[0][1][1:]
    y_data02 = Y_data[0][2][1:]
    y_data03 = Y_data[0][3][1:]
    y_data04 = Y_data[0][4][1:]
    '获取一级图像'
    y_data10 = Y_data[1][0][1:]
    y_data11 = Y_data[1][1][1:]
    y_data12 = Y_data[1][2][1:]
    y_data13 = Y_data[1][3][1:]
    y_data14 = Y_data[1][4][1:]
    '获取二级图像'
    y_data20 = Y_data[2][0][1:]
    y_data21 = Y_data[2][1][1:]
    y_data22 = Y_data[2][2][1:]
    y_data23 = Y_data[2][3][1:]
    y_data24 = Y_data[2][4][1:]
    '获取三级图像'
    y_data30 = Y_data[3][0][1:]
    y_data31 = Y_data[3][1][1:]
    y_data32 = Y_data[3][2][1:]
    y_data33 = Y_data[3][3][1:]
    y_data34 = Y_data[3][4][1:]
    '获取四级图像'
    y_data40 = Y_data[4][0][1:]
    y_data41 = Y_data[4][1][1:]
    y_data42 = Y_data[4][2][1:]
    y_data43 = Y_data[4][3][1:]
    y_data44 = Y_data[4][4][1:]
    'all'
    plt.plot(x_data, y_data00, color='black', linewidth=1.0, label='无雾')
    plt.plot(x_data, y_data10, color='blue', linewidth=1.0, label='一级')
    plt.plot(x_data, y_data20, color='green', linewidth=1.0, label='二级')
    plt.plot(x_data, y_data30, color='red', linewidth=1.0, label='三级')
    plt.plot(x_data, y_data40, color='gray', linewidth=1.0, label='四级')
    my_font = fm.FontProperties(fname="C:/Windows/Fonts/simhei.ttf")
    plt.legend(loc='lower left', prop=my_font)
    plt.title('ALL通道像素均值', fontproperties=my_font)
    plt.show()
    'blue'
    plt.plot(x_data, y_data01, color='black', linewidth=1.0, label='无雾')
    plt.plot(x_data, y_data11, color='blue', linewidth=1.0, label='一级')
    plt.plot(x_data, y_data21, color='green', linewidth=1.0, label='二级')
    plt.plot(x_data, y_data31, color='red', linewidth=1.0, label='三级')
    plt.plot(x_data, y_data41, color='gray', linewidth=1.0, label='四级')
    my_font = fm.FontProperties(fname="C:/Windows/Fonts/simhei.ttf")
    plt.legend(loc='lower left', prop=my_font)
    plt.title('BLUE通道像素均值', fontproperties=my_font)
    plt.show()
    'green'
    plt.plot(x_data, y_data02, color='black', linewidth=1.0, label='无雾')
    plt.plot(x_data, y_data12, color='blue', linewidth=1.0, label='一级')
    plt.plot(x_data, y_data22, color='green', linewidth=1.0, label='二级')
    plt.plot(x_data, y_data32, color='red', linewidth=1.0, label='三级')
    plt.plot(x_data, y_data42, color='gray', linewidth=1.0, label='四级')
    my_font = fm.FontProperties(fname="C:/Windows/Fonts/simhei.ttf")
    plt.legend(loc='lower left', prop=my_font)
    plt.title('GREEN通道像素均值', fontproperties=my_font)
    plt.show()
    'red'
    plt.plot(x_data, y_data03, color='black', linewidth=1.0, label='无雾')
    plt.plot(x_data, y_data13, color='blue', linewidth=1.0, label='一级')
    plt.plot(x_data, y_data23, color='green', linewidth=1.0, label='二级')
    plt.plot(x_data, y_data33, color='red', linewidth=1.0, label='三级')
    plt.plot(x_data, y_data43, color='gray', linewidth=1.0, label='四级')
    my_font = fm.FontProperties(fname="C:/Windows/Fonts/simhei.ttf")
    plt.legend(loc='lower left', prop=my_font)
    plt.title('RED通道像素均值', fontproperties=my_font)
    plt.show()
    'gray'
    plt.plot(x_data, y_data04, color='black', linewidth=1.0, label='无雾')
    plt.plot(x_data, y_data14, color='blue', linewidth=1.0, label='一级')
    plt.plot(x_data, y_data24, color='green', linewidth=1.0, label='二级')
    plt.plot(x_data, y_data34, color='red', linewidth=1.0, label='三级')
    plt.plot(x_data, y_data44, color='gray', linewidth=1.0, label='四级')
    my_font = fm.FontProperties(fname="C:/Windows/Fonts/simhei.ttf")
    plt.legend(loc='lower left', prop=my_font)
    plt.title('GRAY通道像素均值', fontproperties=my_font)
    plt.show()


def pinghua(Y_data, num_fogleval, num_channels):
    # x_data = list(range(1, nrows))  # 产生(1, nrows-1)的区间序列列表
    plt.rcParams['savefig.dpi'] = 300
    plt.rcParams['figure.dpi'] = 300
    '获取图像'
    for i in range(num_fogleval):
        for j in range(num_channels):
            locals()['y_data' + str(i) + str(j)] = Y_data[i][j][1:]  # y_data[i][j]表示第i级雾图像的第j列数据

    '求取平均值'
    for i in range(num_fogleval):
        for n in range(num_channels):
            num = 0
            for j in range(len(locals()['y_data' + str(i) + str(n)])):
                num += locals()['y_data' + str(i) + str(n)][j]
            locals()['y_data_av' + str(i) + str(n)] = num / len(locals()['y_data' + str(i) + str(n)])

    '平滑处理'
    for i in range(num_fogleval):
        for j in range(num_channels):
            temp = locals()['y_data_av' + str(i) + str(j)]
            temp1 = locals()['y_data' + str(i) + str(j)].copy()
            yuzhi = 500
            for n in range(len(locals()['y_data' + str(i) + str(j)])):
                if temp1[n] < (temp + yuzhi) and temp1[n] > (temp - yuzhi):
                    pass
                else:
                    locals()['y_data' + str(i) + str(j)][n] = locals()['y_data_av' + str(i) + str(j)]
            locals()['x_data' + str(i) + str(j)] = list(range(1, len(locals()['y_data' + str(i) + str(j)]) + 1))
            # 产生对应长度的横轴坐标

    '制表'
    colors = ['black', 'blue', 'green', 'red', 'gray']
    labels = ['无雾', '一级', '二级', '三级', '四级']
    titles = ['ALL通道像素均值', 'BLUE通道像素均值', 'GREEN通道像素均值', 'RED通道像素均值', 'GRAY通道像素均值', '暗通道像素均值']
    for i in range(num_channels):
        for j in range(num_fogleval):
            plt.plot(locals()['x_data' + str(j) + str(i)], locals()['y_data' + str(j) + str(i)], color=colors[j],
                     linewidth=1.0, label=labels[j])
            my_font = fm.FontProperties(fname="C:/Windows/Fonts/simhei.ttf")
            plt.legend(loc='lower left', prop=my_font)
            plt.title(titles[i], fontproperties=my_font)
        plt.savefig("E:\\python\\capture_picture\\result\\19_11_18\\" + titles[i] + ".png")
        plt.show()


if __name__ == '__main__':
    path = 'E:/python/capture_picture/num_data/19_11_18/all_data.xls'
    Y_data, num_fogleval, num_channels = read_excel(path)
    # show_datas(Y_data, nrows, ncols)
    pinghua(Y_data, num_fogleval, num_channels)
