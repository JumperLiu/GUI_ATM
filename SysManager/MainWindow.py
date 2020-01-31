# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from ORM.Core.CPU import CPU
from ORM.Common.Base import Base


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 480))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 600))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, "
                                 "stop:0 rgba(44, 0, 255, 252), stop:1 rgba(0, 170, 127, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 480))
        self.centralwidget.setMaximumSize(QtCore.QSize(1200, 720))
        self.centralwidget.setSizeIncrement(QtCore.QSize(10, 6))
        self.centralwidget.setBaseSize(QtCore.QSize(800, 480))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.centralwidget.setFont(font)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 781, 461))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(12)
        self.gridLayout.setObjectName("gridLayout")
        self.VLO_Main = QtWidgets.QVBoxLayout()
        self.VLO_Main.setSpacing(6)
        self.VLO_Main.setObjectName("VLO_Main")
        self.HLO_Welcome = QtWidgets.QHBoxLayout()
        self.HLO_Welcome.setSpacing(6)
        self.HLO_Welcome.setObjectName("HLO_Welcome")
        self.LBL_Welcome = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.LBL_Welcome.setFont(font)
        self.LBL_Welcome.setStyleSheet("background-color: rgba(255, 255, 255, 0);color: rgb(255, 255, 0);")
        self.LBL_Welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.LBL_Welcome.setObjectName("LBL_Welcome")
        self.HLO_Welcome.addWidget(self.LBL_Welcome)
        self.VLO_Main.addLayout(self.HLO_Welcome)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.VLO_Main.addItem(spacerItem)
        self.HLO_LoginName = QtWidgets.QHBoxLayout()
        self.HLO_LoginName.setSpacing(6)
        self.HLO_LoginName.setObjectName("HLO_LoginName")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HLO_LoginName.addItem(spacerItem1)
        self.LBL_LoginName = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LBL_LoginName.setFont(font)
        self.LBL_LoginName.setStyleSheet("color: rgb(85, 255, 255);background-color: rgba(255, 255, 255, 0);")
        self.LBL_LoginName.setAlignment(QtCore.Qt.AlignCenter)
        self.LBL_LoginName.setObjectName("LBL_LoginName")
        self.HLO_LoginName.addWidget(self.LBL_LoginName)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HLO_LoginName.addItem(spacerItem2)
        self.LE_LoginName = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.LE_LoginName.setMinimumSize(QtCore.QSize(420, 38))
        self.LE_LoginName.setMaximumSize(QtCore.QSize(420, 38))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.LE_LoginName.setFont(font)
        self.LE_LoginName.setStyleSheet("background-color: rgba(255, 255, 255, 0);border-color: rgb(255, 255, 255);"
                                        "color: rgb(255, 255, 0);")
        self.LE_LoginName.setMaxLength(20)
        self.LE_LoginName.setAlignment(QtCore.Qt.AlignCenter)
        self.LE_LoginName.setObjectName("LE_LoginName")
        self.HLO_LoginName.addWidget(self.LE_LoginName)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HLO_LoginName.addItem(spacerItem3)
        self.VLO_Main.addLayout(self.HLO_LoginName)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.VLO_Main.addItem(spacerItem4)
        self.HLO_LoginPassword = QtWidgets.QHBoxLayout()
        self.HLO_LoginPassword.setSpacing(6)
        self.HLO_LoginPassword.setObjectName("HLO_LoginPassword")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HLO_LoginPassword.addItem(spacerItem5)
        self.LBL_LoginPassword = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LBL_LoginPassword.setFont(font)
        self.LBL_LoginPassword.setStyleSheet("color: rgb(85, 255, 255);"
                                             "background-color: rgba(255, 255, 255, 0);")
        self.LBL_LoginPassword.setObjectName("LBL_LoginPassword")
        self.HLO_LoginPassword.addWidget(self.LBL_LoginPassword)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HLO_LoginPassword.addItem(spacerItem6)
        self.LE_LoginPassword = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.LE_LoginPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LE_LoginPassword.setMinimumSize(QtCore.QSize(420, 38))
        self.LE_LoginPassword.setMaximumSize(QtCore.QSize(420, 38))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.LE_LoginPassword.setFont(font)
        self.LE_LoginPassword.setStyleSheet("background-color: rgba(255, 255, 255, 0);"
                                            "border-color: rgb(255, 255, 255);color: rgb(255, 255, 0);")
        self.LE_LoginPassword.setMaxLength(12)
        self.LE_LoginPassword.setAlignment(QtCore.Qt.AlignCenter)
        self.LE_LoginPassword.setObjectName("LE_LoginPassword")
        self.HLO_LoginPassword.addWidget(self.LE_LoginPassword)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HLO_LoginPassword.addItem(spacerItem7)
        self.VLO_Main.addLayout(self.HLO_LoginPassword)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.VLO_Main.addItem(spacerItem8)
        self.HLO_Button = QtWidgets.QHBoxLayout()
        self.HLO_Button.setSpacing(6)
        self.HLO_Button.setObjectName("HLO_Button")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HLO_Button.addItem(spacerItem9)
        self.PBTN_Submit = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PBTN_Submit.setFont(font)
        self.PBTN_Submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PBTN_Submit.setStyleSheet("background-color: rgba(255, 255, 255, 0);"
                                       "color: rgb(0, 255, 0);border-color: rgb(255, 255, 255);"
                                       "alternate-background-color: rgb(255, 255, 0);")
        self.PBTN_Submit.setObjectName("PBTN_Submit")
        self.PBTN_Submit.clicked.connect(self.submitLoginLE)
        self.HLO_Button.addWidget(self.PBTN_Submit)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HLO_Button.addItem(spacerItem10)
        self.PBTN_Reset = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PBTN_Reset.setFont(font)
        self.PBTN_Reset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PBTN_Reset.setStyleSheet("color: rgb(255, 0, 0);background-color: rgba(255, 255, 255, 0);"
                                      "alternate-background-color: rgb(255, 255, 0);")
        self.PBTN_Reset.setObjectName("PBTN_Reset")
        self.PBTN_Reset.clicked.connect(self.resetLoginLE)
        self.HLO_Button.addWidget(self.PBTN_Reset)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HLO_Button.addItem(spacerItem11)
        self.VLO_Main.addLayout(self.HLO_Button)
        self.gridLayout.addLayout(self.VLO_Main, 2, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem12, 3, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem13, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "银行 ATM 柜员机模拟程序"))
        self.LBL_Welcome.setText(_translate("MainWindow", "欢迎使用 银行 ATM 自动柜员机"))
        self.LBL_LoginName.setText(_translate("MainWindow", "登录名称 ："))
        self.LBL_LoginPassword.setText(_translate("MainWindow", "登录密码 ："))
        self.PBTN_Submit.setText(_translate("MainWindow", "登 录"))
        self.PBTN_Reset.setText(_translate("MainWindow", "重 置"))

    def resetLoginLE(self):
        self.LE_LoginName.clear()
        self.LE_LoginPassword.clear()
        self.LE_LoginName.setFocus()

    def submitLoginLE(self):
        login_name = self.LE_LoginName.text().strip()
        login_password = self.LE_LoginPassword.text().strip()
        if len(login_name) == 0:
            QtWidgets.QMessageBox.warning(self.PBTN_Submit, "登录信息校验异常信息提示", "注意：您尚未填写 【 登录名称 】 信息……",
                                          QtWidgets.QMessageBox.Ok)
        elif len(login_password) == 0:
            QtWidgets.QMessageBox.warning(self.PBTN_Submit, "登录信息校验异常信息提示", "注意：您尚未填写 【 登录密码 】 信息……",
                                          QtWidgets.QMessageBox.Ok)
        else:
            login_user = Base().login(login_name, login_password)
            if login_user is None:
                ask = QtWidgets.QMessageBox.critical(self.PBTN_Submit, '登录信息校验异常信息提示',
                                                     '抱歉：您输入的 【 登录名称 或 登录密码 】 有误，是否重新输入登录信息？',
                                                     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                if ask == QtWidgets.QMessageBox.Yes:
                    self.resetLoginLE()
            else:
                QtWidgets.QMessageBox.about(self.PBTN_Submit, '登录成功信息提示', '恭喜：您已成功登录银行 ATM 系统！')
