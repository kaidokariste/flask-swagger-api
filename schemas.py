from marshmallow import Schema, fields, validate


class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)  # We don't expec it from input JSON, only give it back
    name = fields.Str(required=True)  # Can be in input and output and is required always
    price = fields.Float(required=True)


class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


class PlainCpiSchema(Schema):
    id = fields.Int(dump_only=True)
    order_date = fields.Date(load_only=True)
    year = fields.Int(required=True, validate=validate.Range(min=1998, max=2025))
    month = fields.Str(required=True)
    index_value = fields.Float(required=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    store_id = fields.Int()


class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)


class StoreUpdateSchema(Schema):
    name = fields.Str()


class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema(), dump_only=True))
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)


class TagSchema(PlainTagSchema):
    store_id = fields.Int(load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)



class CpiSchema(PlainCpiSchema):
    change_to_previous_month = fields.Float(dump_only=True)
    change_to_previous_month_in_percent = fields.Float(dump_only=True)
    previous_close = fields.Float(dump_only=True)

class TagAndItemSchema(Schema):
    message = fields.Str()
    item = fields.Nested(ItemSchema)
    tag = fields.Nested(TagSchema)