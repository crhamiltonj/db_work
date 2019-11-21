from flask import Blueprint
from flask_restplus import Api, Resource


blueprint = Blueprint('api', __name__)
api = Api(blueprint)


@api.route('/ping')
class PingResource(Resource):
    def get(self):
        return {'message': 'pong'}