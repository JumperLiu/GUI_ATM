# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	Core.py
# @Time		    	:	2020/1/28 17:06
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.1
from datetime import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mysql import DATETIME
from ORM.Core.DB import DB


class Base(DB):
    ID = Column('ID', Integer, primary_key=True, autoincrement=True, nullable=False)
    CreateTime = Column('CreateTime', DATETIME(fsp=6), index=True, nullable=False, default=datetime.now())
    ModifyTime = Column('ModifyTime', DATETIME(fsp=6), index=True, nullable=False, default=datetime.now(),
                        onupdate=datetime.now())
    Description = Column('Description', String(2000), nullable=True)

    def __init__(self, current_id=None, create_time=None, modify_time=None, description=None):
        super().__init__()
        self.ID = current_id
        self.CreateTime = create_time
        self.ModifyTime = modify_time
        self.Description = description
