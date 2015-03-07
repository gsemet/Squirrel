from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import and_

from squirrel.db.model import Base


class TableSymbol(Base):
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

    def addAndGetId(self, model):
        rows = model.session.query(TableSymbol).filter(
            and_(TableSymbol.symbol == self.symbol,
                 TableSymbol.exchange == self.exchange)).all()
        if not rows:
            model.session.add(self)
            rows = model.session.query(TableSymbol).filter(
                TableSymbol.symbol == self.symbol).filter(TableSymbol.exchange == self.exchange)
            res = self.rowToSymbol(rows[0]).id
        else:
            res = self.rowToSymbol(rows[0]).id
        return res

    def rowToSymbol(self, row):
        return TableSymbol(id=row.id, symbol=row.symbol, exchange=row.exchange)

    def rowsToSymbols(self, rows):
        return [TableSymbol(id=r.id, symbol=r.symbol, exchange=r.exchange) for r in rows]
