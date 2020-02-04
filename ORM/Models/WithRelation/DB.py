# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	DB.py
# @Time		    	:	2020/2/4 15:16
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.1
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


class DB:
    __tablename__: str = None
    host = 'localhost'
    port = 3306
    user = 'root'
    password = '123456'
    database = 'atmormdb'
    charset = 'utf8mb4'
    engine = create_engine("mysql+mysqlconnector://{}:{}@{}:{}/{}".format(user, password, host, port, database),
                           isolation_level="READ COMMITTED", max_overflow=5)
    base = declarative_base()
