from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Model(object):

    def __init__(self):
        engine = create_engine('sqlite:///:memory:', echo=True)

        Base.metadata.create_all(engine)
