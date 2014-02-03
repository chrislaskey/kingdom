from flask import Flask, g, request
from flask.ext.restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):

    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
