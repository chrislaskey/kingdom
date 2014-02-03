from flask.ext.restful import Api
from .. import app
from . helloworld import HelloWorld


api = Api(app)

api.add_resource(HelloWorld, '/')
