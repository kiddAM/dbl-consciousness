import json

from sqlalchemy import and_
from sqlalchemy import desc

import service_util
from .models import pb_db

def create_encounter(db_session, name, age, gen, dod, street, city, state,
    zipcd, county, dept, cause, brief, link):
    """ adds new encounter to database"""
    gen = pb_db.PoliceBrutalityMapping.GenderIDs(gen)
    cause = pb_db.PoliceBrutalityMapping.CausesOfDeath(cause)

    exists = db_session.query(pb_db.PoliceBrutalityMapping).filter(
        and_(pb_db.PoliceBrutalityMapping.name == name),
        (pb_db.PoliceBrutalityMapping.city == city),
        (pb_db.PoliceBrutalityMapping.state == state).one_or_none())

    if exists:
        raise ValueError('Encounter already logged.')
    else:
        encounter = pb_db.PoliceBrutalityMapping(
            name = name,
            age = age,
            gen = gen,
            dod = dod,
            street = street,
            city = city,
            state = state,
            zipcd = zipcd,
            county = county,
            dept = dept,
            cause = cause,
            brief = brief,
            link = link
        )
        db_session.add(encounter)
        db_session.flush()
        return encounter
    return None

def get_encounter_by_cause(db_session, cause):
    """ gets encounter by cause of death """
    return db_session.query(pb_db.PoliceBrutalityMapping).filter(
        pb_db.PoliceBrutalityMapping.cause == cause).order_by(
        desc(pb_db.PoliceBrutalityMapping.dod)).all()

def get_encounter_by_city(db_session, city):
    """ gets encounter by city """
    return db_session.query(pb_db.PoliceBrutalityMapping).filter(
        pb_db.PoliceBrutalityMapping.city == city).order_by(
        desc(pb_db.PoliceBrutalityMapping.dod)).all()

def get_encounter_by_date(db_session, dod):
    """ gets encounter by date of death """
    return db_session.query(pb_db.PoliceBrutalityMapping).filter(
        pb_db.PoliceBrutalityMapping.dod == dod).order_by(
        desc(pb_db.PoliceBrutalityMapping.dod)).all()

def get_all_encounters(db_session):
    """ gets whole table """
    return db_session.query(pb_db.PoliceBrutalityMapping).order_by(
        desc(pb_db.PoliceBrutalityMapping.dod)).all()

def get_encounter_by_ethnicity(db_session, ethn):
    """ gets encounter by ethn """
    return db_session.query(pb_db.PoliceBrutalityMapping).filter(
        pb_db.PoliceBrutalityMapping.ethn == ethn).order_by(
        desc(pb_db.PoliceBrutalityMapping.dod)).all()

def get_encounter_by_gender(db_session, gender):
    """ gets encounter by gender """
    return db_session.query(pb_db.PoliceBrutalityMapping).filter(
        pb_db.PoliceBrutalityMapping.gender == gender).order_by(
        desc(pb_db.PoliceBrutalityMapping.dod)).all()

def get_encounter_by_date(db_session, entry_id):
    """ gets encounter by entry id """
    return db_session.query(pb_db.PoliceBrutalityMapping).filter(
        pb_db.PoliceBrutalityMapping.id == entry_id).order_by(
        desc(pb_db.PoliceBrutalityMapping.dod)).one_or_none

def get_encounter_by_name(db_session, name):
    """ gets encounter by name """
    return db_session.query(pb_db.PoliceBrutalityMapping).filter(
        pb_db.PoliceBrutalityMapping.name == name).order_by(
        desc(pb_db.PoliceBrutalityMapping.dod)).all()

def get_encounter_by_state(db_session, state):
    """ gets encounter by state """
    return db_session.query(pb_db.PoliceBrutalityMapping).filter(
        pb_db.PoliceBrutalityMapping.state == state).order_by(
        desc(pb_db.PoliceBrutalityMapping.dod)).all()
