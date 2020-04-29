from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Greeting (Resource):
    def get(self):
        return 'Square-a plane figure with four equal straight sides and four right angles.'
        #return 'This is invalid request handled by default backend, check your request path and try again'
api.add_resource(Greeting, '/') # Route_1

if __name__ == '__main__':
    app.run('0.0.0.0','3334')