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
from PyQt5.QtCore import Qt
from SysManager.Custom.IQMMsgDialog import IQMMsgDialog
from SysManager.Custom.IQMsgDialog import Ui_IQMsgDialog


def msg(msg_type: MessageDialogType, title: str, title_page: str, content: str,
        buttons: ButtonListType = ButtonListType.OK, l_bt_label: str = '提交',
        l_bt_tip=None, c_bt_label: str = '重置',  c_bt_tip=None,
        r_bt_label: str = '取消', r_bt_tip=None, elapse: float = 3.0) -> ResultType:
    msg_dialog = IQMMsgDialog()
    ui = Ui_IQMsgDialog()
    ui.setupUi(msg_dialog, msg_type, title, title_page, content, buttons, l_bt_label, l_bt_tip, c_bt_label, c_bt_tip,
               r_bt_label, r_bt_tip, elapse)
    msg_dialog.setWindowModality(Qt.ApplicationModal)
    msg_dialog.exec_()
    return ui.returnClickButton


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
