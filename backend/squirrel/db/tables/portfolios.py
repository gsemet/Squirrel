from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from squirrel.db.model import Base


class Portfolios(Base):
    __tablename__ = 'portfolios'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    exchange = Column(String)

    def __repr__(self):
        return "<{}(name='{}', exchange='{}')>".format(
            self.__tablename__, self.name, self.exchange)
