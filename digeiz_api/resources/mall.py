"""
This is a /resources/mall.py file.

This file define content to access to \
    multiple HTTP Mall methods by defining methods on our resource.
"""
from flask_restful import Resource, reqparse

from models.mall import MallModel


class Mall(Resource):
    """
        Class for the /mall/<string:name> end points.

        This class content:
            - Func to retrieve Mall data by a name.
            - Func to add new Mall to Malls database
            - Func to delete an Mall by it's name
            _ Func that update Mall data by name
        Functions will marshal it automatically
    """
    parser = reqparse.RequestParser()
    parser.add_argument('address',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('account_id',
                        type=int,
                        required=True,
                        help="Every mall needs a account_id."
                        )

    def get(self, name):
        mall = MallModel.find_by_name(name)
        if mall:
            return mall.json()
        return {'message': 'Mall not found'}, 404
        

    def post(self, name):
        """Add mall by name."""
        if MallModel.find_by_name(name):
            return {'message': "An Mall with name '{}' already exists.".format(name)}, 400

        data = Mall.parser.parse_args()

        mall = MallModel(name, **data)
        try:
            mall.save_to_db()
        except Exception as e:
            return {"message": "An error occurred inserting the mall."}, 500

        return mall.json(), 201

    def delete(self, name):
        """Delete a mall by name."""
        mall = MallModel.find_by_name(name)
        if mall:
            mall.delete_from_db()
            return {'message': "Mall with name '{}' deleted".format(name)}
        return {'message': 'mall not found.'}, 404

    def put(self, name):
        data = Mall.parser.parse_args()

        mall = MallModel.find_by_name(name)

        if mall:
            mall.address = data['address']
            mall.account_id = data['account_id']
        else:
            mall = MallModel(name, **data)

        mall.save_to_db()

        return mall.json()


class MallList(Resource):
    """
        Class for the /malls end points.

        This class content:
            - Func to retrieve all data from Malls
    """
    def get(self):
        """Retvrieve malls using pagination"""
        from app import pagination
        return {'malls': pagination.paginate(MallModel, MallModel.mall_fields())}
