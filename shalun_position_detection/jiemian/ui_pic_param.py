# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_pic_param.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(383, 484)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(190, 440, 131, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 50, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 80, 271, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.thresh_comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.thresh_comboBox.setObjectName("thresh_comboBox")
        self.horizontalLayout.addWidget(self.thresh_comboBox)
        self.layoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_3.setGeometry(QtCore.QRect(60, 190, 271, 221))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1)
        self.rho_comboBox = QtWidgets.QComboBox(self.layoutWidget_3)
        self.rho_comboBox.setObjectName("rho_comboBox")
        self.gridLayout.addWidget(self.rho_comboBox, 0, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 1, 0, 1, 1)
        self.theta_comboBox = QtWidgets.QComboBox(self.layoutWidget_3)
        self.theta_comboBox.setObjectName("theta_comboBox")
        self.gridLayout.addWidget(self.theta_comboBox, 1, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 2, 0, 1, 1)
        self.threshold_comboBox = QtWidgets.QComboBox(self.layoutWidget_3)
        self.threshold_comboBox.setObjectName("threshold_comboBox")
        self.gridLayout.addWidget(self.threshold_comboBox, 2, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 3, 0, 1, 1)
        self.minLineLength_comboBox = QtWidgets.QComboBox(self.layoutWidget_3)
        self.minLineLength_comboBox.setObjectName("minLineLength_comboBox")
        self.gridLayout.addWidget(self.minLineLength_comboBox, 3, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 4, 0, 1, 1)
        self.maxLineGap_comboBox = QtWidgets.QComboBox(self.layoutWidget_3)
        self.maxLineGap_comboBox.setObjectName("maxLineGap_comboBox")
        self.gridLayout.addWidget(self.maxLineGap_comboBox, 4, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(30, 150, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "图像处理参数设置"))
        self.label_6.setText(_translate("Dialog", "二值化"))
        self.label_8.setText(_translate("Dialog", "threshold"))
        self.label_10.setText(_translate("Dialog", "rho"))
        self.label_14.setText(_translate("Dialog", "theta"))
        self.label_16.setText(_translate("Dialog", "threshold"))
        self.label_17.setText(_translate("Dialog", "minLineLength"))
        self.label_18.setText(_translate("Dialog", "maxLineGap"))
        self.label_7.setText(_translate("Dialog", "霍夫直线检测"))
