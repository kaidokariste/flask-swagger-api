from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import CpiModel
from schemas import CpiSchema

blp = Blueprint("Consumer price index", __name__, description="Operation on Consumer price index (CPI)")


@blp.route("/cpi/")
class CpiList(MethodView):
    # As it can return many item schemas
    @blp.response(200, CpiSchema(many=True))
    def get(self):
        """Get all monthly consumer price indexes (CPI) 1997=100

        Return CPI and comparison from previous month in index points and in percentages.
        ---
        Internal comment not meant to be exposed.
        """
        return CpiModel.query.all()

    @blp.arguments(CpiSchema)
    @blp.response(201, CpiSchema)
    def post(self, cpi_data):
        """Post corresponding month consumer price index

        Specify also order_date which should match numerically year and month. Day can be freely choosen.
        ---
        Internal comment not meant to be exposed.
        """
        ind = CpiModel(**cpi_data)

        try:
            db.session.add(ind)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Error occured while insering")

        return ind

@blp.route("/cpi/<string:cpi_id>")
class Cpi(MethodView):
    def delete(self, cpi_id):
        ind = CpiModel.query.get_or_404(cpi_id)
        db.session.delete(ind)
        db.session.commit()
        return {"message":"CPI deleted"}

