import sys
import csv
from app.models.pb_db import PoliceBrutalityMapping
from app.service.pb_service import create_encounter

filepath = "csv_report.csv"

def csv_to_pgres():
    with open(filepath, 'r') as csvfile:
        pb_victims = csv.DictReader(csvfile, dialect='excel')
        for row in pb_victims:
            victim = PoliceBrutalityMapping(
                name=row["Subject's name"],
                age=row["Subject's age"],
                gen=row["Subject's gender"],
                ethn=row["Subject's race"],
                dod=row["Date of injury resulting in death (month/day/year)"],
                street=row['Location of injury (address)'],
                city=row['Location of death (city)'],
                state=row['Location of death (state)'],
                zipcd=row['Location of death (zip code)'],
                county=row['Location of death (county)'],
                dept=row['Agency responsible for death'],
                cause=row['Cause of death'],
                brief=row['A brief description of the circumstances surrounding the death'],
                link=row['Link to news article or photo of official document'],
            )
            db_session.add(victim)
            db_session.flush()
        db_session.commit()