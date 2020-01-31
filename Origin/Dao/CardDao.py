# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	CardDao.py
# @Time		    	:	2020/1/17 11:26
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.0
from Origin.Dao.BaseDao import BaseDao
from Origin.Model.Card import Card


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
