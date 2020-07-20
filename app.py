from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Movies(Resource):
    def get(self):
        return {'movies': [{'id':1, 'name':'Transformer'},{'id':2, 'name':'Avengers'}]} 

api.add_resource(Movies, '/movies') # Route_1

if __name__ == '__main__':
     app.run(port=8000)