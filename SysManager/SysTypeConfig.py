# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SysTypeConfig.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore
from Origin.Common.DB import DBCore


class Ui_sys_type_dialog(object):
    def __init__(self):
        self.db = DBCore()

    def setupUi(self, sys_type_dialog):
        sys_type_dialog.setObjectName("sys_type_dialog")
        sys_type_dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        sys_type_dialog.resize(1100, 700)
        sys_type_dialog.setMinimumSize(QtCore.QSize(1100, 700))
        sys_type_dialog.setMaximumSize(QtCore.QSize(1100, 700))
        sys_type_dialog.setBaseSize(QtCore.QSize(1100, 700))
        sys_type_dialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        sys_type_dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        sys_type_dialog.setSizeGripEnabled(False)
        sys_type_dialog.setModal(False)

        self.retranslateUi(sys_type_dialog)
        QtCore.QMetaObject.connectSlotsByName(sys_type_dialog)

    def retranslateUi(self, sys_type_dialog):
        _translate = QtCore.QCoreApplication.translate
        self.db.query(sql='SELECT VERSION()')
        sys_type_dialog.setWindowTitle(_translate("sys_type_dialog", "ATM 系统类型 设置界面 {}".format(self.db.data[0][0])))
