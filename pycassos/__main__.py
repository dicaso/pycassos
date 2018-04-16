from flask import Flask, request
from flask_restful import Resource, Api

app = Flask('pycassos')
api = Api(app)

# Frontend
@app.route('/')
@app.route('/static/song/')
def root():
    return app.send_static_file('song/index.html')

# Backend
class DosageSensitivity(Resource):
    def get(self):
        return {'genes': [{'id':1, 'name':'BRIP1'},{'id':2, 'name':'BRCA1'}]} 

api.add_resource(DosageSensitivity, '/dosage') # Route_1

if __name__ == '__main__':
     app.run(port=4444)
