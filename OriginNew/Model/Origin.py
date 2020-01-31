# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	Origin.py
# @Time		    	:	2020/1/30 05:30
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.1
from abc import abstractmethod
from OriginNew.Model.Base import Base
from OriginNew.Model.ControlType import ControlType


class Origin(Base):
    def __init__(self, table_name=None, current_id=0, sys_type_id=0, state=None, valid=1, create_time=None,
                 controller=None, description=None):
        super().__init__(table_name, current_id, create_time, description)
        self.TID = sys_type_id
        self.State = state
        self.Valid = valid
        self.Controller = controller

    def __eq__(self, other):
        return False if not isinstance(other, Origin) \
            else super().__eq__(other) and self.TID == other.TID and self.State == other.State \
            and self.Valid == other.Valid and self.Controller == other.Controller

    @abstractmethod
    def construct(self, content: tuple):
        pass

    @abstractmethod
    def get_command(self, control_type: ControlType = ControlType.QUERY, condition: str = None) -> str or None:
        return None
