# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	BaseDao.py
# @Time		    	:	2020/1/30 05:30
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.1
from typing import List
from OriginNew.Common.DB import DBCore
from OriginNew.Model.ControlType import ControlType
from OriginNew.Model.Base import Base


class BaseDao:
    def __init__(self):
        """
        构造函数
        初始化Mysql数据库操控自定义对象DBCore
        """
        self.db = DBCore()

    def __modify__(self, entities: List[Base], control_type: ControlType = ControlType.INSERT) -> bool:
        """
        核心业务操控函数
        :param entities: 待新增、修改或删除操作的所对应自定义模型实例对象列表集合，以便于精准定位所需新增、修改或删除操作的基表种类
        :param control_type: 操控枚举种类
        :return: 若成功执行业务操作返回：True，业务操作执行失败返回：False
        """
        commands = list()
        for entity in entities:
            commands.append(entity.get_command(control_type))
            if commands[len(commands) - 1] is None:
                return False
        if len(commands) != len(entities):
            return False
        else:
            self.db.execute(commands)
            return self.db.data == len(entities)

    def query(self, entity: Base, condition=None) -> list:
        """
        查询函数
        :param entity: 待查询基表所对应自定义模型对象，以便于精准定位所查基表种类
        :param condition: 需要带`WHERE`关键字的查询条件
        :return: 所有符合查询条件与基表所对应自定义模型的列表
        """
        entities = list()
        command = entity.get_command(ControlType.QUERY, condition)
        if command is None:
            return entities
        self.db.query(command)
        for i in self.db.data:
            entities.append(entity.construct(i))
        return entities

    def insert(self, entities: List[Base]) -> bool:
        """
        新增函数
        :param entities: 待新增操作的所对应自定义模型实例对象列表集合，以便于精准定位所需新增操作的基表种类
        :return: 若成功执行新增操作返回：True，新增操作执行失败返回：False
        """
        return self.__modify__(entities, ControlType.INSERT)

    def update(self, entities: List[Base]) -> bool:
        """
        修改更新函数
        :param entities: 待更新操作的所对应自定义模型实例对象列表集合，以便于精准定位所需更新操作的基表种类
        :return: 若成功执行更新操作返回：True，更新操作执行失败返回：False
        """
        return self.__modify__(entities, ControlType.UPDATE)

    def delete(self, entities: List[Base]) -> bool:
        """
        删除函数
        :param entities: 待删除操作的所对应自定义模型实例对象列表集合，以便于精准定位所需删除操作的基表种类
        :return: 若成功执行删除操作返回：True，删除操作执行失败返回：False
        """
        return self.__modify__(entities, ControlType.DELETE)
