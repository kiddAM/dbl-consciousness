from marshmallow import Schema, fields

class PoliceFatalitiesSchema(Schema):
    name = fields.Str(required=True)
    age = fields.Integer(max=3)
    gen = fields.Str()
    ethn = fields.Str()
    dod = fields.Date()
    street = fields.Str()
    city = fields.Str(required=True)
    state = fields.Str(required=True, max=2)
    zipcd = fields.Integer(max=5)
    county = fields.Str()
    dept = fields.Str()
    cause = fields.Str()
    brief = fields.Str()
    link = fields.Str()
