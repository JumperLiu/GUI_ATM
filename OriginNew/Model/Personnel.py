# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	Personnel.py
# @Time		    	:	2020/1/30 05:30
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.1
from OriginNew.Model.Origin import Origin
from OriginNew.Model.ControlType import ControlType


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

    def construct(self, content: tuple):
        self.__init__(content[0], content[1], content[2], content[3], content[4], content[5], content[6], content[7],
                      content[8], content[9], content[10], content[11], content[12])

    def get_command(self, control_type: ControlType = ControlType.QUERY, condition: str = None) -> str or None:
        command = 'SELECT * FROM {} {}'.format(self.TableName, '' if condition is None else condition)
        if control_type == ControlType.INSERT:
            command = "INSERT INTO {} (TID, PUID, `Name`, Gender, Birthday, LoginName, LoginPassword, " \
                      "`State`, `Valid`, Controller, Description) VALUES ({}, '{}', '{}', {}, '{}', '{}', '{}', " \
                      "{}, {}, {}, '{}')".format(self.TableName, self.TID, self.PersonnelUniqueID, self.Name,
                                                 self.Gender, self.Birthday, self.LoginName, self.LoginPassword,
                                                 self.State, self.Valid, self.Controller,
                                                 '' if self.Description is None else self.Description)
        elif control_type == ControlType.UPDATE:
            command = "UPDATE {} SET TID={}, PUID={}, `Name`='{}', Gender={}, Birthday='{}', " \
                      "LoginName='{}', LoginPassword='{}', `State`={}, `Valid`={}, Controller={}, " \
                      "Description='{}' WHERE ID={}".format(self.TableName, self.TID, self.PersonnelUniqueID,
                                                            self.Name, self.Gender, self.Birthday, self.LoginName,
                                                            self.LoginPassword, self.State, self.Valid, self.Controller,
                                                            '' if self.Description is None else self.Description,
                                                            self.ID)
        elif control_type == ControlType.DELETE:
            command = 'DELETE FROM {} WHERE ID={}'.format(self.TableName, self.ID)
        return command
