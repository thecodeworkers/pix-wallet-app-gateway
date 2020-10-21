import os
from os.path import join, dirname
from dotenv import load_dotenv

path = os.path.dirname(dirname(__file__))
dotenv_path = join(path, '.env')

load_dotenv(dotenv_path)

SECRET_KEY = os.getenv('SECRET_KEY', '')
SECURE_SERVER = os.getenv('SECURE_SERVER', 'True')

HOST = os.getenv('HOST', '127.0.0.1')
PORT = os.getenv('PORT', 5000)

DEBUG = os.getenv('DEBUG', False)
ENVIRONMENT = os.getenv('ENVIRONMENT', 'production')

RESOURCES_HOST = os.getenv('RESOURCES_HOST', 'localhost:50051')
PROVIDERS_HOST = os.getenv('RESOURCES_HOST', 'localhost:50052')
COUNTRIES_HOST = os.getenv('COUNTRIES_HOST', 'localhost:50053')
BANKS_HOST = os.getenv('BANKS_HOST', 'localhost:50054')
USERS_HOST = os.getenv('USERS_HOST', 'localhost:50055')
