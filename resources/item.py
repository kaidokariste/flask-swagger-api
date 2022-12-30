import uuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import items
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("items", __name__, description="Operation on items")


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    # Main response, using ItemSchema
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted"}
        except KeyError:
            abort(404, message="Item not found")

    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):  # Decorator argument (item_data) should always go after the root (self)
        try:
            item = items[item_id]
            item |= item_data  # New dictionary update syntax
            return item
        except KeyError:
            abort(404, message="Item not found")


@blp.route("/item/")
class ItemList(MethodView):
    # As it can return many item schemas
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return {"items": items.values()}

    # @blp.arguments - Validation of incoming data.
    # Data that requestor sends, is validated against schema and then forwarded to post request as item_data argument.
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):

        for item in items.values():
            if (
                    item_data["name"] == item["name"]
                    and item_data["store_id"] == item["store_id"]
            ):
                abort(400, message="Item already exists")

        item_id = uuid.uuid4().hex
        item = {**item_data, "id": item_id}
        items[item_id] = item

        return item
