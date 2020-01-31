# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	BaseDao.py
# @Time		    	:	2020/1/17 0:49
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.0
from typing import List
from Origin.Common.DB import DBCore
from Origin.Model.Base import Base
from Origin.Model.Card import Card
from Origin.Model.Origin import Origin
from Origin.Model.Personnel import Personnel
from Origin.Model.SysState import SysState
from Origin.Model.SysType import SysType
from Origin.Model.TradeDetails import TradeDetails


def __command__(entity: Base, modify_type=1) -> str:
    """
    核心业务操控SQL命令获取函数
    :param entity: 待新增、修改或删除操作的所对应自定义模型实例对象，以便于精准定位所需新增、修改或删除操作的基表种类
    :param modify_type: 操控种类：1、新增操作；2：修改操作；3：删除操作
    :return: 返回匹配所对应自定义模型实例对象的业务操控SQL命令，否则返回：None
    """
    command = None
    if isinstance(entity, SysType):
        if modify_type == 1:
            command = "INSERT INTO `SysType` (P_ID, `Name`, Frozen, Description) VALUES ({}, '{}', {}, '{}')"\
                .format(entity.PID, entity.Name, entity.Frozen,
                        '' if entity.Description is None else entity.Description)
        elif modify_type == 2:
            command = "UPDATE `SysType` SET P_ID={}, `Name`='{}', Frozen={}, Description='{}' WHERE ID={}".format(
                entity.PID, entity.Name, entity.Frozen,
                '' if entity.Description is None else entity.Description, entity.ID)
        elif modify_type == 3:
            command = 'DELETE FROM `SysType` WHERE ID={}'.format(entity.ID)
    elif isinstance(entity, SysState):
        if modify_type == 1:
            command = "INSERT INTO `SysState` (TID, `Name`, Frozen, Description) VALUES ({}, '{}', {}, '{}')"\
                .format(entity.TID, entity.Name, entity.Frozen,
                        '' if entity.Description is None else entity.Description)
        elif modify_type == 2:
            command = "UPDATE `SysState` SET TID={}, `Name`='{}', Frozen={}, Description='{}' WHERE ID={}".format(
                entity.TID, entity.Name, entity.Frozen,
                '' if entity.Description is None else entity.Description, entity.ID)
        elif modify_type == 3:
            command = 'DELETE FROM `SysState` WHERE ID={}'.format(entity.ID)
    elif isinstance(entity, Personnel):
        if modify_type == 1:
            command = "INSERT INTO `Personnel` (TID, PUID, `Name`, Gender, Birthday, LoginName, LoginPassword, " \
                      "`State`, `Valid`, Controller, Description) VALUES ({}, '{}', '{}', {}, '{}', '{}', '{}', " \
                      "{}, {}, {}, '{}')".format(entity.TID, entity.PersonnelUniqueID, entity.Name, entity.Gender,
                                                 entity.Birthday, entity.LoginName, entity.LoginPassword,
                                                 entity.State, entity.Valid, entity.Controller,
                                                 '' if entity.Description is None else entity.Description)
        elif modify_type == 2:
            command = "UPDATE `Personnel` SET TID={}, PUID={}, `Name`='{}', Gender={}, Birthday='{}', " \
                      "LoginName='{}', LoginPassword='{}', `State`={}, `Valid`={}, Controller={}, " \
                      "Description='{}' WHERE ID={}".format(entity.TID, entity.PersonnelUniqueID, entity.Name,
                                                            entity.Gender, entity.Birthday, entity.LoginName,
                                                            entity.LoginPassword, entity.State, entity.Valid,
                                                            entity.Controller, '' if entity.Description is None
                                                            else entity.Description, entity.ID)
        elif modify_type == 3:
            command = 'DELETE FROM `Personnel` WHERE ID={}'.format(entity.ID)
    elif isinstance(entity, Card):
        if modify_type == 1:
            command = "INSERT INTO `Card` (TID, PID, `Name`, `SerialID`, `CheckSID`, ActivationDT, QueryPassword" \
                      ", TradePassword, CurrencyType, DepositType, Balance, BillDay, RepayDay, MobilePhone, Email" \
                      ", Address, `State`, `Valid`, Controller, Description) VALUES ({}, {}, '{}', '{}', '{}', " \
                      "'{}', '{}', '{}', {}, {}, {}, {}, {}, '{}', '{}', '{}', {}, {}, {}, '{}')"\
                .format(entity.TID, entity.PersonnelID, entity.Name, entity.SerialID, entity.CheckSID,
                        entity.ActivationDateTime, entity.QueryPassword, entity.TradePassword,
                        entity.CurrencyType, entity.DepositType, entity.Balance, entity.BillDay,
                        entity.RepayDay, entity.MobilePhone, entity.Email, entity.Address, entity.State,
                        entity.Valid, entity.Controller, '' if entity.Description is None else entity.Description)
        elif modify_type == 2:
            command = "UPDATE `Card` SET TID={}, PID={}, `Name`='{}', `SerialID`='{}', `CheckSID`='{}', " \
                      "ActivationDT='{}', QueryPassword='{}', TradePassword='{}', CurrencyType={}, DepositType={}" \
                      ", Balance={}, BillDay={}, RepayDay={}, MobilePhone='{}', Email='{}', Address='{}', " \
                      "`State`={}, `Valid`={}, Controller={}, Description='{}' WHERE ID={}"\
                .format(entity.TID, entity.PersonnelID, entity.Name, entity.SerialID, entity.CheckSID,
                        entity.ActivationDateTime, entity.QueryPassword, entity.TradePassword, entity.CurrencyType,
                        entity.DepositType, entity.Balance, entity.BillDay, entity.RepayDay, entity.MobilePhone,
                        entity.Email, entity.Address, entity.State, entity.Valid, entity.Controller, '' if
                        entity.Description is None else entity.Description, entity.ID)
        elif modify_type == 3:
            command = 'DELETE FROM `Card` WHERE ID={}'.format(entity.ID)
    elif isinstance(entity, TradeDetails):
        if modify_type == 1:
            command = "INSERT INTO `TradeDetails` (CID, TID, Amount, `State`, `Valid`, Controller, Description) " \
                      "VALUES ({}, {}, {}, {}, {}, {}, '{}'" \
                      ")".format(entity.CardID, entity.TID, entity.Amount, entity.State, entity.Valid,
                                 entity.Controller, '' if entity.Description is None else entity.Description)
        elif modify_type == 2:
            command = "UPDATE `TradeDetails` SET CID={}, TID={}, Amount={}, `State`={}, `Valid`={}, Controller={}" \
                      ", Description='{}' WHERE ID={}".format(entity.CardID, entity.TID, entity.Amount,
                                                              entity.State, entity.Valid, entity.Controller, ''
                                                              if entity.Description is None else entity.Description,
                                                              entity.ID)
        elif modify_type == 3:
            command = 'DELETE FROM `TradeDetails` WHERE ID={}'.format(entity.ID)
    return command


