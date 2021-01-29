"""
/models/unit.py file
This file define the Model for 'Unit' which our data will be based on.
"""
from flask_restful import fields

from db import db


class UnitModel(db.Model):
    """
        This class is an Unit model it content:
            - fun that return data as json format
            - fun thant look for a Unit with it's name or Id
            - fun to save an delete data into database
            - fun that return the Resource fields for pagination
    """
    __tablename__ = 'units'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    mall_id = db.Column(db.Integer, db.ForeignKey('malls.id'))
    mall = db.relationship('MallModel')

    def __init__(self, name, mall_id):
        self.name = name
        self.mall_id = mall_id

    def json(self):
        return {'name': self.name}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def unit_fields():
        """Resource fields for marshalling."""
        return {
            'name': fields.String,
            'mall_id': fields.Integer
        }
