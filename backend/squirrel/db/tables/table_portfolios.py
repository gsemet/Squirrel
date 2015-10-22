# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import Text

from squirrel.db.tables.base.table_base import IdTableBase


class TablePortfolios(IdTableBase):
    __tablename__ = 'portfolios'

    name = Column(String(50), index=True)
    description = Column(Text(), index=True)
    broker_id = Column(Integer(), ForeignKey("brokers.id"))
    type = Column(Integer(), ForeignKey("portfolio_types.id"))
    creation_date = Column(DateTime(), index=True)
    currency = Column(Integer(), ForeignKey("currencies.id"))
    balance = relationship("TablePortfolioBalances", uselist=False, backref="parent")
