import marshmallow as ma
from app.models.bb_db import BlackBusiness

class BlackBusinessSchema(ma.ModelSchema):
    class Meta:
        # Fields to expose
        model = BlackBusiness
