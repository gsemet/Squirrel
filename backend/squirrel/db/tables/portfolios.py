from sqlalchemy import Column, Integer, String
from squirrel.db.model import Base


class Portfolios(Base):
    __tablename__ = 'portfolios'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<{}(name='{}', fullname='{}', password='{}')>".format(
            self.__tablename__, self.name, self.fullname, self.password)
