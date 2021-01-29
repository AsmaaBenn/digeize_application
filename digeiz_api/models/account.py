"""
/models/account.py file
This file define the Model for 'Account' which our data will be based on.
"""
from flask_restful import fields

from db import db
from models.mall import MallModel


class AccountModel(db.Model):
    """
        This class is an Account model it content:
            - func that return data as json format
            - func thant look for an account with it's name
            - func to save an delete data into database
            - func that return the Resource fields for pagination
    """
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    malls = db.relationship('MallModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name


    def json(self):
        return {'name': self.name, 'malls': [mall.json() for mall in self.malls.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def account_filed():
        """Resource fields for marshalling."""
        return {
            'name': fields.String,
            'malls': fields.List(fields.Nested(MallModel.mall_fields()))
        }
