"""
This is a /resources/unit.py file.

This file define content to access to \
    multiple HTTP Unit methods by defining methods on our resource.
"""
from flask_restful import Resource, reqparse

from models.unit import UnitModel

class UnitId(Resource):
    """
        Class for the /unit/<id> end points.

        This class content:
            - Func to retrieve Unit data by a ID.
            - Func to delete an Unit by it's ID
            - Func to update Unit data by ID
        Functions will marshal it automatically
    """
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('mall_id',
                        type=int,
                        required=True,
                        help="Every unit needs a mall_id."
                        )

    def get(self, _id):
        unit = UnitModel.find_by_id(_id)
        if unit:
            return unit.json()
        return {'message': 'Unit not found'}, 404
    
    def delete(self, _id):
        """Delete a unit by id."""
        unit = UnitModel.find_by_id(_id)
        if unit:
            unit.delete_from_db()
            return {'message': "Unit with name '{}' deleted".format(unit.name)}
        return {'message': 'Unit not found.'}, 404

    def put(self, _id):
        data = UnitId.parser.parse_args()

        unit = UnitModel.find_by_id(_id)

        if unit:
            unit.name = data['name']
            unit.mall_id = data['mall_id']
        else:
            unit = UnitModel(**data)

        unit.save_to_db()

        return unit.json()


class UnitPost(Resource):
    """
        Class for the /unit end point.

        This class content:
            - Func to Add a new Unit to our data.
        Functions will marshal it automatically
    """
    parser = reqparse.RequestParser()
    parser.add_argument('mall_id',
                        type=int,
                        required=True,
                        help="Every unit needs a mall_id."
                        )

    def post(self):
        """Add new Unit by name."""
        data = UnitId.parser.parse_args()

        unit = UnitModel(**data)
        try:
            unit.save_to_db()
        except Exception as e:
            return {"message": "An error occurred inserting the unit."}, 500

        return unit.json(), 201


class UnitList(Resource):
    """
        Class for the /units end points.

        This class content:
            - Func to retrieve all data from Units
    """
    def get(self):
        """Retrieve all units using pagination."""
        from app import pagination
        return {'units': pagination.paginate(UnitModel, UnitModel.unit_fields())}
