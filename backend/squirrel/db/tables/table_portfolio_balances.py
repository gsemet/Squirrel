# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import Text

from squirrel.db.tables.base.table_base import TableBase


class TablePortfolioBalances(TableBase):
    __tablename__ = 'portfolio_balances'

    id = Column(Integer(), ForeignKey("portfolios.id", ondelete="CASCADE"))
    deposit = Column(Integer())
    balance = Column(Integer())
