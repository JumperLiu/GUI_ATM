# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	SysState.py
# @Time		    	:	2020/1/16 20:07
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.0
from Origin.Model.Base import Base


class SysState(Base):
    def __init__(self, current_id=0, sys_type_id=0, name=None, create_time=None, frozen=0, description=None):
        super().__init__('`SysState`', current_id, create_time, description)
        self.Name = name
        self.TID = sys_type_id
        self.Frozen = frozen

    def __eq__(self, other):
        return False if not isinstance(other, SysState) \
            else super().__eq__(other) \
            and self.Name == other.Name and self.TID == other.TID and self.Frozen == other.Frozen
