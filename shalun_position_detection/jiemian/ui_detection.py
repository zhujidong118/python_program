# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_detection.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1040)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/my_pic/pic_data/icon/tubiao.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 70, 1091, 861))
        self.groupBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.groupBox.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.groupBox.setTitle("")
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 430, 531, 421))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setStyleSheet("color: rgb(255, 0, 0);")
        self.groupBox_7.setFlat(False)
        self.groupBox_7.setCheckable(False)
        self.groupBox_7.setObjectName("groupBox_7")
        self.label_3 = QtWidgets.QLabel(self.groupBox_7)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 512, 384))
        self.label_3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setMidLineWidth(0)
        self.label_3.setText("")
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setObjectName("label_3")
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_8.setGeometry(QtCore.QRect(550, 430, 531, 421))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setStyleSheet("color: rgb(255, 0, 0);")
        self.groupBox_8.setFlat(False)
        self.groupBox_8.setCheckable(False)
        self.groupBox_8.setObjectName("groupBox_8")
        self.label_4 = QtWidgets.QLabel(self.groupBox_8)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 512, 384))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_4.setMidLineWidth(0)
        self.label_4.setText("")
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setObjectName("label_4")
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 6, 531, 421))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.groupBox_9.setFont(font)
        self.groupBox_9.setMouseTracking(False)
        self.groupBox_9.setTabletTracking(False)
        self.groupBox_9.setAcceptDrops(False)
        self.groupBox_9.setAutoFillBackground(False)
        self.groupBox_9.setStyleSheet("color: rgb(255, 0, 0);")
        self.groupBox_9.setFlat(False)
        self.groupBox_9.setCheckable(False)
        self.groupBox_9.setObjectName("groupBox_9")
        self.label = QtWidgets.QLabel(self.groupBox_9)
        self.label.setGeometry(QtCore.QRect(10, 30, 512, 384))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(1)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.groupBox_10 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_10.setGeometry(QtCore.QRect(550, 6, 531, 421))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.groupBox_10.setFont(font)
        self.groupBox_10.setStyleSheet("color: rgb(255, 0, 0);")
        self.groupBox_10.setFlat(False)
        self.groupBox_10.setCheckable(False)
        self.groupBox_10.setObjectName("groupBox_10")
        self.label_2 = QtWidgets.QLabel(self.groupBox_10)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 512, 384))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(2, 0, 1611, 61))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.toolButton_5 = QtWidgets.QToolButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_5.setFont(font)
        self.toolButton_5.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.toolButton_5.setAutoFillBackground(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/my_pic/pic_data/icon/用户.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_5.setIcon(icon1)
        self.toolButton_5.setIconSize(QtCore.QSize(48, 36))
        self.toolButton_5.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_5.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton = QtWidgets.QToolButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton.setFont(font)
        self.toolButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.toolButton.setAutoFillBackground(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/my_pic/pic_data/icon/相机 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon2)
        self.toolButton.setIconSize(QtCore.QSize(48, 36))
        self.toolButton.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_2.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/my_pic/pic_data/icon/iconfont_剪刀.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon3)
        self.toolButton_2.setIconSize(QtCore.QSize(48, 36))
        self.toolButton_2.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_8 = QtWidgets.QToolButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_8.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/my_pic/pic_data/icon/清除.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_8.setIcon(icon4)
        self.toolButton_8.setIconSize(QtCore.QSize(48, 36))
        self.toolButton_8.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_8.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_8.setObjectName("toolButton_8")
        self.toolButton_4 = QtWidgets.QToolButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_4.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/my_pic/pic_data/icon/分析评比.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon5)
        self.toolButton_4.setIconSize(QtCore.QSize(48, 36))
        self.toolButton_4.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_3 = QtWidgets.QToolButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_3.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/my_pic/pic_data/icon/设备.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon6)
        self.toolButton_3.setIconSize(QtCore.QSize(48, 36))
        self.toolButton_3.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_12 = QtWidgets.QToolButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_12.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/my_pic/pic_data/icon/设置.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_12.setIcon(icon7)
        self.toolButton_12.setIconSize(QtCore.QSize(48, 36))
        self.toolButton_12.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_12.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_12.setObjectName("toolButton_12")
        self.toolButton_6 = QtWidgets.QToolButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_6.setFont(font)
        self.toolButton_6.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.toolButton_6.setAutoFillBackground(False)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/my_pic/pic_data/icon/4打开文件 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_6.setIcon(icon8)
        self.toolButton_6.setIconSize(QtCore.QSize(48, 36))
        self.toolButton_6.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_6.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_6.setObjectName("toolButton_6")
        self.toolButton_7 = QtWidgets.QToolButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_7.setFont(font)
        self.toolButton_7.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.toolButton_7.setAutoFillBackground(False)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/my_pic/pic_data/icon/保存.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_7.setIcon(icon9)
        self.toolButton_7.setIconSize(QtCore.QSize(48, 36))
        self.toolButton_7.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_7.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_7.setObjectName("toolButton_7")
        self.toolButton_10 = QtWidgets.QToolButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_10.setFont(font)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/my_pic/pic_data/icon/最小化0.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_10.setIcon(icon10)
        self.toolButton_10.setIconSize(QtCore.QSize(48, 36))
        self.toolButton_10.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_10.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_10.setObjectName("toolButton_10")
        self.toolButton_11 = QtWidgets.QToolButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_11.setFont(font)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/my_pic/pic_data/icon/退出.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_11.setIcon(icon11)
        self.toolButton_11.setIconSize(QtCore.QSize(48, 36))
        self.toolButton_11.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_11.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_11.setObjectName("toolButton_11")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QtCore.QRect(1098, 70, 821, 861))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_14 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_14.setGeometry(QtCore.QRect(0, 0, 421, 391))
        self.groupBox_14.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.groupBox_14.setTitle("")
        self.groupBox_14.setObjectName("groupBox_14")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_14)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 6, 401, 381))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setStyleSheet("color: rgb(255, 0, 0);")
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_6 = QtWidgets.QLabel(self.groupBox_6)
        self.label_6.setGeometry(QtCore.QRect(10, 30, 381, 341))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_6.setMidLineWidth(0)
        self.label_6.setText("")
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 400, 421, 461))
        self.groupBox_3.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_3)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 401, 431))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(12)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(153)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(430, 400, 391, 261))
        self.groupBox_4.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton.setGeometry(QtCore.QRect(50, 50, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 120, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_4.setGeometry(QtCore.QRect(210, 120, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_27 = QtWidgets.QLabel(self.groupBox_4)
        self.label_27.setGeometry(QtCore.QRect(90, 10, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_27.setFont(font)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_6.setGeometry(QtCore.QRect(210, 50, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 192, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_8.setGeometry(QtCore.QRect(210, 192, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.groupBox_15 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_15.setGeometry(QtCore.QRect(430, 0, 391, 391))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_15.setFont(font)
        self.groupBox_15.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.groupBox_15.setTitle("")
        self.groupBox_15.setObjectName("groupBox_15")
        self.groupBox_12 = QtWidgets.QGroupBox(self.groupBox_15)
        self.groupBox_12.setGeometry(QtCore.QRect(10, 6, 371, 381))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        self.groupBox_12.setFont(font)
        self.groupBox_12.setStyleSheet("color: rgb(255, 0, 0);")
        self.groupBox_12.setObjectName("groupBox_12")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_12)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 110, 291, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_29 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.gridLayout.addWidget(self.label_29, 0, 1, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.gridLayout.addWidget(self.label_31, 2, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 3, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 0, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 1, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 2, 0, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.gridLayout.addWidget(self.label_33, 4, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 4, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.gridLayout.addWidget(self.label_30, 1, 1, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_32.setFont(font)
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.gridLayout.addWidget(self.label_32, 3, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox_12)
        self.label_19.setGeometry(QtCore.QRect(110, 60, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_19.setObjectName("label_19")
        self.label_7 = QtWidgets.QLabel(self.groupBox_12)
        self.label_7.setGeometry(QtCore.QRect(200, 60, 54, 12))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_21 = QtWidgets.QLabel(self.groupBox_12)
        self.label_21.setGeometry(QtCore.QRect(84, 339, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_21.setObjectName("label_21")
        self.label_34 = QtWidgets.QLabel(self.groupBox_12)
        self.label_34.setGeometry(QtCore.QRect(210, 340, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_5.setGeometry(QtCore.QRect(430, 670, 391, 191))
        self.groupBox_5.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_28 = QtWidgets.QLabel(self.groupBox_5)
        self.label_28.setGeometry(QtCore.QRect(80, 40, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_28.setFont(font)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton.setGeometry(QtCore.QRect(70, 110, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_2.setGeometry(QtCore.QRect(220, 110, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.groupBox_11 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_11.setGeometry(QtCore.QRect(-10, 940, 1941, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_11.setFont(font)
        self.groupBox_11.setTitle("")
        self.groupBox_11.setObjectName("groupBox_11")
        self.label_15 = QtWidgets.QLabel(self.groupBox_11)
        self.label_15.setGeometry(QtCore.QRect(1690, 5, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setAcceptDrops(False)
        self.label_15.setAutoFillBackground(True)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_12 = QtWidgets.QLabel(self.groupBox_11)
        self.label_12.setGeometry(QtCore.QRect(1532, 5, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setAutoFillBackground(True)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_11)
        self.label_13.setGeometry(QtCore.QRect(1610, 5, 63, 20))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setAutoFillBackground(True)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_11)
        self.label_14.setGeometry(QtCore.QRect(30, 6, 1381, 20))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(11)
        self.label_14.setFont(font)
        self.label_14.setAutoFillBackground(True)
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "砂轮零件几何参数视觉检测系统"))
        self.groupBox_7.setTitle(_translate("MainWindow", "比对结果"))
        self.groupBox_8.setTitle(_translate("MainWindow", "分析结果"))
        self.groupBox_9.setTitle(_translate("MainWindow", "实时监控"))
        self.groupBox_10.setTitle(_translate("MainWindow", "截取图像"))
        self.toolButton_5.setText(_translate("MainWindow", "用户管理"))
        self.toolButton.setText(_translate("MainWindow", "打开相机"))
        self.toolButton_2.setText(_translate("MainWindow", "截取图像"))
        self.toolButton_8.setText(_translate("MainWindow", "清除截图"))
        self.toolButton_4.setText(_translate("MainWindow", "分析计算"))
        self.toolButton_3.setText(_translate("MainWindow", "运动台控制"))
        self.toolButton_12.setText(_translate("MainWindow", "设置参数"))
        self.toolButton_6.setText(_translate("MainWindow", "打开文件"))
        self.toolButton_7.setText(_translate("MainWindow", "保存文件"))
        self.toolButton_10.setText(_translate("MainWindow", "最 小 化"))
        self.toolButton_11.setText(_translate("MainWindow", "退出程序"))
        self.groupBox_6.setTitle(_translate("MainWindow", "标准图纸"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "11"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "13"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "零件编号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "最大轮廓误差"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "均值轮廓误差"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "是否合格"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "001"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "0.05mm"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "0.03mm"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "合格"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "开始检测"))
        self.pushButton_3.setText(_translate("MainWindow", "标准校正"))
        self.pushButton_4.setText(_translate("MainWindow", "轮廓拟合"))
        self.label_27.setText(_translate("MainWindow", "检测流程控制"))
        self.pushButton_6.setText(_translate("MainWindow", "检测节拍"))
        self.pushButton_5.setText(_translate("MainWindow", "运动台开启"))
        self.pushButton_8.setText(_translate("MainWindow", "运动台暂停"))
        self.groupBox_12.setTitle(_translate("MainWindow", "标准图纸"))
        self.label_29.setText(_translate("MainWindow", "0"))
        self.label_31.setText(_translate("MainWindow", "0"))
        self.label_25.setText(_translate("MainWindow", "最小误差值"))
        self.label_22.setText(_translate("MainWindow", "最大轮廓值"))
        self.label_23.setText(_translate("MainWindow", "最小轮廓值"))
        self.label_24.setText(_translate("MainWindow", "最大误差值"))
        self.label_33.setText(_translate("MainWindow", "0"))
        self.label_26.setText(_translate("MainWindow", "误差均值"))
        self.label_30.setText(_translate("MainWindow", "0"))
        self.label_32.setText(_translate("MainWindow", "0"))
        self.label_19.setText(_translate("MainWindow", "零件编码"))
        self.label_7.setText(_translate("MainWindow", "001"))
        self.label_21.setText(_translate("MainWindow", "检测结果是否合格"))
        self.label_34.setText(_translate("MainWindow", "合格"))
        self.label_28.setText(_translate("MainWindow", "检测模式控制"))
        self.radioButton.setText(_translate("MainWindow", "自动检测"))
        self.radioButton_2.setText(_translate("MainWindow", "手动检测"))
        self.label_15.setText(_translate("MainWindow", "2019-09-22  14：49：50"))
        self.label_12.setText(_translate("MainWindow", "当前用户："))
        self.label_13.setText(_translate("MainWindow", "admin"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "分析工具"))
        self.menu_3.setTitle(_translate("MainWindow", "视图"))
        self.menu_4.setTitle(_translate("MainWindow", "系统设置"))
        self.menu_5.setTitle(_translate("MainWindow", "帮助"))
import ui_detection_qrc_rc
