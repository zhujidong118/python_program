#! /env/ python3
# coding=utf-8
# date 2019.11.21
# write graysnow


import sys, os

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy as np
from PyQt5.QtCore import pyqtSlot, Qt, QRect
from PyQt5.QtWidgets import QDesktopWidget, QFileDialog, QLabel, QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen
import threading

from ui_detection import Ui_MainWindow  # 导入.ui转换为.py中的类
from ui_pic_param import Ui_Dialog
from ui_rect_jiequ import Ui_Dialog_jiequ
from shalun_position_detection.position_detection import compute_contour, contour_interpolation, \
    save_zuobiao_xiangdui_txt


class MyLabel(QLabel):
    def __init__(self, parent=None):
        super(MyLabel, self).__init__(parent)
        self.x0 = 0
        self.y0 = 0
        self.x1 = 864
        self.y1 = 648
        self.flag = False

    # 鼠标点击事件
    def mousePressEvent(self, event):
        self.flag = True
        self.x0 = event.x()
        self.y0 = event.y()

    # 鼠标释放事件
    def mouseReleaseEvent(self, event):
        self.flag = False
        # print(self.x0)
        # print(self.y0)
        # print(self.x1)
        # print(self.y1)

    # 鼠标移动事件
    def mouseMoveEvent(self, event):
        if self.flag:
            self.x1 = event.x()
            self.y1 = event.y()
            self.update()

    # 绘制事件
    def paintEvent(self, event):
        super().paintEvent(event)
        rect = QRect(self.x0, self.y0, abs(self.x1 - self.x0), abs(self.y1 - self.y0))
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red, 1, Qt.SolidLine))
        painter.drawRect(rect)


