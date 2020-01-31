# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	Origin.py
# @Time		    	:	2020/1/28 17:19
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.1
from sqlalchemy import Column, Boolean, Integer
from ORM.Core.Base import Base


class Origin(Base):
    TypeID = Column('TypeID', Integer, index=True, autoincrement=False, nullable=False, default=-1)
    State = Column('State', Integer, autoincrement=False, nullable=False, default=-1)
    Valid = Column('Valid', Boolean, autoincrement=False, nullable=False, default=True)
    Controller = Column('Controller', Integer, autoincrement=False, nullable=False, default=-1)

    def __init__(self, current_id=None, type_id=None, state=None, valid=True, controller=None, create_time=None,
                 modify_time=None, description=None):
        super().__init__(current_id, create_time, modify_time, description)
        self.TypeID = type_id
        self.State = state
        self.Valid = valid
        self.Controller = controller
