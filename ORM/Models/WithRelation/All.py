# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	All.py
# @Time		    	:	2020/2/4 11:27
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.1
from sqlalchemy import Column, Boolean, DATETIME, Integer, String, UniqueConstraint
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.orm import relationship, backref
from datetime import datetime
from ORM.Models.WithRelation.DB import DB


class Association(DB.base):
    __tablename__ = 'association'
    ID = Column('ID', Integer, primary_key=True, autoincrement=True, nullable=False)
    SysType_ID = Column(Integer, ForeignKey('systypes.ID'), primary_key=True)
    SysState_ID = Column(Integer, ForeignKey('sysstates.ID'), primary_key=True)
    sysstate = relationship('SysState', backref='parent_associations')
    systype = relationship('SysType', backref='child_associations')


class SysType(DB.base):
    __tablename__ = 'systypes'
    ID = Column('ID', Integer, primary_key=True, autoincrement=True, nullable=False)
    ParentID = Column('ParentID', Integer, index=True, autoincrement=False, nullable=False, default=-1)
    Name = Column('Name', String(255), index=True, nullable=False)
    Frozen = Column('Frozen', Boolean, index=True, nullable=False, default=False)
    SysStates = relationship('SysState', secondary='association', cascade='all, delete-orphan')
    CreateTime = Column('CreateTime', DATETIME(fsp=6), index=True, nullable=False, default=datetime.now())
    ModifyTime = Column('ModifyTime', DATETIME(fsp=6), index=True, nullable=False, default=datetime.now(),
                        onupdate=datetime.now())
    Description = Column('Description', String(2000), nullable=True)
    UniqueConstraint('ParentID', 'Name', name='uix_SysTypes_ParentID_Name')

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


class SysState(DB.base):
    __tablename__ = 'sysstates'
    ID = Column('ID', Integer, primary_key=True, autoincrement=True, nullable=False)
    TypeID = Column('TypeID', Integer, ForeignKey('systypes.ID'))
    SysType = relationship('SysType', backref=backref('sysstates', cascade='all, delete-orphan'))
    Name = Column('Name', String(255), index=True, nullable=False)
    Frozen = Column('Frozen', Boolean, index=True, nullable=False, default=False)
    CreateTime = Column('CreateTime', DATETIME(fsp=6), index=True, nullable=False, default=datetime.now())
    ModifyTime = Column('ModifyTime', DATETIME(fsp=6), index=True, nullable=False, default=datetime.now(),
                        onupdate=datetime.now())
    Description = Column('Description', String(2000), nullable=True)
    UniqueConstraint('TypeID', 'Name', name='uix_SysStates_TypeID_Name')

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


class All(DB):
    def __init__(self):
        super().__init__()

    def create_by_engine(self):
        self.base.metadata.drop_all(self.engine)
        self.base.metadata.create_all(self.engine)


if __name__ == '__main__':
    a = All()
    a.create_by_engine()
