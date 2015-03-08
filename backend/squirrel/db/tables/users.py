from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import and_

from squirrel.db.tables.table_base import TableBase


class TableUsers(TableBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    pseudo = Column(String(256))
    full_name = Column(String(256))

    def __init__(self, id, pseudo, full_name):
        self.id = id
        self.pseudo = pseudo
        self.full_name = full_name

    def __repr__(self):
        return ("<{}("
                "id={id!r}, "
                "pseudo={pseudo!r}, "
                "full_name={full_name!r}"
                ")>".format(type(self).__pseudo__,
                            id=self.id,
                            pseudo=self.pseudo,
                            full_name=self.full_name,
                            ))

    def formatSelectUniqCondition(self):
        return and_(TableUsers.pseudo == self.pseudo,
                    TableUsers.full_name == self.full_name)

    def rowToMySelf(self, row):
        return TableUsers(id=row.id, symbol=row.symbol, exchange=row.exchange)

    def rowToMySelfs(self, rows):
        return [self.rowToMySelf(r) for r in rows]
