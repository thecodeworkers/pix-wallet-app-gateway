from flask import Flask
from flask_mongoengine import MongoEngine
from ..constants import SECRET_KEY, ENVIRONMENT, DATABASE_NAME, DATABASE_HOST, DATABASE_PORT

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.env = ENVIRONMENT
app.config['MONGODB_SETTINGS'] = {
    "db": DATABASE_NAME,
    "host": DATABASE_HOST,
    "port": int(DATABASE_PORT)
}

mongo = MongoEngine(app)
