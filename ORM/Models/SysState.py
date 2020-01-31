# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	SysState.py
# @Time		    	:	2020/1/29 17:48
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.1
from sqlalchemy import Table, MetaData, Column, Boolean, Integer, String, UniqueConstraint
from ORM.Core.Base import Base


class SysState(Base, Base.base):
    __tablename__ = 'sysstates'
    __table__ = Table(
        __tablename__,
        MetaData(),
        Base.ID,
        Column('TypeID', Integer, index=True, autoincrement=False, nullable=False, default=0),
        Column('Name', String(255), index=True, nullable=False),
        Column('Frozen', Boolean, index=True, nullable=False, default=False),
        Base.CreateTime,
        Base.ModifyTime,
        Base.Description,
        UniqueConstraint('TypeID', 'Name', name='uix_SysStates_TypeID_Name')
    )

    def __init__(self, current_id=None, type_id=0, name=None, frozen=False, create_time=None, modify_time=None,
                 description=None):
        super().__init__(current_id, create_time, modify_time, description)
        self.TypeID = type_id
        self.Name = name
        self.Frozen = frozen

    def __repr__(self):
        return 'ID = {}, TypeID = {}, Name = {}, Frozen = {}, CreateTime = {}, ModifyTime = {}, Description = {}'.\
            format(self.ID, self.TypeID, self.Name, '是' if self.Frozen else '否', self.CreateTime, self.ModifyTime,
                   self.Description)


if __name__ == '__main__':
    pass
    # from ORM.Core.CPU import CPU
    # cpu = CPU(SysState)
    # create table
    # if not cpu.create():
    #     print('基表 [ {} ] 创建失败……程序结束'.format(cpu.OriginType.__tablename__))
    #     exit(0)
    # insert data
    # print('基表 [ {} ] 创建成功，开始注入数据……'.format(cpu.OriginType.__tablename__))
    # data = [
    #     SysState(type_id=4, name='有效项目组'),
    #     SysState(type_id=4, name='无效项目组'),
    #     SysState(type_id=4, name='有效项目组员'),
    #     SysState(type_id=4, name='无效项目组员')
    # ]
    # print('状态新增{}'.format('成功！' if cpu.install_all(data) else '失败……'))
    # update data
    # entities = cpu.query_all(condition='WHERE 1=1 ORDER BY ID')
    # entities[0].Description = '电子信息学院大数据专业项目组状态：有效'
    # entities[1].Description = '电子信息学院大数据专业项目组状态：无效'
    # entities[2].Description = '电子信息学院大数据专业项目组员状态：有效'
    # entities[3].Description = '电子信息学院大数据专业项目组员状态：无效'
    # print('状态更新{}'.format('成功！' if cpu.update_all(entities, False) else '失败……'))
    # delete data
    # print('状态删除{}'.format('成功！' if cpu.delete_by(condition='WHERE ID IN (2, 4)') else '失败……'))
    # del cpu
