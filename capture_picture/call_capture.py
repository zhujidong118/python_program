from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cv2
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5.QtGui import QImage, QPixmap
# import os
# os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

from capture import Ui_Form  # 导入.ui转换为.py中的类


class MyForm(QWidget, Ui_Form):
    # 建立的是Main Window项目，故此处导入的是QMainWindow
    # class myform(QWidget,Ui_Form):如建立的是Widget项目，导入的是QWidget
    def __init__(self):
        super(MyForm, self).__init__()
        self.setupUi(self)

        self.timer_camera = QtCore.QTimer()  # 定义定时器，用于控制显示视频的帧率
        self.timer_garb = QtCore.QTimer()  # 定义定时抓取定时器，用于控制自动抓取图片
        # self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 视频流
        self.cap = cv2.VideoCapture()  # 视频流

        self.CAM_NUM = 0  # 为0时表示视频流来自笔记本内置摄像头
        self.name_num = 0
        self.camera_state = 0
        self.slot_init()

    def slot_init(self):

        self.timer_camera.timeout.connect(self.show_camera)
        self.timer_garb.timeout.connect(self.grab_camera)
        self.pushButton_3.clicked.connect(self.directory_file)  # “保存路径”按钮槽函数
        self.label_7.setVisible(False)  # 隐藏图片保存路径
        self.label_6.setVisible(False)  # 隐藏图片抓取数量
        '检测相机是否打开，并提示'
        if self.timer_camera.isActive() == False:  # 若定时器未启动
            self.flag = self.cap.open(self.CAM_NUM, cv2.CAP_DSHOW)  # 参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频
            if self.flag == False:  # flag表示open()成不成功
                msg = QtWidgets.QMessageBox.warning(self, '提示', "请检查相机于电脑是否连接正确",
                                                    buttons=QtWidgets.QMessageBox.Ok)
                self.camera_state = 0
            else:
                self.timer_camera.start(24)  # 定时器开始计时24ms，结果是每过24ms从摄像头中取一帧显示
                self.camera_state = 1
                self.pushButton.setText('关闭相机')

    '''打开/关闭相机'''

    @pyqtSlot()
    def on_pushButton_clicked(self):
        if self.timer_camera.isActive() == False:  # 若定时器未启动
            self.flag = self.cap.open(self.CAM_NUM, cv2.CAP_DSHOW)  # 参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频
            if self.flag == False:  # flag表示open()成不成功
                msg = QtWidgets.QMessageBox.warning(self, '提示', "请检查相机于电脑是否连接正确",
                                                    buttons=QtWidgets.QMessageBox.Ok)
                self.camera_state = 0
            else:
                self.timer_camera.start(24)  # 定时器开始计时30ms，结果是每过30ms从摄像头中取一帧显示
                self.camera_state = 1
                self.pushButton.setText('关闭相机')
        else:
            self.timer_camera.stop()  # 关闭定时器
            self.timer_garb.stop()
            self.cap.release()  # 释放视频流
            self.label.clear()  # 清空视频显示区域
            self.camera_state = 0
            self.pushButton.setText('打开相机')

    '''显示视频'''

    def show_camera(self):
        # self.cap.set(3, 2592)
        # self.cap.set(4, 1944)
        flag, self.image = self.cap.read()  # 从视频流中读取
        show = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0],
                                 QtGui.QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
        showImage = showImage.scaled(self.label.width(), self.label.height(), Qt.KeepAspectRatio,
                                     Qt.SmoothTransformation)  # 按比例缩放
        self.label.setAlignment(Qt.AlignCenter)  # 居中显示
        self.label.setPixmap(QtGui.QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage

    '开始/停止拍摄'

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        if self.timer_garb.isActive() == False:
            if self.camera_state == False:
                msg = QtWidgets.QMessageBox.warning(self, '提示', "相机未启动",
                                                    buttons=QtWidgets.QMessageBox.Ok)
                self.pushButton_2.setText('开始抓取')
            else:
                self.timer_garb.start(250)
                self.pushButton_2.setText('停止抓取')
                self.label_6.setVisible(True)  # 显示图片抓取数量
        else:
            self.timer_garb.stop()
            self.pushButton_2.setText('开始抓取')

    '拍摄照片'

    def grab_camera(self):
        if self.name_num <= int(self.lineEdit_3.text()) - 1:
            flag, self.image = self.cap.read()  # 从视频流中读取
            # show = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
            self.name_num += 1
            self.label_6.setText('目前抓取图片数量： ' + str(self.name_num))
            # name_str = "yiji_{}".format(self.name_num)
            # cv2.imwrite("E:\\python\\capture_picture\\pic_data\\19_11_19\\1_yiji\\" + name_str + ".jpg", self.image)
            cv2.imwrite(self.directory + '/' + self.lineEdit_2.text() + str(self.name_num) + ".jpg", self.image)
        else:
            self.timer_garb.stop()
            self.label_6.setVisible(False)  # 隐藏图片抓取数量
            self.pushButton_2.setText('开始抓取')
            msg = QtWidgets.QMessageBox.warning(self, '提示', "图片抓取完成",
                                                buttons=QtWidgets.QMessageBox.Ok)

    '''选择保存文件路径'''

    def directory_file(self):
        self.directory = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")  # 起始路径
        self.label_7.setVisible(True)  # 显示图片保存路径
        self.label_7.setText("文件路径为 " + self.directory + '/')
        print(self.directory + '/')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec_())
