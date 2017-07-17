import json
from sqlalchemy import and_
from sqlalchemy import desc
from app.models.bb_db import BlackBusiness
from app.service import  service_util

def create_encounter(db_session,name,owner,service,city, state, address,founding=0):

    exists = db_session.query(BlackBusiness).filter(
        and_(BlackBusiness.name == name),
        (BlackBusiness.owner == owner),
        (BlackBusiness.address == address)
    )
    if exists:
        raise ValueError("Bad Value")
    else:
        (x, y) = service_util.getGeoLocation(address, city, state)
        business = BlackBusiness(
            name=name,
            owner=owner,
            service=service,
            x=x,
            y=y,
            founding=founding,
            address=address,
            city=city,
            state=state
        )
        db_session.add(business)
        db_session.flush()
        return business
    return None

def create_business_from_obj(db_session, business):
    exists = db_session.query(BlackBusiness).filter(
        and_(BlackBusiness.name == business.get_business_by_name()),
        (BlackBusiness.owner == business.get_business_by_owner()),
        (BlackBusiness.address == business.get_business_by_address().one_or_more())
    )
    if exists:
        raise ValueError("Bad Value")
    else:
        db_session.add(business)
        db_session.flush()
        return business
    return None

def get_all_businesses(db_session):
    return db_session.query(BlackBusiness).order_by(desc(BlackBusiness.name)).all()

def get_business_by_city(db_session, city):
    """ gets encounter by city of death """
    return db_session.query(BlackBusiness).filter(
        BlackBusiness.city == city).order_by(
        desc(BlackBusiness.name)).all()

def get_business_by_address(db_session, address):
    """ gets encounter by address of death """
    return db_session.query(BlackBusiness).filter(
        BlackBusiness.address == address).order_by(
        desc(BlackBusiness.name)).all()

def get_business_by_founding(db_session, founding):
    """ gets encounter by founding of death """
    return db_session.query(BlackBusiness).filter(
        BlackBusiness.founding == founding).order_by(
        desc(BlackBusiness.name)).all()

def get_business_by_owner(db_session, owner):
    """ gets encounter by owner of death """
    return db_session.query(BlackBusiness).filter(
        BlackBusiness.owner == owner).order_by(
        desc(BlackBusiness.name)).all()

def get_business_by_state(db_session, state):
    """ gets encounter by state of death """
    return db_session.query(BlackBusiness).filter(
        BlackBusiness.state == state).order_by(
        desc(BlackBusiness.name)).all()

def get_business_by_service(db_session, service):
    """ gets encounter by service of death """
    return db_session.query(BlackBusiness).filter(
        BlackBusiness.service == service).order_by(
        desc(BlackBusiness.name)).all()