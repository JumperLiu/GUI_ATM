# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	Utils.py
# @Time		    	:	2020/1/31 20:36
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.1
from hashlib import md5


class Utils:
    def __init__(self):
        super().__init__()
        self.MD5 = md5()

    def encrypt(self, origin: str = None) -> str or None:
        if origin is not None:
            self.MD5.update(str.encode(origin))
            return self.MD5.hexdigest()
        return None
