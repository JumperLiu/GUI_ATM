# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/Sys_Manager/IQMsgDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtGui, QtWidgets
from ORM.Common.Enums import *
from ORM.Common.Styles import *
from SysManager.Images_res_rc import *
from SysManager.Custom.IQLabel import IQLabel


class Ui_IQMsgDialog(object):
    def __init__(self):
        super().__init__()
        self.buttonType = ButtonListType.OK
        self.returnClickButton = ResultType.CANCEL

    def setupUi(self, IQMsgDialog, msg_type: MessageDialogType, title: str, title_page: str, content: str,
                buttons: ButtonListType, l_bt_label: str = '提交', l_bt_tip=None,
                c_bt_label: str = '重置', c_bt_tip=None,
                r_bt_label: str = '取消', r_bt_tip=None):
        self.buttonType = buttons
        IQMsgDialog.setObjectName("IQMsgDialog")
        IQMsgDialog.resize(800, 480)
        IQMsgDialog.setMinimumSize(QtCore.QSize(800, 480))
        IQMsgDialog.setMaximumSize(QtCore.QSize(800, 480))
        IQMsgDialog.setMouseTracking(True)
        IQMsgDialog.setAutoFillBackground(False)
        IQMsgDialog.setStyleSheet(dialog_background_style(msg_type))
        IQMsgDialog.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowMinMaxButtonsHint |
                                   QtCore.Qt.MSWindowsFixedSizeDialogHint | QtCore.Qt.WindowCloseButtonHint)
        self.gridLayoutWidget = QtWidgets.QWidget(IQMsgDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 9, 801, 461))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.HLO_03_Content = QtWidgets.QHBoxLayout()
        self.HLO_03_Content.setSpacing(6)
        self.HLO_03_Content.setObjectName("HLO_03_Content")
        spacerItem = QtWidgets.QSpacerItem(20, 260, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HLO_03_Content.addItem(spacerItem)
        self.VLO_03_Content = QtWidgets.QVBoxLayout()
        self.VLO_03_Content.setSpacing(6)
        self.VLO_03_Content.setObjectName("VLO_03_Content")
        self.LBL_03_Content_Image = QtWidgets.QLabel(self.gridLayoutWidget)
        self.LBL_03_Content_Image.setMinimumSize(QtCore.QSize(96, 96))
        self.LBL_03_Content_Image.setMaximumSize(QtCore.QSize(96, 96))
        self.LBL_03_Content_Image.setBaseSize(QtCore.QSize(96, 96))
        self.LBL_03_Content_Image.setScaledContents(True)
        self.LBL_03_Content_Image.setAlignment(QtCore.Qt.AlignCenter)
        self.LBL_03_Content_Image.setObjectName("LBL_03_Content_Image")
        self.LBL_03_Content_Image.setPixmap(msg_image(msg_type))
        self.LBL_03_Content_Image.setStyleSheet(transparent_label_style())
        self.VLO_03_Content.addWidget(self.LBL_03_Content_Image)
        spacerItem1 = QtWidgets.QSpacerItem(96, 152, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.VLO_03_Content.addItem(spacerItem1)
        self.HLO_03_Content.addLayout(self.VLO_03_Content)
        spacerItem2 = QtWidgets.QSpacerItem(60, 260, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HLO_03_Content.addItem(spacerItem2)
        self.LBL_03_Content_Main_Content = QtWidgets.QLabel(self.gridLayoutWidget)
        self.LBL_03_Content_Main_Content.setMinimumSize(QtCore.QSize(592, 248))
        self.LBL_03_Content_Main_Content.setMaximumSize(QtCore.QSize(592, 248))
        self.LBL_03_Content_Main_Content.setBaseSize(QtCore.QSize(592, 248))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.LBL_03_Content_Main_Content.setFont(font)
        self.LBL_03_Content_Main_Content.setWordWrap(True)
        self.LBL_03_Content_Main_Content.setOpenExternalLinks(False)
        self.LBL_03_Content_Main_Content.setObjectName("LBL_03_Content_Main_Content")
        self.LBL_03_Content_Main_Content.setStyleSheet(msg_content_style())
        self.HLO_03_Content.addWidget(self.LBL_03_Content_Main_Content)
        spacerItem3 = QtWidgets.QSpacerItem(20, 260, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HLO_03_Content.addItem(spacerItem3)
        self.gridLayout.addLayout(self.HLO_03_Content, 2, 0, 1, 1)
        self.HLO_04_Button = QtWidgets.QHBoxLayout()
        self.HLO_04_Button.setSpacing(6)
        self.HLO_04_Button.setObjectName("HLO_04_Button")
        spacerItem4 = QtWidgets.QSpacerItem(190, 60, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HLO_04_Button.addItem(spacerItem4)
        self.PBTN_Submit = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PBTN_Submit.setFont(font)
        self.PBTN_Submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PBTN_Submit.setMouseTracking(True)
        self.PBTN_Submit.setObjectName("PBTN_Submit")
        self.PBTN_Submit.setStyleSheet(msg_submit_style())
        self.HLO_04_Button.addWidget(self.PBTN_Submit)
        spacerItem5 = QtWidgets.QSpacerItem(80, 60, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HLO_04_Button.addItem(spacerItem5)
        self.PBTN_Reset = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PBTN_Reset.setFont(font)
        self.PBTN_Reset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PBTN_Reset.setMouseTracking(True)
        self.PBTN_Reset.setObjectName("PBTN_Reset")
        self.PBTN_Reset.setStyleSheet(msg_reset_style())
        self.HLO_04_Button.addWidget(self.PBTN_Reset)
        spacerItem6 = QtWidgets.QSpacerItem(80, 60, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HLO_04_Button.addItem(spacerItem6)
        self.PBTN_Cancel = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PBTN_Cancel.setFont(font)
        self.PBTN_Cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PBTN_Cancel.setMouseTracking(True)
        self.PBTN_Cancel.setObjectName("PBTN_Cancel")
        self.PBTN_Cancel.setStyleSheet(msg_cancel_style())
        self.HLO_04_Button.addWidget(self.PBTN_Cancel)
        spacerItem7 = QtWidgets.QSpacerItem(190, 60, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HLO_04_Button.addItem(spacerItem7)
        self.gridLayout.addLayout(self.HLO_04_Button, 3, 0, 1, 1)
        self.HLO_02_Title = QtWidgets.QHBoxLayout()
        self.HLO_02_Title.setObjectName("HLO_02_Title")
        spacerItem8 = QtWidgets.QSpacerItem(40, 68, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HLO_02_Title.addItem(spacerItem8)
        self.LBL_02_Title_Title = QtWidgets.QLabel(self.gridLayoutWidget)
        self.LBL_02_Title_Title.setMaximumSize(QtCore.QSize(16777215, 68))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.LBL_02_Title_Title.setFont(font)
        self.LBL_02_Title_Title.setScaledContents(True)
        self.LBL_02_Title_Title.setAlignment(QtCore.Qt.AlignCenter)
        self.LBL_02_Title_Title.setObjectName("LBL_02_Title_Title")
        self.LBL_02_Title_Title.setStyleSheet(msg_title_style())
        self.HLO_02_Title.addWidget(self.LBL_02_Title_Title)
        spacerItem9 = QtWidgets.QSpacerItem(40, 68, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HLO_02_Title.addItem(spacerItem9)
        self.gridLayout.addLayout(self.HLO_02_Title, 1, 0, 1, 1)
        self.HLO_01_Head = QtWidgets.QHBoxLayout()
        self.HLO_01_Head.setSpacing(6)
        self.HLO_01_Head.setObjectName("HLO_01_Head")
        spacerItem10 = QtWidgets.QSpacerItem(10, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HLO_01_Head.addItem(spacerItem10)
        self.LBL_01_Head_Icon = IQLabel(self.gridLayoutWidget)
        self.LBL_01_Head_Icon.setMinimumSize(QtCore.QSize(40, 40))
        self.LBL_01_Head_Icon.setMaximumSize(QtCore.QSize(40, 40))
        self.LBL_01_Head_Icon.setBaseSize(QtCore.QSize(40, 40))
        self.LBL_01_Head_Icon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LBL_01_Head_Icon.setMouseTracking(True)
        self.LBL_01_Head_Icon.setText("")
        self.LBL_01_Head_Icon.setScaledContents(True)
        self.LBL_01_Head_Icon.setAlignment(QtCore.Qt.AlignCenter)
        self.LBL_01_Head_Icon.setObjectName("LBL_01_Head_Icon")
        self.LBL_01_Head_Icon.formatExt = 'png'
        self.LBL_01_Head_Icon.normalImage = 'icon_normal_01'
        self.LBL_01_Head_Icon.hoverImage = 'icon_hover_01'
        self.LBL_01_Head_Icon.hoverToolTip = 'Author : Cynosure0313@live.cn'
        self.LBL_01_Head_Icon.setNormalImage()
        self.LBL_01_Head_Icon.ME_Signal.connect(self.LBL_01_Head_Icon.setHoverImage)
        self.LBL_01_Head_Icon.ML_Signal.connect(self.LBL_01_Head_Icon.setNormalImage)
        self.LBL_01_Head_Icon.setStyleSheet(transparent_label_style())
        self.HLO_01_Head.addWidget(self.LBL_01_Head_Icon)
        spacerItem11 = QtWidgets.QSpacerItem(15, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HLO_01_Head.addItem(spacerItem11)
        self.LBL_01_Head_Title = QtWidgets.QLabel(self.gridLayoutWidget)
        self.LBL_01_Head_Title.setMinimumSize(QtCore.QSize(572, 40))
        self.LBL_01_Head_Title.setMaximumSize(QtCore.QSize(700, 40))
        self.LBL_01_Head_Title.setBaseSize(QtCore.QSize(572, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.LBL_01_Head_Title.setFont(font)
        self.LBL_01_Head_Title.setObjectName("LBL_01_Head_Title")
        self.LBL_01_Head_Title.setStyleSheet(msg_head_style())
        self.HLO_01_Head.addWidget(self.LBL_01_Head_Title)
        spacerItem12 = QtWidgets.QSpacerItem(15, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HLO_01_Head.addItem(spacerItem12)
        # self.LBL_01_Head_Min_Zoom = IQLabel(self.gridLayoutWidget)
        # self.LBL_01_Head_Min_Zoom.setMinimumSize(QtCore.QSize(40, 40))
        # self.LBL_01_Head_Min_Zoom.setMaximumSize(QtCore.QSize(40, 40))
        # self.LBL_01_Head_Min_Zoom.setBaseSize(QtCore.QSize(40, 40))
        # self.LBL_01_Head_Min_Zoom.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.LBL_01_Head_Min_Zoom.setMouseTracking(True)
        # self.LBL_01_Head_Min_Zoom.setText("")
        # self.LBL_01_Head_Min_Zoom.setScaledContents(True)
        # self.LBL_01_Head_Min_Zoom.setAlignment(QtCore.Qt.AlignCenter)
        # self.LBL_01_Head_Min_Zoom.setObjectName("LBL_01_Head_Min_Zoom")
        # self.HLO_01_Head.addWidget(self.LBL_01_Head_Min_Zoom)
        # spacerItem13 = QtWidgets.QSpacerItem(10, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.HLO_01_Head.addItem(spacerItem13)
        # self.LBL_01_Head_Shutdown = QtWidgets.QLabel(self.gridLayoutWidget)
        # self.LBL_01_Head_Shutdown.setMinimumSize(QtCore.QSize(40, 40))
        # self.LBL_01_Head_Shutdown.setMaximumSize(QtCore.QSize(40, 40))
        # self.LBL_01_Head_Shutdown.setBaseSize(QtCore.QSize(40, 40))
        # self.LBL_01_Head_Shutdown.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.LBL_01_Head_Shutdown.setMouseTracking(True)
        # self.LBL_01_Head_Shutdown.setText("")
        # self.LBL_01_Head_Shutdown.setScaledContents(True)
        # self.LBL_01_Head_Shutdown.setAlignment(QtCore.Qt.AlignCenter)
        # self.LBL_01_Head_Shutdown.setObjectName("LBL_01_Head_Shutdown")
        # self.HLO_01_Head.addWidget(self.LBL_01_Head_Shutdown)
        # spacerItem14 = QtWidgets.QSpacerItem(10, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.HLO_01_Head.addItem(spacerItem14)
        self.gridLayout.addLayout(self.HLO_01_Head, 0, 0, 1, 1)
        # 设置界面背景为透明
        IQMsgDialog.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # 设置当前窗体透明度为98%
        IQMsgDialog.setWindowOpacity(0.98)
        self.gridLayoutWidget.setStyleSheet(dialog_background_style(msg_type))
        self.gridLayoutWidget.setWindowOpacity(0.98)

        self.retranslateUi(IQMsgDialog, title, title_page, content, buttons, l_bt_label, l_bt_tip, c_bt_label, c_bt_tip,
                           r_bt_label, r_bt_tip)
        QtCore.QMetaObject.connectSlotsByName(IQMsgDialog)

    def retranslateUi(self, IQMsgDialog, title: str, title_page: str, content: str, bts: ButtonListType,
                      l_bt_label: str = '提交', l_bt_tip=None, c_bt_label: str = '重置', c_bt_tip=None,
                      r_bt_label: str = '取消', r_bt_tip=None):
        _translate = QtCore.QCoreApplication.translate
        IQMsgDialog.setWindowTitle(_translate("IQMsgDialog", title))
        self.LBL_01_Head_Title.setText(_translate("IQMsgDialog", title))
        self.LBL_02_Title_Title.setText(_translate("IQMsgDialog", title_page))
        self.LBL_03_Content_Main_Content.setText(_translate("IQMsgDialog", content))
        self.PBTN_Submit.setVisible(False)
        self.PBTN_Submit.setEnabled(False)
        self.PBTN_Reset.setVisible(False)
        self.PBTN_Reset.setEnabled(False)
        self.PBTN_Cancel.setVisible(False)
        self.PBTN_Cancel.setEnabled(False)
        if bts == ButtonListType.YESNO or bts == ButtonListType.OKCANCEL or bts == ButtonListType.YESNOCANCEL:
            self.PBTN_Submit.setText(_translate("IQMsgDialog", l_bt_label))
            if l_bt_tip is not None:
                self.PBTN_Submit.setToolTip(l_bt_tip)
            self.PBTN_Submit.setVisible(True)
            self.PBTN_Submit.setEnabled(True)
            self.PBTN_Submit.clicked.connect(self.left_button_clicked)
        if bts == ButtonListType.OK or bts == ButtonListType.YESNOCANCEL:
            self.PBTN_Reset.setText(_translate("IQMsgDialog", c_bt_label))
            if c_bt_tip is not None:
                self.PBTN_Reset.setToolTip(c_bt_tip)
            self.PBTN_Reset.setVisible(True)
            self.PBTN_Reset.setEnabled(True)
            self.PBTN_Reset.clicked.connect(self.center_button_clicked)
        if bts == ButtonListType.YESNO or bts == ButtonListType.OKCANCEL or bts == ButtonListType.YESNOCANCEL:
            self.PBTN_Cancel.setText(_translate("IQMsgDialog", r_bt_label))
            if r_bt_tip is not None:
                self.PBTN_Cancel.setToolTip(r_bt_tip)
            self.PBTN_Cancel.setVisible(True)
            self.PBTN_Cancel.setEnabled(True)
            self.PBTN_Cancel.clicked.connect(self.right_button_clicked)

    def left_button_clicked(self):
        if self.buttonType == (ButtonListType.YESNO or ButtonListType.YESNOCANCEL):
            self.returnClickButton = ResultType.YES
        elif self.buttonType == ButtonListType.OKCANCEL:
            self.returnClickButton = ResultType.OK
        self.gridLayoutWidget.parent().close()

    def center_button_clicked(self):
        if self.buttonType == ButtonListType.OK:
            self.returnClickButton = ResultType.OK
        elif self.buttonType == ButtonListType.YESNOCANCEL:
            self.returnClickButton = ResultType.NO
        self.gridLayoutWidget.parent().close()

    def right_button_clicked(self):
        if self.buttonType == ButtonListType.YESNO:
            self.returnClickButton = ResultType.NO
        elif self.buttonType == (ButtonListType.OKCANCEL or ButtonListType.YESNOCANCEL):
            self.returnClickButton = ResultType.CANCEL
        self.gridLayoutWidget.parent().close()

