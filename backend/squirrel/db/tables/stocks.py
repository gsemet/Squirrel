from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import and_

from squirrel.db.tables.table_base import TableBase


class TableStocks(TableBase):
    __tablename__ = 'stocks'

    id = Column(Integer, primary_key=True)
    symbol = Column(String(10), index=True)
    exchange = Column(String(10), index=True)
    importer_id = Column(Integer, ForeignKey("plugin_importers.id"))
    title = Column(String(200), index=True)
    currency_id = Column(Integer, ForeignKey("currencies.id"))

    def __init__(self, id, symbol, exchange, importer_id, title, currency_id):
        self.id = id
        self.symbol = symbol
        self.exchange = exchange
        self.importer_id = importer_id
        self.title = title
        self.currency_id = currency_id

    def __repr__(self):
        return ("<{}("
                "id={id!r}, "
                "symbol={symbol!r}, "
                "exchange={exchange!r}"
                "importer_id={importer_id!r}"
                ")>".format(type(self).__name__,
                            id=self.id,
                            symbol=self.symbol,
                            exchange=self.exchange,
                            importer_id=self.importer_id,
                            title=self.title,
                            currency_id=self.currency_id,
                            ))

    def formatSelectUniqCondition(self):
        return and_(TableStocks.symbol == self.symbol,
                    TableStocks.exchange == self.exchange,
                    TableStocks.importer_id == self.importer_id,
                    TableStocks.title == self.title,
                    TableStocks.currency_id == self.currency_id,
                    )

    def rowToMySelf(self, row):
        return TableStocks(id=row.id,
                           symbol=row.symbol,
                           exchange=row.exchange,
                           importer_id=row.importer_id,
                           title=row.title,
                           currency_id=row.currency_id,
                           )
