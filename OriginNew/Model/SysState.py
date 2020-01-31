# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	SysState.py
# @Time		    	:	2020/1/30 05:30
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.1
from OriginNew.Model.Base import Base
from OriginNew.Model.ControlType import ControlType


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

    def construct(self, content: tuple):
        self.__init__(content[0], content[1], content[2], content[3], content[4], content[5])

    def get_command(self, control_type: ControlType = ControlType.QUERY, condition: str = None) -> str or None:
        command = 'SELECT * FROM {} {}'.format(self.TableName, '' if condition is None else condition)
        if control_type == ControlType.INSERT:
            command = "INSERT INTO {} (TID, `Name`, Frozen, Description) VALUES ({}, '{}', {}, '{}')"\
                .format(self.TableName, self.TID, self.Name, self.Frozen,
                        '' if self.Description is None else self.Description)
        elif control_type == ControlType.UPDATE:
            command = "UPDATE {} SET TID={}, `Name`='{}', Frozen={}, Description='{}' WHERE ID={}".format(
                self.TableName, self.TID, self.Name, self.Frozen, '' if self.Description is None else self.Description,
                self.ID)
        elif control_type == ControlType.DELETE:
            command = 'DELETE FROM {} WHERE ID={}'.format(self.TableName, self.ID)
        return command
