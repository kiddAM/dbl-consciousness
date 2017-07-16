import json

from sqlalchemy import and_

import service_util
from .models import pb_db

def create_encounter(db_session, name, age, gen, dod, street, city, state,
    zipcd, county, dept, cause, brief, link):

    encounter = 
