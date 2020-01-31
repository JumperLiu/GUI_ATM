# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	DB.py
# @Time		    	:	2020/1/28 16:40
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.1
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.exc import NoSuchTableError
from sqlalchemy.ext.declarative import declarative_base
import time


class DB:
    __tablename__: str = None
    __table__: Table = None
    host = 'localhost'
    port = 3306
    user = 'root'
    password = '123456'
    database = 'atmormdb'
    charset = 'utf8mb4'
    engine = create_engine("mysql+mysqlconnector://{}:{}@{}:{}/{}".format(user, password, host, port, database),
                           isolation_level="READ COMMITTED", max_overflow=5)
    base = declarative_base()

    def __init__(self):
        super().__init__()
        self.CheckTableExist: time = None

    def __check_table_exist__(self, table_name: str = None) -> bool:
        self.CheckTableExist = time.time()
        try:
            Table(table_name, MetaData(), autoload=True, autoload_with=DB.engine)
            return True
        except NoSuchTableError:
            return False

    def drop(self) -> bool:
        self.__table__.drop(bind=self.engine, checkfirst=True)
        return not self.__check_table_exist__(self.__tablename__)

    def create(self) -> bool:
        if self.drop():
            self.__table__.create(bind=self.engine)
            return self.__check_table_exist__(self.__tablename__)
        return False
