from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.orm.exc import NoResultFound

from squirrel.db.model import Base


class TableBase(AbstractConcreteBase, Base):
    __tablename__ = NotImplementedError

    def addAndGetId(self, model):
        try:
            row = model.session.query(type(self)).filter(
                self.formatSelectUniqCondition()).one()
            res = self.rowToMySelf(row).id
        except NoResultFound:
            model.session.add(self)
            row = model.session.query(type(self)).filter(
                self.formatSelectUniqCondition()).one()
            res = self.rowToMySelf(row).id
        return res

    def ensureHasId(self, model):
        self.id = self.addAndGetId(model)

    def rowToMySelf(self):
        raise NotImplementedError

    def formatSelectUniqCondition(self):
        raise NotImplementedError
