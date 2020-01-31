# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	SysType.py
# @Time		    	:	2020/1/28 17:04
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.1
from sqlalchemy import Table, MetaData, Column, Boolean, Integer, String, UniqueConstraint
from ORM.Core.Base import Base


class SysType(Base, Base.base):
    __tablename__ = 'systypes'
    __table__ = Table(
        __tablename__,
        MetaData(),
        Base.ID,
        Column('ParentID', Integer, index=True, autoincrement=False, nullable=False, default=-1),
        Column('Name', String(255), index=True, nullable=False),
        Column('Frozen', Boolean, index=True, nullable=False, default=False),
        Base.CreateTime,
        Base.ModifyTime,
        Base.Description,
        UniqueConstraint('ParentID', 'Name', name='uix_SysTypes_ParentID_Name')
    )

    def __init__(self, current_id=None, parent_id=-1, name=None, create_time=None, modify_time=None, frozen=False,
                 description=None):
        super().__init__(current_id, create_time, modify_time, description)
        self.ParentID = parent_id
        self.Name = name
        self.Frozen = frozen

    def __repr__(self):
        return 'ID = {}, ParentID = {}, Name = {}, Frozen = {}, CreateTime = {}, ModifyTime = {}, Description = {}'.\
            format(self.ID, self.ParentID, self.Name, '是' if self.Frozen else '否', self.CreateTime, self.ModifyTime,
                   self.Description)


if __name__ == '__main__':
    pass
    # from ORM.Core.CPU import CPU
    # cpu = CPU(SysType)
    # create table
    # if not cpu.create():
    #     print('基表 [ {} ] 创建失败……程序结束'.format(cpu.OriginType.__tablename__))
    #     exit(0)
    # insert data
    # print('基表 [ {} ] 创建成功，开始注入数据……'.format(cpu.OriginType.__tablename__))
    # data = [
    #     SysType(parent_id=-1, name='分类根节点'),
    #     SysType(parent_id=1, name='系统管理员分类'),
    #     SysType(parent_id=2, name='超级管理员'),
    #     SysType(parent_id=2, name='系统参数维护管理员'),
    #     SysType(parent_id=1, name='数据信息管理员分类'),
    #     SysType(parent_id=5, name='超级数据维护管理员'),
    #     SysType(parent_id=5, name='数据新增管理员'),
    #     SysType(parent_id=5, name='数据修改管理员'),
    #     SysType(parent_id=5, name='数据冻结管理员'),
    #     SysType(parent_id=1, name='管理员状态分类'),
    #     SysType(parent_id=1, name='客户状态分类')
    # ]
    # print('分类新增{}'.format('成功！' if cpu.install_all(data) else '失败……'))
    # update data
    # entities = cpu.query_all(condition='WHERE 1=1 ORDER BY ID')
    # entities[0].Description = '银行ATM系统分类根节点。'
    # entities[1].Description = '银行ATM系统管理员分类一级子节点。'
    # entities[2].Description = '银行ATM系统超级管理员分类二级子节点，具备一切管理权限，为最高级别管理者。'
    # entities[3].Description = '银行ATM系统参数维护管理员分类二级子节点，具备系统内相关参数进行调整及修编，权限仅次于超级管理员，但不能进行数据信息维护。'
    # entities[4].Description = '银行ATM系统数据信息管理员分类一级子节点。'
    # entities[5].Description = '银行ATM系统超级数据维护管理员分类二级子节点，具备一切数据信息管理维护权限，为除系统参数外所有其它数据信息维护最高级别管理者。'
    # entities[6].Description = '银行ATM系统数据新增管理员分类二级子节点，具备一切除系统参数外所有其它数据新增级别管理者，权限仅次于超级数据维护管理员。'
    # entities[7].Description = '银行ATM系统数据修改管理员分类二级子节点，具备一切除系统参数外所有其它数据修改级别管理者，权限仅次于超级数据维护管理员。'
    # entities[8].Description = '银行ATM系统数据冻结管理员分类二级子节点，具备一切除系统参数外所有其它数据冻结级别管理者，权限仅次于超级数据维护管理员。'
    # entities[9].Description = '银行ATM系统管理员状态分类一级子节点。'
    # entities[10].Description = '银行ATM系统客户状态分类一级子节点。'
    # print('分类更新{}'.format('成功！' if cpu.update_all(entities, False) else '失败……'))
    # delete data
    # print('分类删除{}'.format('成功！' if cpu.delete_by(condition='WHERE ID>=2') else '失败……'))
    # del cpu
