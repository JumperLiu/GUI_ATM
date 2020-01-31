# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	TradeDetails.py
# @Time		    	:	2020/1/16 22:24
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.0
from Origin.Model.Origin import Origin


class TradeDetails(Origin):
    def __init__(self, current_id=0, card_id=None, sys_type_id=0, amount=0.0, state=None, valid=1, create_time=None,
                 controller=None, description=None):
        super().__init__('`TradeDetails`', current_id, sys_type_id, state, valid, create_time, controller, description)
        self.CardID = card_id
        self.Amount = amount

    def __eq__(self, other):
        return False if not isinstance(other, TradeDetails) else super().__eq__(other) \
            and self.CardID == other.CardID and self.Amount == other.Amount
