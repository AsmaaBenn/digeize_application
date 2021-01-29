"""
Application Main file.

In the gigeiz_api/app.py file, define an entry point \
    for running the application.
"""
from flask import Flask
from flask_restful import Api
from flask_rest_paginate import Pagination

from resources.mall import Mall, MallList
from resources.account import Account, AccountList, AccountPost
from resources.unit import UnitId, UnitPost, UnitList
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

api = Api(app)
db.init_app(app)

# Configurations for Paginate
# app.config['PAGINATE_PAGE_SIZE'] = 5
pagination = Pagination(app, db)


@app.before_first_request
def create_tables():
    """Create our data base."""
    db.create_all()


@app.route('/')
def get_stores():
    """Welcome massage."""
    return "Welcome to this fantastic app!"

# Endpoints that can accept multiple resources in a single call.
api.add_resource(MallList, '/malls')
api.add_resource(Mall, '/mall/<string:name>')

api.add_resource(AccountList, '/accounts')
api.add_resource(Account, '/account/<string:name>')
api.add_resource(AccountPost, '/account')

api.add_resource(UnitList, '/units')
api.add_resource(UnitId, '/unit/<int:_id>')
api.add_resource(UnitPost, '/unit')

if __name__ == '__main__':
    app.run(port=5000)