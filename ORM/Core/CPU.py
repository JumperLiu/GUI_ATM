# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	CPU.py
# @Time		    	:	2020/1/29 15:21
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.1
from sqlalchemy import text
from sqlalchemy.orm import scoped_session, sessionmaker
from typing import List
from ORM.Core.Base import Base


class CPU(Base):
    def __init__(self, origin_type: Base.base):
        super().__init__()
        self.OriginType = origin_type
        self.Session = None
        self.__open__()

    def __del__(self):
        self.__close__()
        self.Session.remove()

    def __open__(self):
        self.Session = scoped_session(sessionmaker(bind=Base.engine, expire_on_commit=False))

    def __close__(self):
        self.Session.close()

    def create(self) -> bool:
        return self.OriginType().create()

    def drop(self) -> bool:
        return self.OriginType().drop()

    def query_one(self, entity: Base.base) -> Base.base:
        return self.Session.query(self.OriginType).get(entity.ID)

    def query_all(self, condition: str = None, columns: str = '*') -> List[Base.base]:
        return self.Session.query(self.OriginType).from_statement(text('SELECT {} FROM `{}` {}'.format(
            columns, self.OriginType.__tablename__, '' if condition is None else condition
        ))).all()

    def install_all(self, entities: List[Base.base]) -> bool:
        # noinspection PyBroadException
        try:
            self.Session.bulk_save_objects(entities)
            self.Session.commit()
            success = True
        except Exception as e:
            print(e)
            self.Session.rollback()
            success = False
        return success

    def install_any(self, *entities: Base.base) -> bool:
        return self.install_all(list(entities))

    def update_all(self, entities: List[Base.base], check=True) -> bool:
        # noinspection PyBroadException
        try:
            success = True
            for entity in entities:
                origin = self.query_one(entity) if check else entity
                if origin is not None:
                    self.Session.merge(origin)
                else:
                    success = False
                    break
            if not success:
                self.Session.rollback()
            else:
                self.Session.commit()
        except Exception as e:
            print(e)
            self.Session.rollback()
            success = False
        return success

    def update_any(self, *entities: Base.base, check=True) -> bool:
        return self.update_all(list(entities), check)

    def delete_all(self, entities: List[Base.base], check=True) -> bool:
        # noinspection PyBroadException
        try:
            success = True
            for entity in entities:
                origin = self.query_one(entity) if check else entity
                if origin is not None:
                    self.Session.delete(origin)
                else:
                    success = False
                    break
            if not success:
                self.Session.rollback()
            else:
                self.Session.commit()
        except Exception as e:
            print(e)
            self.Session.rollback()
            success = False
        return success

    def delete_any(self, *entities: Base.base, check=True) -> bool:
        return self.delete_all(list(entities), check)

    def delete_by(self, condition: str = None) -> bool:
        return self.delete_all(self.query_all(condition=condition), False)
