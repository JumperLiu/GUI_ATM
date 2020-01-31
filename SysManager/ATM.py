# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ATM.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from SysManager import SysTypeConfig


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 680)
        MainWindow.setMinimumSize(QtCore.QSize(900, 680))
        MainWindow.setMaximumSize(QtCore.QSize(900, 680))
        MainWindow.setBaseSize(QtCore.QSize(900, 680))
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 901, 121))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.sys_type_pbt = QtWidgets.QPushButton(self.centralwidget)
        self.sys_type_pbt.setGeometry(QtCore.QRect(60, 130, 160, 36))
        self.sys_type_pbt.setMinimumSize(QtCore.QSize(160, 36))
        self.sys_type_pbt.setMaximumSize(QtCore.QSize(160, 36))
        self.sys_type_pbt.setBaseSize(QtCore.QSize(160, 36))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.sys_type_pbt.setFont(font)
        self.sys_type_pbt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sys_type_pbt.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sys_type_pbt.setObjectName("sys_type_pbt")
        self.sys_type_pbt.clicked.connect(self.openSysTypeConfig)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ATM - 模拟界面"))
        self.label.setText(_translate("MainWindow", "欢迎使用 ATM 模拟系统"))
        self.sys_type_pbt.setText(_translate("MainWindow", "系统类型设置"))

    def openSysTypeConfig(self):
        d = QtWidgets.QDialog()
        ui = SysTypeConfig.Ui_sys_type_dialog()
        ui.setupUi(d)
        d.setWindowModality(QtCore.Qt.ApplicationModal)
        d.exec_()
