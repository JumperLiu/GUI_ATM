# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	Base.py
# @Time		    	:	2020/1/30 05:30
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.1
from abc import abstractmethod
from OriginNew.Model.ControlType import ControlType


class Base:
    def __init__(self, table_name=None, current_id=0, create_time=None, description=None):
        self.TableName = table_name
        self.ID = current_id
        self.CreateTime = create_time
        self.Description = description

    def __eq__(self, other):
        return False if not isinstance(other, Base) \
            else self.TableName == other.TableName and self.ID == other.ID and self.CreateTime == other.CreateTime \
            and self.Description == other.Description

    def __hash__(self):
        return hash(id(self))

    @abstractmethod
    def construct(self, content: tuple):
        pass

    @abstractmethod
    def get_command(self, control_type: ControlType = ControlType.QUERY, condition: str = None) -> str or None:
        return None
