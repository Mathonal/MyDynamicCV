import os
import dotenv
from datetime import timedelta

# paths initialization
basedir = os.path.abspath(os.path.dirname(__file__))
dotenv.load_dotenv(os.path.join(basedir, '.env'))

class Config:
    """base config : common params"""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    #SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    FLASK_APP='flask_app'
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

class DevConfig(Config):
    FLASK_ENV='development'
    FLASK_DEBUG=True
    TESTING = True

class ProdConfig(Config): # HEROKU/clouds CONFIGURATION
    FLASK_ENV='production'
    FLASK_DEBUG=False
    TESTING = False
    
    SECRET_KEY = os.environ.get('SECRET_KEY')