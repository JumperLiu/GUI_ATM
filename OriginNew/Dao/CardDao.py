# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	CardDao.py
# @Time		    	:	2020/1/30 05:30
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.1
from OriginNew.Dao.BaseDao import BaseDao
from OriginNew.Model.Card import Card


class CardDao(BaseDao):
    def __init__(self):
        super().__init__()

    def query(self, condition=None, entity=Card()) -> list:
        return super().query(entity=entity, condition=condition)

    def insert(self, *entities: Card) -> bool:
        return super().insert(list(entities))

    def update(self, *entities: Card) -> bool:
        return super().update(list(entities))

    def delete(self, *entities: Card) -> bool:
        return super().delete(list(entities))
