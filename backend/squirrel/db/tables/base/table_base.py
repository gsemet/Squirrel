from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sqlalchemy as sa

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.exc import NoResultFound


NAMING_CONVENTION = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

Base = declarative_base(metadata=sa.MetaData(naming_convention=NAMING_CONVENTION))


def PrimaryKeyColumn():
    return Column(Integer, primary_key=True)


class TableBase(AbstractConcreteBase, Base):
    # __tablename__ = NotImplementedError

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

    def rowsToListOfMySelf(self, rows):
        return [self.rowToMySelf(r) for r in rows]

    def formatSelectUniqCondition(self):
        raise NotImplementedError


class IdTableBase(AbstractConcreteBase, Base):
    id = PrimaryKeyColumn()
