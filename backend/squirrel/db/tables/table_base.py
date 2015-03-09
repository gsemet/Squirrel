from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from sqlalchemy.ext.declarative import AbstractConcreteBase
from squirrel.db.model import Base


class TableBase(AbstractConcreteBase, Base):
    __tablename__ = NotImplementedError

    def addAndGetId(self, model):
        row = model.session.query(type(self)).filter(
            self.formatSelectUniqCondition()).limit(1).one()
        if not row:
            model.session.add(self)
            row = model.session.query(type(self)).filter(
                self.formatSelectUniqCondition()).limit(1).one()
            res = self.rowToMySelf(row).id
        else:
            res = self.rowToMySelf(row).id
        return res

    def rowToMySelf(self):
        raise NotImplementedError

    def formatSelectUniqCondition(self):
        raise NotImplementedError
