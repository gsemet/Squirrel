from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from squirrel.db.model import Base


class TableTick(Base):
    __tablename__ = 'ticks'

    id = Column(Integer, primary_key=True)
    symbol_id = Column(Integer,  ForeignKey('symbols.id'))
    exchange = Column(String(10))
    date = Column(Integer)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Integer)

    def __init__(self, symbol_id, date, open, high, low, close, volume):
        self.symbol_id = symbol_id
        self.date = date
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def __repr__(self):
        return ("<{}("
                "symbol_id={symbol_id!r}, "
                "date={date!r}, "
                "open={open!r}, "
                "high={high!r}, "
                "low={low!r}, "
                "close={close!r}, "
                "volume={volume!r}"
                ")>".format(type(self).__name__,
                            symbol_id=self.symbol_id,
                            date=self.date,
                            open=self.open,
                            high=self.high,
                            low=self.low,
                            close=self.close,
                            volume=self.volume,
                            ))
