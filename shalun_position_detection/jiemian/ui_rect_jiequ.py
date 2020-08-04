# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_rect_jiequ.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_jiequ(object):
    def setupUi(self, Dialog_jiequ):
        Dialog_jiequ.setObjectName("Dialog_jiequ")
        Dialog_jiequ.resize(900, 700)
        Dialog_jiequ.setMinimumSize(QtCore.QSize(900, 700))
        Dialog_jiequ.setMaximumSize(QtCore.QSize(900, 700))
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_jiequ)
        self.buttonBox.setGeometry(QtCore.QRect(690, 664, 191, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog_jiequ)
        self.buttonBox.accepted.connect(Dialog_jiequ.accept)
        self.buttonBox.rejected.connect(Dialog_jiequ.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_jiequ)

    def retranslateUi(self, Dialog_jiequ):
        _translate = QtCore.QCoreApplication.translate
        Dialog_jiequ.setWindowTitle(_translate("Dialog_jiequ", "选择矩形区域"))
