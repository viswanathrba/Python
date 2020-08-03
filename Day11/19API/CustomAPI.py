from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Ping(Resource):

    def get(self):
        return {'status': 'Success', 'ping': 'pong'}, 200

class Run(Resource):

    def post(self):
        return {'status': 'Success', 'result': 'post method success'}, 201

api.add_resource(Ping, "/stage/api/ping")
api.add_resource(Run, "/stage/api/execution")

if __name__ == '__main__':
    app.run() # By Default Local Host Ip 127.0.0.1 and Default Port Number 5000
                OR
    #app.run(host='192.168.31.97', port=5000) # Change Local Machine Ip Address 
    
