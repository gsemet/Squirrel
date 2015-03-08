from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import and_

from squirrel.db.tables.table_base import TableBase


class TableSymbols(TableBase):
    __tablename__ = 'symbols'

    id = Column(Integer, primary_key=True)
    symbol = Column(String(10))
    exchange = Column(String(10))

    def __init__(self, id, symbol, exchange):
        self.id = id
        self.symbol = symbol
        self.exchange = exchange

    def __repr__(self):
        return ("<{}("
                "id={id!r}, "
                "symbol={symbol!r}, "
                "exchange={exchange!r}"
                ")>".format(type(self).__name__,
                            id=self.id,
                            symbol=self.symbol,
                            exchange=self.exchange,
                            ))

    def formatSelectUniqCondition(self):
        return and_(TableSymbols.symbol == self.symbol,
                    TableSymbols.exchange == self.exchange)

    def rowToMySelf(self, row):
        return TableSymbols(id=row.id, symbol=row.symbol, exchange=row.exchange)
