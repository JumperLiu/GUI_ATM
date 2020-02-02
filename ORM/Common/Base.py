# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	Base.py
# @Time		    	:	2020/1/31 19:57
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.1
from ORM.Core.CPU import CPU
from ORM.Common.Enums import *
from ORM.Common.Utils import Utils
from ORM.Models.Personnel import Personnel
from PyQt5 import QtCore, QtWidgets
from SysManager.CustomMessageDialog import Ui_CustomMessageDialog


def msg(msg_type: MessageDialogType, title: str, content: str, buttons: ButtonListType, **buttons_label):
    d = QtWidgets.QDialog()
    cmd = Ui_CustomMessageDialog()
    cmd.setupUi(d)
    d.setWindowModality(QtCore.Qt.ApplicationModal)
    d.exec_()


class Base:
    def __init__(self):
        super().__init__()
        self.Tools = Utils()
        self.DB = None

    def login(self, name: str = None, password: str = None) -> Personnel:
        self.DB = CPU(Personnel)
        login_users = self.DB.query_all("WHERE LoginName='{}' AND LoginPassword='{}' AND Valid=1".format(
            name, self.Tools.encrypt(password)))
        del self.DB
        return None if len(login_users) == 0 else login_users[0]
