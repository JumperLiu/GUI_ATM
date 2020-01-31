# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	Card.py
# @Time		    	:	2020/1/16 21:05
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.0
from Origin.Model.Origin import Origin


class Card(Origin):
    def __init__(self, current_id=0, sys_type_id=0, personnel_id=None, name=None, serial_id=None, check_sid=None,
                 activation_date_time=None, query_password=None, trade_password=None, currency_type=1, deposit_type=1,
                 balance=0.0, bill_day=5, repay_day=23, mobile=None, email=None, address=None, state=None, valid=1,
                 create_time=None, controller=None, description=None):
        super().__init__('`Card`', current_id, sys_type_id, state, valid, create_time, controller, description)
        self.PersonnelID = personnel_id
        self.Name = name
        self.SerialID = serial_id
        self.CheckSID = check_sid
        self.ActivationDateTime = activation_date_time
        self.QueryPassword = query_password
        self.TradePassword = trade_password
        self.CurrencyType = currency_type
        self.DepositType = deposit_type
        self.Balance = balance
        self.BillDay = bill_day
        self.RepayDay = repay_day
        self.MobilePhone = mobile
        self.Email = email
        self.Address = address

    def __eq__(self, other):
        return False if not isinstance(other, Card) else super().__eq__(other) \
            and self.PersonnelID == other.PersonnelID and self.Name == other.Name and self.SerialID == other.SerialID \
            and self.CheckSID == other.CheckSID and self.ActivationDateTime == other.ActivationDateTime \
            and self.QueryPassword == other.QueryPassword and self.TradePassword == other.TradePassword \
            and self.CurrencyType == other.CurrencyType and self.DepositType == other.DepositType \
            and self.Balance == other.Balance and self.BillDay == other.BillDay and self.RepayDay == other.RepayDay \
            and self.MobilePhone == other.MobilePhone and self.Email == other.Email and self.Address == other.Address
