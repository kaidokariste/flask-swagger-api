import uuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import ItemModel
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("items", __name__, description="Operation on items")


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    # Main response, using ItemSchema
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        return item

    def delete(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message":"Item deleted"}

    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):  # Decorator argument (item_data) should always go after the root (self)
        item = ItemModel.query.get(item_id)
        # if item exists, update
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        # if it does not exist, create
        else:
            item = ItemModel(id=item_id, **item_data)

        db.session.add(item)
        db.session.commit()

        return item


@blp.route("/item/")
class ItemList(MethodView):
    # As it can return many item schemas
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return ItemModel.query.all()

    # @blp.arguments - Validation of incoming data.
    # Data that requestor sends, is validated against schema and then forwarded to post request as item_data argument.
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        item = ItemModel(**item_data)

        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Error occured while insering")

        return item
