"""
This is a /resources/account.py file.

This file define content an access to \
    multiple HTTP Account methods by defining methods on our resource.
"""
from flask_restful import Resource, reqparse

from models.account import AccountModel
from models.mall import MallModel


class Account(Resource):
    """
        Class for the /mall/<string:name> end points.

        This class content:
            - Func to retrieve Account data by a name.
            - Func to add new Account to Accounts database
            - Func to delete an account by it's name
        Functions will marshal it automatically
    """

    def get(self, name):
        account = AccountModel.find_by_name(name)
        if account:
            return account.json()
        return {'message': 'Account not found'}, 404

    

    def delete(self, name):
        account = AccountModel.find_by_name(name)
        if account:
            mall = MallModel.find_by_id(account.id)
            if mall:
                mall.delete_from_db()
            account.delete_from_db()
            return {'message': "Account with name '{}' deleted".format(name)}
        return {'message': 'Account not found.'}, 404


class AccountPost(Resource):
    """
        Class for the /account end point.

        This class content:
            - Func to Add a new account to our data.
        Functions will marshal it automatically
    """
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def post(self):
        data = AccountPost.parser.parse_args()

        account = AccountModel(**data)
        try:
            account.save_to_db()
        except Exception as e:
            return {"message": "An error occurred creating the account."}, 500

        return account.json(), 201


class AccountList(Resource):
    """
        Class for the /accounts end points.

        This class content:
            - Func to retrieve all data from Accounts
    """

    def get(self):
        """Retrieve all Accounts using pagination."""
        from app import pagination
        return {'accounts': pagination.paginate(AccountModel, AccountModel.account_filed())}
