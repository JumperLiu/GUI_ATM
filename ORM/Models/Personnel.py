# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	Personnel.py
# @Time		    	:	2020/1/29 23:10
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.1
from sqlalchemy import Table, MetaData, Column, Boolean, DATE, String, UniqueConstraint, Index
from ORM.Core.Origin import Origin
from ORM.Common.Utils import Utils


class Personnel(Origin, Origin.base):
    __tablename__ = 'personnels'
    __table__ = Table(
        __tablename__,
        MetaData(),
        Origin.ID,
        Origin.TypeID,
        Column('PersonnelUniqueID', String(20), nullable=False),
        Column('Name', String(50), index=True, nullable=False),
        Column('Gender', Boolean, index=True, nullable=False, default=True),
        Column('Birthday', DATE, index=True, nullable=True),
        Column('LoginName', String(20), nullable=False),
        Column('LoginPassword', String(64), nullable=False),
        Origin.State,
        Origin.Valid,
        Origin.CreateTime,
        Origin.ModifyTime,
        Origin.Controller,
        Origin.Description,
        UniqueConstraint('PersonnelUniqueID', name='uix_Personnels_PersonnelUniqueID'),
        UniqueConstraint('LoginName', name='uix_Personnels_LoginName'),
        Index('ix_Personnels_LoginName_LoginPassword', 'LoginName', 'LoginPassword'),
        Index('ix_Personnels_State_Valid', 'State', 'Valid')
    )

    def __init__(self, current_id=None, type_id=None, personnel_unique_id=None, name=None, gender=True,
                 birthday=None, login_name=None, login_password=None, state=None, valid=True,
                 create_time=None, modify_time=None, controller=None, description=None):
        super().__init__(current_id, type_id, state, valid, controller, create_time, modify_time, description)
        self.Tools = Utils()
        self.PersonnelUniqueID = personnel_unique_id
        self.Name = name
        self.Gender = gender
        self.Birthday = birthday
        self.LoginName = login_name
        self.LoginPassword = self.Tools.encrypt(login_password)

    def __repr__(self):
        return 'ID = {}, TypeID = {}, PersonnelUniqueID = {}, Name = {}, Gender = {}, Birthday = {}, LoginName = {}, ' \
               'LoginPassword = {}, State = {}, Valid = {}, CreateTime = {}, ModifyTime = {}, Controller = {}, ' \
               'Description = {}'.format(self.ID, self.TypeID, self.PersonnelUniqueID, self.Name,
                                         '男' if self.Gender else '女', self.Birthday, self.LoginName,
                                         self.LoginPassword, self.State, '有效' if self.Valid else '无效',
                                         self.CreateTime, self.ModifyTime, self.Controller, self.Description)


if __name__ == '__main__':
    pass
    # from ORM.Core.CPU import CPU
    # cpu = CPU(Personnel)
    # create table
    # if not cpu.create():
    #     print('基表 [ {} ] 创建失败……程序结束'.format(cpu.OriginType.__tablename__))
    #     exit(0)
    # insert data
    # print('基表 [ {} ] 创建成功，开始注入数据……'.format(cpu.OriginType.__tablename__))
    # personnel = Personnel(type_id=2, personnel_unique_id='610112197903130014', name='刘志鹏', login_name='jumper79',
    #                       login_password='jumper_79', state=1)
    # print('人员新增{}'.format('成功！' if cpu.install_any(personnel) else '失败……'))
    # update data
    # personnel = cpu.query_one(Personnel(current_id=1))
    # personnel.Birthday = '1979-3-13'
    # personnel.Controller = 1
    # personnel.Description = '银行ATM系统超级管理员，大数据专业讲师，Apple developer。'
    # print('人员更新{}'.format('成功！' if cpu.update_any(personnel, check=False) else '失败……'))
    # delete data
    # personnel = cpu.query_one(Personnel(current_id=1))
    # print('人员删除{}'.format('成功！' if cpu.delete_any(personnel, check=False) else '失败……'))
    # del cpu
