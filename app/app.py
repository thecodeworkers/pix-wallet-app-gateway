from flask import jsonify
from .bootstrap import app
from .routes import graphql_routes

# @app.route('/', methods=['GET'])
# def welcome():
#     print(os.urandom(16))
#     return "Hello get"

# @app.route('/', methods=['POST'])
# def welcome_post():
#     return jsonify("Hello post"), 201


@app.route('/')
def welcome():
    return jsonify('Welcome Pix World')

@app.errorhandler(404)
def page_not_found(error):
    return { 'result': 'not_found' }, 404

# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=8000)

graphql_routes()
