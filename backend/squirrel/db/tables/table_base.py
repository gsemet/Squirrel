from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TableBase(AbstractConcreteBase, Base):
    __tablename__ = NotImplementedError

    def addAndGetId(self, model):
        rows = model.session.query(type(self)).filter(self.formatSelectUniqCondition()).limit(1)
        if not rows:
            model.session.add(self)
            rows = model.session.query(type(self)).filter(self.formatSelectUniqCondition()).limit(1)
            res = self.rowToMySelf(rows[0]).id
        else:
            res = self.rowToMySelf(rows[0]).id
        return res

    def rowToMySelf(self):
        raise NotImplementedError

    def formatSelectUniqCondition(self):
        raise NotImplementedError
