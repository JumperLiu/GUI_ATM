# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	Card.py
# @Time		    	:	2020/1/30 15:28
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.1
from sqlalchemy import Table, MetaData, Column, String, Integer, DECIMAL, UniqueConstraint, Index
from sqlalchemy.dialects.mysql import DATETIME, TINYINT
from ORM.Core.Origin import Origin


class Card(Origin, Origin.base):
    __tablename__ = 'cards'
    __table__ = Table(
        __tablename__,
        MetaData(),
        Origin.ID,
        Origin.TypeID,
        Column('PersonnelID', Integer, autoincrement=False, nullable=False, default=-1),
        Column('Name', String(50), index=True, nullable=False),
        Column('SerialID', String(20), nullable=False),
        Column('CheckSID', String(10), index=True, nullable=False),
        Column('ActivationDateTime', DATETIME(fsp=6), nullable=True),
        Column('QueryPassword', String(64), index=True, nullable=False),
        Column('TradePassword', String(64), index=True, nullable=False),
        Column('CurrencyType', TINYINT(2), nullable=False, default=1),
        Column('DepositType', TINYINT(2), nullable=False, default=1),
        Column('Balance', DECIMAL(26, 6), index=True, nullable=False, default=0.0),
        Column('BillDay', TINYINT(2), nullable=False, default=5),
        Column('RepayDay', TINYINT(2), nullable=False, default=23),
        Column('MobilePhone', String(20), nullable=True),
        Column('Email', String(50), nullable=True),
        Column('Address', String(255), nullable=True),
        Origin.State,
        Origin.Valid,
        Origin.CreateTime,
        Origin.ModifyTime,
        Origin.Controller,
        Origin.Description,
        UniqueConstraint('TypeID', 'PersonnelID', 'SerialID', name='uix_Cards_TID_PID_SID'),
        Index('ix_Cards_CurrencyType_DepositType', 'CurrencyType', 'DepositType'),
        Index('ix_Cards_BillDay_RepayDay', 'BillDay', 'RepayDay'),
        Index('ix_Cards_State_Valid', 'State', 'Valid')
    )

    def __init__(self, current_id=None, type_id=None, personnel_id=None, name=None, serial_id=None, check_id=None,
                 activation_datetime=None, query_password=None, trade_password=None, currency_type=1, deposit_type=1,
                 balance=0.0, bill_day=5, repay_day=23, mobile_phone=None, email=None,
                 address=None, state=None, valid=True, create_time=None, modify_time=None, controller=None,
                 description=None):
        super().__init__(current_id, type_id, state, valid, controller, create_time, modify_time, description)
        self.PersonnelID = personnel_id
        self.Name = name
        self.SerialID = serial_id
        self.CheckSID = check_id
        self.ActivationDateTime = activation_datetime
        self.QueryPassword = query_password
        self.TradePassword = trade_password
        self.CurrencyType = currency_type
        self.DepositType = deposit_type
        self.Balance = balance
        self.BillDay = bill_day
        self.RepayDay = repay_day
        self.MobilePhone = mobile_phone
        self.Email = email
        self.Address = address

    def __repr__(self):
        return 'ID = {}, TypeID = {}, PersonnelID = {}, Name = {}, SerialID = {}, CheckSID = {}, ' \
               'ActivationDateTime = {}, QueryPassword = {}, TradePassword = {}, CurrencyType = {}, ' \
               'DepositType = {}, Balance = {}, BillDay = {}, RepayDay = {}, MobilePhone = {}, Email = {}, ' \
               'Address = {}, State = {}, Valid = {}, CreateTime = {}, ModifyTime = {}, Controller = {}, ' \
               'Description = {}'.format(self.ID, self.TypeID, self.PersonnelID, self.Name, self.SerialID,
                                         self.CheckSID, self.ActivationDateTime, self.QueryPassword, self.TradePassword,
                                         self.CurrencyType, self.DepositType, self.Balance, self.BillDay, self.RepayDay,
                                         self.MobilePhone, self.Email, self.Address, self.State,
                                         '有效' if self.Valid else '无效', self.CreateTime, self.ModifyTime,
                                         self.Controller, self.Description)


if __name__ == '__main__':
    pass
    # from ORM.Core.CPU import CPU
    # cpu = CPU(Card)
    # create table
    # if not cpu.create():
    #     print('基表 [ {} ] 创建失败……程序结束'.format(cpu.OriginType.__tablename__))
    #     exit(0)
    # insert data
    # print('基表 [ {} ] 创建成功，开始注入数据……'.format(cpu.OriginType.__tablename__))
    # from hashlib import md5
    # m = md5()
    # m.update(str.encode('jumper_79'))
    # query_pw = m.hexdigest()
    # m.update(str.encode('jumper_0313'))
    # trade_pw = m.hexdigest()
    # card = Card(type_id=1, personnel_id=1, name='白金分期卡', serial_id='6226.....8319', check_id='807',
    #             query_password=query_pw, trade_password=trade_pw, state=1, controller=1)
    # print('银行卡新增{}'.format('成功！' if cpu.install_any(card) else '失败……'))
    # update data
    # import time
    # card = cpu.query_one(Card(current_id=1))
    # card.ActivationDateTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time.time())))
    # print('银行卡更新{}'.format('成功！' if cpu.update_any(card, check=False) else '失败……'))
    # delete data
    # card = cpu.query_one(Card(current_id=1))
    # print('银行卡删除{}'.format('成功！' if cpu.delete_any(card, check=False) else '失败……'))
    # del cpu
