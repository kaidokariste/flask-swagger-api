from marshmallow import Schema, fields

class PlainItemSchema(Schema):
    id = fields.Str(dump_only=True) # We don't expec it from input JSON, only give it back
    name = fields.Str(required=True) # Can be in input and output and is required always
    price = fields.Float(required=True)

class PlainStoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

class ItemUpdateSchema(Schema):
    name = fields.Str()
    price =  fields.Float()
    store_id = fields.Int()

class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)

class StoreUpdateSchema(Schema):
    name = fields.Str()

class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema(), dump_only=True))