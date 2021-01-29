"""
/models/mall.py file
This file define the Model for 'Mall' which our data will be based on.
"""
from flask_restful import fields

from db import db
from models.unit import UnitModel


class MallModel(db.Model):
    """
        This class is an Mall model it content:
            - func that return data as json format
            - func thant look for a Mall by it's name or id
            - func to save an delete data into database
            - func that return the Resource fields for pagination
    """
    __tablename__ = 'malls'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    address = db.Column(db.String(100))

    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'))
    account = db.relationship('AccountModel')

    units = db.relationship('UnitModel', lazy='dynamic')

    def __init__(self, name, address, account_id):
        self.name = name
        self.address = address
        self.account_id = account_id

    def json(self):
        return {'name': self.name, 'address': self.address, 'units': [unit.json() for unit in self.units.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(account_id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def mall_fields():
        """Resource fields for marshalling."""
        return {
            'name': fields.String,
            'address': fields.String,
            'account_id': fields.Integer,
            'units': fields.List(fields.Nested(UnitModel.unit_fields()))
        }
