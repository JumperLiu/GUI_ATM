# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	SysTypeDao.py
# @Time		    	:	2020/1/16 22:49
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.0
from Origin.Dao.BaseDao import BaseDao
from Origin.Model.SysType import SysType


class SysTypeDao(BaseDao):
    def __init__(self):
        super().__init__()

    def query(self, condition=None, entity=SysType()) -> list:
        return super().query(entity=entity, condition=condition)

    def insert(self, *entities: SysType) -> bool:
        return super().insert(list(entities))

    def update(self, *entities: SysType) -> bool:
        return super().update(list(entities))

    def delete(self, *entities: SysType) -> bool:
        return super().delete(list(entities))
