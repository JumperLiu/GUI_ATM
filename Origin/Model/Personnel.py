# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	Personnel.py
# @Time		    	:	2020/1/16 20:45
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.0
from Origin.Model.Origin import Origin


class Personnel(Origin):
    def __init__(self, current_id=0, sys_type_id=0, personnel_unique_id=None, name=None, gender=0, birthday=None,
                 login_name=None, login_password=None, state=None, valid=1, create_time=None, controller=None,
                 description=None):
        super().__init__('`Personnel`', current_id, sys_type_id, state, valid, create_time, controller, description)
        self.PersonnelUniqueID = personnel_unique_id
        self.Name = name
        self.Gender = gender
        self.Birthday = birthday
        self.LoginName = login_name
        self.LoginPassword = login_password

    def __eq__(self, other):
        return False if not isinstance(other, Personnel) else super().__eq__(other) \
            and self.PersonnelUniqueID == other.PersonnelUniqueID and self.Name == other.Name \
            and self.Gender == other.Gender and self.Birthday == other.Birthday and self.LoginName == other.LoginName \
            and self.LoginPassword == other.LoginPassword
