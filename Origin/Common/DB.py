# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	DB.py
# @Time		    	:	2020/1/16 15:34
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.0
import pymysql
from typing import List


class DBCore:
    def __init__(self, host='localhost', port=3306, user='root', password='123456', database='atmdb'):
        super().__init__()
        self.host = host
        self.port = port
        self.username = user
        self.password = password
        self.database = database
        self.db = None
        self.data = None
        self.cursor = None

    def __open__(self):
        self.db = pymysql.connect(host=self.host, port=self.port, user=self.username,
                                  password=self.password, database=self.database)
        self.cursor = self.db.cursor()

    def __close__(self):
        self.db.close()

    def execute(self, sqls: List[str]):
        self.__open__()
        self.data = 0
        # noinspection PyBroadException
        try:
            for sql in sqls:
                self.cursor.execute(sql)
                self.data += self.cursor.rowcount
            if self.data != len(sqls):
                self.data = 0
                self.db.rollback()
            else:
                self.db.commit()
        except Exception:
            self.data = 0
            self.db.rollback()
        self.__close__()

    def query(self, sql):
        self.__open__()
        self.cursor.execute(sql)
        self.data = self.cursor.fetchall()
        self.__close__()
