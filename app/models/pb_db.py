from sqlalchemy import Column, Enum, Integer, TEXT, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class GenderIDs(Enum):
    """docstring for ."""
    man = 'M'
    tman = 'TM'
    twom = 'TW'
    wom = 'W'
    unk = 'n/a'

class CausesOfDeath(Enum):
    """docstring for CausesOfDeath."""
    asx_restr = 'Asphyxiation/Restraint'
    beaten = 'Beaten'
    gun_taser = 'Gunshot/Taser'
    other = 'Other'
    vehicle = 'Vehicle'

class PoliceBrutalityMapping(Base):
    """docstring for PoliceBrutalityMapping."""

    __tablename__ = 'poc_police_deaths'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', TEXT, nullable=False)
    age = Column('age', Integer)
    gen = Column('gender', Enum(GenderIDs), nullable=False)
    ethn = Column('race/ethnicity', TEXT)
    dod = Column('date_of_death', Date, primary_key=True)
    street = Column('street', TEXT)
    city = Column('city', TEXT, nullable=False)
    state = Column('state', TEXT(2), nullable=False)
    zipcd = Column('zip_code', Integer(5), nullable=False)
    county = Column('county', TEXT)
    dept = Column('police_dept', TEXT)
    cause = Column('cause_of_death', Enum(CausesOfDeath), nullable=False)
    brief = Column('brief_account', TEXT)
    link = Column('link', TEXT)
