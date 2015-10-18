from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from squirrel.db.tables.base.table_base import IdTableBase


class TablePortfolios(IdTableBase):
    __tablename__ = 'portfolios'

    name = Column(String(50), index=True)
    exchange = Column(String(50), index=True)