class BaseDao:
    def __init__(self):
        """
        构造函数
        初始化Mysql数据库操控自定义对象DBCore
        """
        self.db = DBCore()

    def __modify__(self, entities: List[Base], modify_type=1) -> bool:
        """
        核心业务操控函数
        :param entities: 待新增、修改或删除操作的所对应自定义模型实例对象列表集合，以便于精准定位所需新增、修改或删除操作的基表种类
        :param modify_type: 操控种类：1、新增操作；2：修改操作；3：删除操作
        :return: 若成功执行业务操作返回：True，业务操作执行失败返回：False
        """
        commands = list()
        for entity in entities:
            commands.append(__command__(entity=entity, modify_type=modify_type))
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
        if isinstance(entity, Origin):
            return entities
        find = 'SELECT * FROM {} {}'.format(entity.TableName, '' if condition is None else condition)
        self.db.query(sql=find)
        for i in self.db.data:
            entities.append(
                SysType(i[0], i[1], i[2], i[3], i[4], i[5]) if isinstance(entity, SysType) else
                SysState(i[0], i[1], i[2], i[3], i[4], i[5]) if isinstance(entity, SysState) else
                Personnel(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12])
                if isinstance(entity, Personnel) else
                Card(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14],
                     i[15], i[16], i[17], i[18], i[19], i[20], i[21]) if isinstance(entity, Card) else
                TradeDetails(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
            )
        return entities

    def insert(self, entities: List[Base]) -> bool:
        """
        新增函数
        :param entities: 待新增操作的所对应自定义模型实例对象列表集合，以便于精准定位所需新增操作的基表种类
        :return: 若成功执行新增操作返回：True，新增操作执行失败返回：False
        """
        return self.__modify__(entities, 1)

    def update(self, entities: List[Base]) -> bool:
        """
        修改更新函数
        :param entities: 待更新操作的所对应自定义模型实例对象列表集合，以便于精准定位所需更新操作的基表种类
        :return: 若成功执行更新操作返回：True，更新操作执行失败返回：False
        """
        return self.__modify__(entities, 2)

    def delete(self, entities: List[Base]) -> bool:
        """
        删除函数
        :param entities: 待删除操作的所对应自定义模型实例对象列表集合，以便于精准定位所需删除操作的基表种类
        :return: 若成功执行删除操作返回：True，删除操作执行失败返回：False
        """
        return self.__modify__(entities, 3)
