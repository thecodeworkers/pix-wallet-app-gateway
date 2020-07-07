from flask import jsonify
from app.bootstrap import app

app.secret_key = b'\x83]\xe5\xe6Fy@\xfe\xa6V\xb9\xd2\t\x9dl\xdd'

@app.route('/', methods=['GET'])
def welcome():
    print(os.urandom(16))
    return "Hello get"

@app.route('/', methods=['POST'])
def welcome_post():
    return jsonify("Hello post"), 201

@app.errorhandler(404)
def page_not_found(error):
    return { 'result': 'not_found' }, 404

# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=8000)