class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # 建立的是Main Window项目，故此处导入的是QMainWindow
    # class myform(QWidget,Ui_Form):如建立的是Widget项目，导入的是QWidget
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        # self.setFixedSize(self.width(), self.height())
        self.timer_date = QtCore.QTimer()  # 定义显示状态栏日期时间定时器
        self.timer_camera = QtCore.QTimer()  # 定义定时器，用于控制显示视频的帧率
        self.cap = cv2.VideoCapture()  # 视频流
        self.camera_state = 0  # 摄像头开关状态
        self.jiequ_state = 0  # 截取图像是否为真
        self.CAM_NUM = 0  # 为0时表示视频流来自笔记本内置摄像头
        self.lock = threading.RLock()  # 定义一个Rlock对象
        self.max_len_contour = 0  # 定义轮廓直径最大值
        # self.flag_label_2_pic = 0  # 判断label_2(截图)是否显示图片，0为空，1显示
        self.filename = ""

        self.thresh = 100
        self.rho = 1
        self.theta = np.pi / 180
        self.threshold = 200
        self.minLineLength = 300
        self.maxLineGap = 200

        self.slot_init()

    "----------------------------主函数-------------------------"

    def slot_init(self):
        # self.toolButton_2.clicked.connect(self.caputer_picture)  # 拍摄源图按钮
        self.toolButton_2.clicked.connect(self.show_jiequ)  # 截取图像显示
        self.toolButton_10.clicked.connect(self.showMinimized)  # 最小化按钮
        # self.toolButton_11.clicked.connect(self.close)  # 退出按钮
        self.timer_date.timeout.connect(self.show_date)  # 显示状态栏时间槽函数连接
        self.timer_date.start()
        self.timer_camera.timeout.connect(self.show_camera)
        # self.center()  # 放置界面在屏幕中心

        '检测相机是否打开，并提示'
        if self.timer_camera.isActive() == False:  # 若定时器未启动
            self.flag = self.cap.open(self.CAM_NUM)  # 参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频
            if self.flag == False:  # flag表示open()成不成功
                # msg = QtWidgets.QMessageBox.warning(self, '提示', "请检查相机与电脑是否连接正确",
                #                                     buttons=QtWidgets.QMessageBox.Ok)
                self.camera_state = 0
                self.label.setText("请检查相机与电脑是否连接正确！")
            else:
                self.timer_camera.start(24)  # 定时器开始计时30ms，结果是每过30ms从摄像头中取一帧显示
                self.camera_state = 1
                self.toolButton.setText('关闭相机')

        '初始化显示零件标准图'
        show_biaozhun = cv2.imread("E:\\python\\shalun_position_detection\\pic_data\\lingjiantu.jpg")
        if show_biaozhun is None:
            self.label_6.setText("没有标准零件图！请在正确路径下存入，并命名为“lingjiantu.jpg”")
        else:
            showImage = self.show_image(show_biaozhun)
            showImage = showImage.scaled(self.label_6.width(), self.label_6.height(), Qt.KeepAspectRatio,
                                         Qt.SmoothTransformation)  # 按比例缩放
            self.label_6.setAlignment(Qt.AlignCenter)  # 居中显示
            self.label_6.setPixmap(QtGui.QPixmap.fromImage(showImage))

    # function 实时视频显示窗口
    def show_camera(self):
        t1 = threading.Thread(target=self.action_show_camera)
        t1.start()

    # function “打开/关闭相机”按钮功能
    @pyqtSlot()
    def on_toolButton_clicked(self):
        if self.timer_camera.isActive() == False:  # 若定时器未启动
            self.flag = self.cap.open(self.CAM_NUM)
            # 参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频
            if self.flag == False:  # flag表示open()成不成功
                msg = QtWidgets.QMessageBox.warning(self, '提示', "请检查相机与电脑是否连接正确",
                                                    buttons=QtWidgets.QMessageBox.Ok)
                self.label.setText("请检查相机与电脑是否连接正确！")
                self.camera_state = 0
            else:
                self.timer_camera.start(24)  # 定时器开始计时30ms，结果是每过30ms从摄像头中取一帧显示
                self.camera_state = 1
                self.toolButton.setText('关闭相机')
        else:
            self.timer_camera.stop()  # 关闭定时器
            self.cap.release()  # 释放视频流
            self.label.clear()  # 清空视频显示区域
            self.camera_state = 0
            self.toolButton.setText('打开相机')

    # function 截取图像
    def show_jiequ(self):
        if self.camera_state == 1:
            # self.label_2.clear()  # 清空视频显示区域
            cv2.imwrite("E:\\python\\shalun_position_detection\\pic_data\\wait_detection\\jiequ1.jpg", self.image)
            dialog = param2(self)
            result = dialog.exec_()
            if result == 1:
                # print(dialog.label.x0, dialog.label.y0, dialog.label.x1, dialog.label.y1)
                image = self.image[dialog.label.y0 * 3:dialog.label.y1 * 3, dialog.label.x0 * 3:dialog.label.x1 * 3]
                cv2.imwrite("E:\\python\\shalun_position_detection\\pic_data\\wait_detection\\jiequ2.jpg", image)
                showImage = self.show_image(image)
                showImage = showImage.scaled(self.label_2.width(), self.label_2.height(), Qt.KeepAspectRatio,
                                             Qt.SmoothTransformation)  # 按比例缩放
                self.label_2.setAlignment(Qt.AlignCenter)  # 居中显示
                self.label_2.setPixmap(QtGui.QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage
                self.jiequ_state = 1
                self.filename = ""  # 清空路径
            else:
                pass
            dialog.destroy()
        else:
            msg = QtWidgets.QMessageBox.warning(self, '提示', "请检查相机于电脑是否连接正确",
                                                buttons=QtWidgets.QMessageBox.Ok)

    # function 分析计算
    @pyqtSlot()
    def on_toolButton_4_clicked(self):
        if self.jiequ_state == 0:
            msg = QtWidgets.QMessageBox.warning(self, '提示', "截取图像为空，无法进行计算，请选取文件进行计算！",
                                                buttons=QtWidgets.QMessageBox.Ok)
        else:
            if self.filename == "":
                self.label_4.clear()
                self.label_3.clear()
                image = cv2.imread("E:\\python\\shalun_position_detection\\pic_data\\wait_detection\\jiequ2.jpg")
                flag_compute, image, zuobiao, self.max_len_contour = compute_contour(image, thresh=self.thresh,
                                                                                     rho=self.rho,
                                                                                     theta=self.theta,
                                                                                     threshold=self.threshold,
                                                                                     minLineLength=self.minLineLength,
                                                                                     maxLineGap=self.maxLineGap)
                if flag_compute == 1:
                    showImage = self.show_image(image)
                    showImage = showImage.scaled(self.label_4.width(), self.label_4.height(), Qt.KeepAspectRatio,
                                                 Qt.SmoothTransformation)  # 按比例缩放
                    self.label_4.setAlignment(Qt.AlignCenter)  # 居中显示
                    self.label_4.setPixmap(QtGui.QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage
                    '比对计算'
                    image1 = contour_interpolation(zuobiao)
                    showImage1 = self.show_image(image1)
                    showImage1 = showImage1.scaled(self.label_3.width(), self.label_3.height(), Qt.KeepAspectRatio,
                                                   Qt.SmoothTransformation)  # 按比例缩放
                    self.label_3.setAlignment(Qt.AlignCenter)  # 居中显示
                    self.label_3.setPixmap(QtGui.QPixmap.fromImage(showImage1))  # 往显示视频的Label里 显示QImage
                    self.label_29.setText(str(self.max_len_contour) + "mm")  # 将最大轮廓直径值填入label_29中
                    save_zuobiao_xiangdui_txt(
                        "E:/python/shalun_position_detection/pic_data/result_detection/zuobiao_xiangdui.txt",
                        zuobiao)  # 保存轮廓像素相对坐标
                    msg = QtWidgets.QMessageBox.warning(self, '提示', "计算结束！", buttons=QtWidgets.QMessageBox.Ok)
                elif flag_compute == 0:
                    msg = QtWidgets.QMessageBox.warning(self, '提示', "未识别出目标，请调整参数再次计算分析！",
                                                        buttons=QtWidgets.QMessageBox.Ok)
            else:
                self.label_4.clear()
                self.label_3.clear()
                image = cv2.imread(self.filename)
                # image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
                flag_compute, image, zuobiao, self.max_len_contour = compute_contour(image, thresh=self.thresh,
                                                                                     rho=self.rho,
                                                                                     theta=self.theta,
                                                                                     threshold=self.threshold,
                                                                                     minLineLength=self.minLineLength,
                                                                                     maxLineGap=self.maxLineGap)
                if flag_compute == 1:
                    showImage = self.show_image(image)
                    showImage = showImage.scaled(self.label_4.width(), self.label_4.height(), Qt.KeepAspectRatio,
                                                 Qt.SmoothTransformation)  # 按比例缩放
                    self.label_4.setAlignment(Qt.AlignCenter)  # 居中显示
                    self.label_4.setPixmap(QtGui.QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage
                    '比对计算'
                    image1 = contour_interpolation(zuobiao)
                    showImage1 = self.show_image(image1)
                    showImage1 = showImage1.scaled(self.label_3.width(), self.label_3.height(), Qt.KeepAspectRatio,
                                                   Qt.SmoothTransformation)  # 按比例缩放
                    self.label_3.setAlignment(Qt.AlignCenter)  # 居中显示
                    self.label_3.setPixmap(QtGui.QPixmap.fromImage(showImage1))  # 往显示视频的Label里 显示QImage
                    self.label_29.setText(str(self.max_len_contour) + "mm")  # 将最大轮廓直径值填入label_29中
                    save_zuobiao_xiangdui_txt(
                        "E:/python/shalun_position_detection/pic_data/result_detection/zuobiao_xiangdui.txt",
                        zuobiao)  # 保存轮廓像素相对坐标
                    msg = QtWidgets.QMessageBox.warning(self, '提示', "计算结束！", buttons=QtWidgets.QMessageBox.Ok)
                elif flag_compute == 0:
                    msg = QtWidgets.QMessageBox.warning(self, '提示', "未识别出目标，请调整参数再次计算分析！",
                                                        buttons=QtWidgets.QMessageBox.Ok)

    # function 打开文件(.jpg; .png; ...)
    @pyqtSlot()
    def on_toolButton_6_clicked(self):
        self.filename, filetype = QFileDialog.getOpenFileName(self, "选择图片", "./",
                                                              "IGPE (*.jpg);;GIF (*.GIF);;PNG (*.png);;ICO (*.ico)")
        if self.filename == "":
            pass
        else:
            self.label_2.clear()
            self.label_3.clear()
            self.label_4.clear()
            image = cv2.imread(self.filename)
            showImage = self.show_image(image)
            showImage = showImage.scaled(self.label_2.width(), self.label_2.height(), Qt.KeepAspectRatio,
                                         Qt.SmoothTransformation)  # 按比例缩放
            self.label_2.setAlignment(Qt.AlignCenter)  # 居中显示
            self.label_2.setPixmap(QtGui.QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage
            self.jiequ_state = 1

    # function 清除截图按钮
    @pyqtSlot()
    def on_toolButton_8_clicked(self):
        self.label_2.clear()
        self.label_3.clear()
        self.label_4.clear()
        self.jiequ_state = 0

    # function 退出程序按钮
    @pyqtSlot()
    def on_toolButton_11_clicked(self):
        self.cap.release()  # 释放视频流
        self.timer_camera.stop()
        self.close()

    # function 打开图像处理参数设置按钮
    @pyqtSlot()
    def on_toolButton_12_clicked(self):
        dialog = param1(self)
        result = dialog.exec_()
        if result == 1:
            self.thresh = eval(dialog.thresh_comboBox.currentText())
            self.rho = eval(dialog.rho_comboBox.currentText())
            self.theta = eval(dialog.theta_comboBox.currentText())
            self.threshold = eval(dialog.threshold_comboBox.currentText())
            self.minLineLength = eval(dialog.minLineLength_comboBox.currentText())
            self.maxLineGap = eval(dialog.maxLineGap_comboBox.currentText())
        else:
            pass
        dialog.destroy()

    # function 显示状态栏日期槽函数
    def show_date(self):
        now = QtCore.QDate.currentDate()
        time = QtCore.QTime.currentTime()
        self.label_15.setText(now.toString(QtCore.Qt.ISODate) + '  ' + time.toString(QtCore.Qt.DefaultLocaleLongDate))

    # function 放置界面在屏幕中心
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2 - 20)

    "------------------------功能型函数，用于减少代码量-----------------------"

    # function 定义显示图片功能函数
    def show_image(self, image):
        # image = cv2.resize(image, (self.picture_size_w, self.picture_size_h))  # 把读到的帧的大小重新设置为 640x480
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
        image = QtGui.QImage(image.data, image.shape[1], image.shape[0], image.shape[1] * 3,
                             QtGui.QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
        return image

    # function 实时显示图像多线程target函数
    def action_show_camera(self):
        self.lock.acquire()
        try:
            # self.cap.set(6, cv2.VideoWriter.fourcc('M', 'J', 'P', 'G'))
            self.cap.set(3, 2592)
            self.cap.set(4, 1944)
            flag, self.image = self.cap.read()  # 从视频流中读取
            if flag:
                show = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
                showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0],
                                         QtGui.QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
                showImage = showImage.scaled(self.label.width(), self.label.height(), Qt.KeepAspectRatio,
                                             Qt.SmoothTransformation)  # 按比例缩放
                self.label.setAlignment(Qt.AlignCenter)  # 居中显示
                self.label.setPixmap(QtGui.QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage
        finally:
            self.lock.release()


class param1(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(param1, self).__init__(parent)
        self.setupUi(self)

        self.thresh_comboBox.addItems(['90', '95', '100', '105', '110', '115', '120', '125'])
        self.thresh_comboBox.setCurrentIndex(2)
        self.rho_comboBox.addItems(['1', '2'])
        self.rho_comboBox.setCurrentIndex(0)
        self.theta_comboBox.addItems(['np.pi/180'])
        self.theta_comboBox.setCurrentIndex(0)
        self.threshold_comboBox.addItems(['150', '160', '170', '180', '190', '200', '210', '220', '230', '240', '250'])
        self.threshold_comboBox.setCurrentIndex(5)
        self.minLineLength_comboBox.addItems(
            ['250', '260', '270', '280', '290', '300', '310', '320', '330', '340', '350'])
        self.minLineLength_comboBox.setCurrentIndex(5)
        self.maxLineGap_comboBox.addItems(['150', '160', '170', '180', '190', '200', '210', '220', '230', '240', '250'])
        self.maxLineGap_comboBox.setCurrentIndex(5)


class param2(QtWidgets.QDialog, Ui_Dialog_jiequ):
    def __init__(self, parent=None):
        super(param2, self).__init__(parent)
        self.setupUi(self)

        self.label = MyLabel(self)
        self.label.setGeometry(QRect(20, 10, 864, 648))

        image = cv2.imread("E:\\python\\shalun_position_detection\\pic_data\\wait_detection\\jiequ1.jpg")
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
        showImage = QtGui.QImage(image.data, image.shape[1], image.shape[0], image.shape[1] * 3,
                                 QtGui.QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
        showImage = showImage.scaled(self.label.width(), self.label.height(), Qt.KeepAspectRatio,
                                     Qt.SmoothTransformation)  # 按比例缩放
        self.label.setAlignment(Qt.AlignCenter)  # 居中显示
        self.label.setPixmap(QtGui.QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage
        self.label.setCursor(Qt.CrossCursor)
        self.show()


if __name__ == '__main__':
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    app = QtWidgets.QApplication(sys.argv)
    window = MyMainWindow()
    window.showMaximized()
    sys.exit(app.exec_())
