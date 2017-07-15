from sqlalchemy import orm
from sqlalchemy import Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BlackBusinessMapping(Base):
    "Docstring for BlackBusinessMapping"
    __tablename__ = "Black_Businesses"


    _id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    owner = Column('owner_name', String)
    founding = Column('founding', String, nullable=False)
    address = Column('address', String)

    def getid(self):
        return self._id

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s'>" % (self.name, self.fullname, self.password)

