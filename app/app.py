from flask import jsonify
from .routes import graphql_routes
from .bootstrap import app

@app.route('/')
def welcome():
    return jsonify('Welcome Pix World')

@app.route('/graphql/')
def welcome_graph():
    return jsonify('Welcome Pix GraphQL')

@app.errorhandler(404)
def page_not_found(error):
    return { 'result': 'not_found' }, 404

graphql_routes()

# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=8000)
