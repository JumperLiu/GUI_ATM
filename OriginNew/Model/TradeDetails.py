# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	TradeDetails.py
# @Time		    	:	2020/1/30 05:30
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.1
from OriginNew.Model.Origin import Origin
from OriginNew.Model.ControlType import ControlType


class TradeDetails(Origin):
    def __init__(self, current_id=0, card_id=None, sys_type_id=0, amount=0.0, state=None, valid=1, create_time=None,
                 controller=None, description=None):
        super().__init__('`TradeDetails`', current_id, sys_type_id, state, valid, create_time, controller, description)
        self.CardID = card_id
        self.Amount = amount

    def __eq__(self, other):
        return False if not isinstance(other, TradeDetails) else super().__eq__(other) \
            and self.CardID == other.CardID and self.Amount == other.Amount

    def construct(self, content: tuple):
        self.__init__(content[0], content[1], content[2], content[3], content[4], content[5], content[6], content[7],
                      content[8])

    def get_command(self, control_type: ControlType = ControlType.QUERY, condition: str = None) -> str or None:
        command = 'SELECT * FROM {} {}'.format(self.TableName, '' if condition is None else condition)
        if control_type == ControlType.INSERT:
            command = "INSERT INTO {} (CID, TID, Amount, `State`, `Valid`, Controller, Description) " \
                      "VALUES ({}, {}, {}, {}, {}, {}, '{}'" \
                      ")".format(self.TableName, self.CardID, self.TID, self.Amount, self.State, self.Valid,
                                 self.Controller, '' if self.Description is None else self.Description)
        elif control_type == ControlType.UPDATE:
            command = "UPDATE {} SET CID={}, TID={}, Amount={}, `State`={}, `Valid`={}, Controller={}" \
                      ", Description='{}' WHERE ID={}".format(self.TableName, self.CardID, self.TID, self.Amount,
                                                              self.State, self.Valid, self.Controller, ''
                                                              if self.Description is None else self.Description,
                                                              self.ID)
        elif control_type == ControlType.DELETE:
            command = 'DELETE FROM {} WHERE ID={}'.format(self.TableName, self.ID)
        return command
