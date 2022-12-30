from marshmallow import Schema, fields

class ItemSchema(Schema):
    id = fields.Str(dump_only=True) # We don't expec it from input JSON, only give it back
    name = fields.Str(required=True) # Can be in input and output and is required always
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)

class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()

class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
