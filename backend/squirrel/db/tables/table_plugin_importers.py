from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from sqlalchemy import Column
from sqlalchemy import String

from squirrel.db.tables.base.table_base import IdTableBase
from squirrel.db.tables.base.table_base import PrimaryKeyColumn


class TablePluginImporters(IdTableBase):
    __tablename__ = 'plugin_importers'

    name = Column(String(50), index=True)
