# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import and_

from squirrel.db.tables.table_base import IdTableBase


class TableStocks(IdTableBase):
    __tablename__ = 'stocks'

    symbol = Column(String(10), index=True)
    exchange = Column(String(10), index=True)
    importer_id = Column(Integer, ForeignKey("plugin_importers.id"))
    title = Column(String(200), index=True)
    currency_id = Column(Integer, ForeignKey("currencies.id"))
