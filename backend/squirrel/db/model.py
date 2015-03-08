from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import sqlalchemy as sa

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Model(object):

    def __init__(self, dburl=None):
        if dburl is None:
            dburl = 'sqlite://'  # in memory DB
        self._engine = sa.create_engine(dburl, echo=True)

    def start(self, create=True):
        Session = sa.orm.sessionmaker()
        Session.configure(bind=self._engine)
        self._session = Session()
        if create:
            Base.metadata.create_all(self._engine)

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
