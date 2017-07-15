from sqlalchemy import orm
from sqlalchemy.ext import (
    hybrid as sa_hybrid,
    declarative_base
    )
from sqlalchemy.dialects import postgresql as sa_postgres
from sqlalchemy.types import _LookupExpressionAdapter

Base = declarative_base()

class PoliceBrutalityMapping(Base):
    """docstring for PoliceBrutalityMapping."""

    __tablename__ = 'poc_police_deaths'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', TEXT, nullable=False)
    age = Column('age', Integer)
    gen = Column('gender', TEXT)
    dod = Column('date_of_death', Date, primary_key=True)
    street = Column('street', TEXT)
    city = Column('city', TEXT, nullable=False)
    state = Column('state', TEXT(2), nullable=False)
    zipcd = Column('zip_code', Integer(5), nullable=False)
    county = Column('county', TEXT)
    dept = Column('police_dept', TEXT)
    cause = Column('cause_of_death', TEXT)
    brief = Column('brief_account', TEXT)
    link = Column('link', TEXT)
    
