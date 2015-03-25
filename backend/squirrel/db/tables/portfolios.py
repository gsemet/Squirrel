from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from squirrel.db.tables.table_base import TableBase


class TablePortfolios(TableBase):
    __tablename__ = 'portfolios'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), index=True)
    exchange = Column(String(50), index=True)

    def __repr__(self):
        return "<{}(name='{}', exchange='{}')>".format(
            self.__tablename__, self.name, self.exchange)
