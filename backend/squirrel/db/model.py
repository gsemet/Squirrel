from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import sqlalchemy as sa

from sqlalchemy.ext.declarative import declarative_base

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

Base = declarative_base(metadata=sa.MetaData(naming_convention=naming_convention))

# force import all table here to register them, so they ll be created with the
# create_all function.
from squirrel.db.tables import *


class Model(object):

    def __init__(self, dburl=None):
        if dburl is None:
            dburl = 'sqlite://'  # in memory DB
        verbose = False
        self._engine = sa.create_engine(dburl, echo=verbose,  pool_reset_on_return=None)
        self.metadata = Base.metadata

    def start(self, create=True):
        self.metadata.bind = self._engine

        Session = sa.orm.sessionmaker()
        Session.configure(bind=self._engine)
        self._session = Session()
        if create:
            print("Creating all tables...")
            self.metadata.create_all(self._engine)

    def stop(self):
        self._session.close()

    @property
    def session(self):
        return self._session

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, type, value, tb):
        self.stop()
