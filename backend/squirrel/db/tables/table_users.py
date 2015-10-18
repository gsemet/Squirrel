from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import and_

from squirrel.db.tables.base.table_base import TableBase


class TableUsers(IdTableBase):
    __tablename__ = 'users'

    pseudo = Column(String(256), index=True)
    first_name = Column(String(256), index=True)
    last_name = Column(String(256), index=True)

    def __init__(self, id, pseudo, full_name):
        self.id = id
        self.pseudo = pseudo
        self.full_name = full_name
