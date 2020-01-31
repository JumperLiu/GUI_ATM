# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	TradeDetails.py
# @Time		    	:	2020/1/30 21:22
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.1
from sqlalchemy import Table, MetaData, Column, Integer, DECIMAL, Index
from ORM.Core.Origin import Origin


class TradeDetails(Origin, Origin.base):
    __tablename__ = 'tradedetails'
    __table__ = Table(
        __tablename__,
        MetaData(),
        Origin.ID,
        Column('BeginCardID', Integer, index=True, autoincrement=False, nullable=False, default=-1),
        Origin.TypeID,
        Column('EndCardID', Integer, index=True, autoincrement=False, nullable=True),
        Column('Amount', DECIMAL(26, 6), index=True, nullable=False, default=0.0),
        Origin.State,
        Origin.Valid,
        Origin.CreateTime,
        Origin.ModifyTime,
        Origin.Controller,
        Origin.Description,
        Index('ix_TradeDetails_State_Valid', 'State', 'Valid')
    )

    def __init__(self, current_id=None, begin_card_id=None, type_id=None, end_card_id=None,
                 amount=0.0, state=None, valid=True, create_time=None,
                 modify_time=None, controller=None, description=None):
        super().__init__(current_id, type_id, state, valid, controller, create_time, modify_time, description)
        self.BeginCardID = begin_card_id
        self.EndCardID = end_card_id
        self.Amount = amount

    def __repr__(self):
        return 'ID = {}, BeginCardID = {}, TypeID = {}, EndCardID = {}, Amount = {}, State = {}, Valid = {}, ' \
               'CreateTime = {}, ModifyTime = {}, Controller = {}, Description = {}'.\
            format(self.ID, self.BeginCardID, self.TypeID, self.EndCardID, self.Amount, self.State,
                   '有效' if self.Valid else '无效', self.CreateTime, self.ModifyTime, self.Controller, self.Description)


if __name__ == '__main__':
    pass
    # from ORM.Core.CPU import CPU
    # cpu = CPU(TradeDetails)
    # create table
    # if not cpu.create():
    #     print('基表 [ {} ] 创建失败……程序结束'.format(cpu.OriginType.__tablename__))
    #     exit(0)
    # insert data
    # print('基表 [ {} ] 创建成功，开始注入数据……'.format(cpu.OriginType.__tablename__))
    # data = [
    #     TradeDetails(begin_card_id=1, type_id=15, end_card_id=12, amount=2000.098, state=1, controller=1),
    #     TradeDetails(begin_card_id=12, type_id=16, end_card_id=1, amount=2000.098, state=1, controller=1),
    #     TradeDetails(begin_card_id=1, type_id=11, amount=6600.00, state=1, controller=1)
    # ]
    # print('交易明细新增{}'.format('成功！' if cpu.install_all(data) else '失败……'))
    # update data
    # trade_details = cpu.query_one(TradeDetails(current_id=3))
    # trade_details.Amount = 8800.009896
    # print('交易明细更新{}'.format('成功！' if cpu.update_any(trade_details, check=False) else '失败……'))
    # delete data
    # print('交易明细删除{}'.format('成功！' if cpu.delete_by(condition='WHERE ID>2') else '失败……'))
    # del cpu
