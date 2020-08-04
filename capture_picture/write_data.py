import xlwt
import cv2
import os

from jiemian.D1121.avgbgr import avgbgr_demo1, avgbgr_demo2


#  将数据写入新文件
def data_write0(file_path, datas, num_pic):  # filename为写入CSV文件的路径，data为要写入数据列表
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet

    # 将数据写入第 i 行，第 j 列
    for i in range(0, num_pic):
        for j in range(0, 5):
            sheet1.write(i, j, datas[i][j])

    f.save(file_path)  # 保存文件


def data_write1(image_path, file_path):  # filename为写入CSV文件的路径，data为要写入数据列表
    labels = ['0_wu\\', '1_yiji\\', '2_erji\\', '3_sanji\\', '4_siji\\']
    titles = ['wu_', 'yiji_', 'erji_', 'sanji_', 'siji_']
    dirnum = 0  # 文件夹数量，雾图等级
    filenum = 0  # 文件数量，每个雾图等级中图片数量
    # path = 'E:\\python\\capture_picture\\pic_data\\geban\\

    '计算文件夹数量'
    for lists in os.listdir(image_path):
        sub_path = os.path.join(image_path, lists)
        print(sub_path)
        if os.path.isdir(sub_path):
            dirnum = dirnum + 1

    '计算文件夹下的文件数量'
    image_path1 = image_path + labels[0]
    for lists in os.listdir(image_path1):
        sub_path = os.path.join(image_path1, lists)
        # print(sub_path)
        if os.path.isfile(sub_path):
            filenum = filenum + 1

    '产生对应数量的sheet'
    f = xlwt.Workbook()
    for i in range(1, (dirnum + 1)):
        #  locals()['sheet' + str(i)] = f.add_sheet(str(locals()['sheet' + str(i)]), cell_overwrite_ok=True)
        locals()['sheet' + str(i)] = f.add_sheet(('sheet' + str(i)), cell_overwrite_ok=True)
    # 将数据写入第 i 行，第 j 列
    datas = []
    for i in range(dirnum):  # 雾图级别
        data = []
        for j in range(1, (filenum + 1)):  # 图片数量
            image_path2 = image_path + labels[i] + titles[i] + str(j) + ".jpg"
            print(image_path2)
            image0 = cv2.imread(image_path2)
            data.append(avgbgr_demo1(image0))
        datas.append(data)

    for i in range(dirnum):
        for j in range(1, (filenum + 1)):
            for k in range(0, 6):
                locals()['sheet' + str(i + 1)].write(j, k, datas[i][j - 1][k])

    f.save(file_path)  # 保存文件


if __name__ == '__main__':
    print("-----------------hello opencv----------------")
    '''
    num_pic = 500  # 图片数量
    datas = []
    for num in range(1, (num_pic + 1)):
        image_path = "E:/python/capture_picture/pic_data/geban/1_yiji/" + "yiji_" + str(num) + ".jpg"
        print(image_path)
        image0 = cv2.imread(image_path)
        datas.append(avgbgr_demo1(image0))  # 不加窗
        # datas.append(avgbgr_demo2(image0))  # 加窗
        # print(datas)
    file_path = "E:/python/capture_picture/num_data/gebanbujiachuang/1_yiji.xls"
    data_write0(file_path, datas, num_pic)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''
    image_path = "E:\\python\\capture_picture\\pic_data\\19_11_18\\"
    file_path = "E:\\python\\capture_picture\\num_data\\19_11_18\\all_data.xls"
    data_write1(image_path, file_path)
