# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	Enums.py
# @Time		    	:	2020/2/1 20:06
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.1
from enum import IntEnum


class MessageDialogType(IntEnum):
    ABOUT = 1
    ASK = 2
    INFORMATION = 3
    WARNING = 4
    ERROR = 5
    SUCCESS = 6
    FAILS = 7
