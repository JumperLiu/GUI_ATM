# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	ControlType.py
# @Time		    	:	2020/1/30 11:43
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.1
from enum import IntEnum


class ControlType(IntEnum):
    """
    数据库操作枚举类型：QUERY - 查询操作； INSERT - 新增操作； UPDATE - 更新操作； DELETE - 删除操作
    """
    QUERY = 1
    INSERT = 2
    UPDATE = 3
    DELETE = 4
