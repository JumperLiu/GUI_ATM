# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	TradeDetailsDao.py
# @Time		    	:	2020/1/30 05:30
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.1
from OriginNew.Dao.BaseDao import BaseDao
from OriginNew.Model.TradeDetails import TradeDetails


class TradeDetailsDao(BaseDao):
    def __init__(self):
        super().__init__()

    def query(self, condition=None, entity=TradeDetails()) -> list:
        return super().query(entity=entity, condition=condition)

    def insert(self, *entities: TradeDetails) -> bool:
        return super().insert(list(entities))

    def update(self, *entities: TradeDetails) -> bool:
        return super().update(list(entities))

    def delete(self, *entities: TradeDetails) -> bool:
        return super().delete(list(entities))
