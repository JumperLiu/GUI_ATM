# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	Card.py
# @Time		    	:	2020/1/30 05:30
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.1
from OriginNew.Model.Origin import Origin
from OriginNew.Model.ControlType import ControlType


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

    def construct(self, content: tuple):
        self.__init__(content[0], content[1], content[2], content[3], content[4], content[5], content[6], content[7],
                      content[8], content[9], content[10], content[11], content[12], content[13], content[14],
                      content[15], content[16], content[17], content[18], content[19], content[20], content[21])

    def get_command(self, control_type: ControlType = ControlType.QUERY, condition: str = None) -> str or None:
        command = 'SELECT * FROM {} {}'.format(self.TableName, '' if condition is None else condition)
        if control_type == ControlType.INSERT:
            command = "INSERT INTO {} (TID, PID, `Name`, `SerialID`, `CheckSID`, ActivationDT, QueryPassword" \
                      ", TradePassword, CurrencyType, DepositType, Balance, BillDay, RepayDay, MobilePhone, Email" \
                      ", Address, `State`, `Valid`, Controller, Description) VALUES ({}, {}, '{}', '{}', '{}', " \
                      "'{}', '{}', '{}', {}, {}, {}, {}, {}, '{}', '{}', '{}', {}, {}, {}, '{}')"\
                .format(self.TableName, self.TID, self.PersonnelID, self.Name, self.SerialID, self.CheckSID,
                        self.ActivationDateTime, self.QueryPassword, self.TradePassword, self.CurrencyType,
                        self.DepositType, self.Balance, self.BillDay, self.RepayDay, self.MobilePhone,
                        self.Email, self.Address, self.State, self.Valid, self.Controller,
                        '' if self.Description is None else self.Description)
        elif control_type == ControlType.UPDATE:
            command = "UPDATE {} SET TID={}, PID={}, `Name`='{}', `SerialID`='{}', `CheckSID`='{}', " \
                      "ActivationDT='{}', QueryPassword='{}', TradePassword='{}', CurrencyType={}, DepositType={}" \
                      ", Balance={}, BillDay={}, RepayDay={}, MobilePhone='{}', Email='{}', Address='{}', " \
                      "`State`={}, `Valid`={}, Controller={}, Description='{}' WHERE ID={}"\
                .format(self.TableName, self.TID, self.PersonnelID, self.Name, self.SerialID, self.CheckSID,
                        self.ActivationDateTime, self.QueryPassword, self.TradePassword, self.CurrencyType,
                        self.DepositType, self.Balance, self.BillDay, self.RepayDay, self.MobilePhone,
                        self.Email, self.Address, self.State, self.Valid, self.Controller, '' if
                        self.Description is None else self.Description, self.ID)
        elif control_type == ControlType.DELETE:
            command = 'DELETE FROM {} WHERE ID={}'.format(self.TableName, self.ID)
        return command
