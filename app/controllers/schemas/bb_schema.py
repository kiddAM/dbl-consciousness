from marshmallow import Schema, fields, pre_load
from app.models.bb_db import BlackBusiness

class BlackBusinessSchema(Schema):
    name = fields.String(required=True)
    owner = fields.String(required=False)
    service = fields.String(required=True)
    x = fields.Float(required=False)
    y = fields.Float(required=False)
    founding = fields.DateTime(required=False)
    address = fields.String(required=True)
    city = fields.String(required=True)
    state = fields.String(required=True)