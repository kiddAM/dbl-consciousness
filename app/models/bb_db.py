from sqlalchemy import orm
from sqlalchemy import Column, Integer, String, Float, Date

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BlackBusiness(Base):
    "Docstring for BlackBusinessMapping"
    __tablename__ = "black_businesses"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, nullable=False)
    owner = Column('owner_name', String)
    service = Column('service', String, nullable=False)
    x = Column('lat', Float)
    y = Column('long', Float)
    founding = Column('founding', Date)
    address = Column('address', String, nullable=False)
    city = Column('city', String)
    state = Column('state', String)



    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s'>" % (self.name, self.fullname, self.password)

