from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from squirrel.db.tables.table_base import TableBase


class TableCurrencies(TableBase):
    __tablename__ = 'currencies'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), index=True)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return ("<{}(id='{id}', name='{name}')>").format(
            self.__tablename__,
            self.id,
            self.name)

    def formatSelectUniqCondition(self):
        return (TableCurrencies.name == self.name)

    def rowToMySelf(self, row):
        return TableCurrencies(id=row.id,
                               name=row.name,
                               )
