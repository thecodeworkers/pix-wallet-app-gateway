from flask import jsonify
from .routes import graphql_routes
from .bootstrap import app
from .constants import HOST, PORT

@app.route('/')
def welcome():
    return jsonify('Welcome Pix World')

@app.errorhandler(404)
def page_not_found(error):
    return { 'result': 'not_found' }, 404

graphql_routes()

def run_server():
    app.run(host=HOST, port=PORT)
