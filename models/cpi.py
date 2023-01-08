from db import db

class CpiModel(db.Model):
    __tablename__="tarbijahinnaindeks"

    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, nullable=False)
    year = db.Column(db.Integer)
    month = db.Column(db.String())
    index_value = db.Column(db.Float())
    change_to_previous_month = db.Column(db.Float())
    change_to_previous_month_in_percent = db.Column(db.Float())
    previous_close = db.Column(db.Float())
