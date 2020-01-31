# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	SysTypeDao.py
# @Time		    	:	2020/1/16 19:36
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.0
from Origin.Model.Base import Base


class SysType(Base):
    def __init__(self, current_id=0, parent_id=-1, name=None, create_time=None, frozen=0, description=None):
        super().__init__('`SysType`', current_id, create_time, description)
        self.Name = name
        self.PID = parent_id
        self.Frozen = frozen

    def __eq__(self, other):
        return False if not isinstance(other, SysType) \
            else super().__eq__(other) \
            and self.Name == other.Name and self.PID == other.PID and self.Frozen == other.Frozen
