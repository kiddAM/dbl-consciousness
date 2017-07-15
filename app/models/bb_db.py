from sqlalchemy import orm
from sqlalchemy import Column, Integer, String, Float

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BlackBusinessMapping(Base):
    "Docstring for BlackBusinessMapping"
    __tablename__ = "Black_Businesses"



    _id = Column('id', Integer, primary_key=True)
    name = Column('name', String, nullable=False)
    owner = Column('owner_name', String, nullable=False)
    service = Column('service', String, nullable=True)
    x = Column('lat', Float)
    y = Column('long', Float)
    founding = Column('founding', String)
    address = Column('address', String, nullable=False)

    def getid(self):
        return self._id

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s'>" % (self.name, self.fullname, self.password)

