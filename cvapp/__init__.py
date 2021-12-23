import os
import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create database connection object
db = SQLAlchemy()

# LOGGING SETUP
logging.basicConfig(level=logging.DEBUG,
    format='%(levelname)s -- %(message)s')

# ENVIRONMENT CHECK for heroku prod/dev
herokuflag = os.getenv('ISHEROKU') # give 'None' if not found
logging.debug('Heroku EnvVariable value : {}'.format(herokuflag))
if herokuflag :
    logging.debug('Cloud environment')
else : logging.debug('Local environment')

# GET var from .env (only in localdev)
SQLPOPULATE_AT_STARTUP = True if os.getenv('SQLPOPULATE_AT_STARTUP') == 'True' else False

def register_extensions(app):
    # Connect sqlalchemy to app
    db.init_app(app)

    # LOGIN MANAGMENTS
    # login_manager = LoginManager()
    # login_manager.login_view = 'auth.login'
    # login_manager.init_app(app)
    # @login_manager.user_loader
    # def load_user(user_id):
    #     # since the user_id is just the primary key of our user table, 
    #     # use it in the query for the user
    #     return User.query.get(int(user_id))

# === CREATE APP WITH CONTEXT ===

def create_app():
    """Construct core Flask application."""
    app = Flask(__name__, instance_relative_config=False)

    # CONFIG PARAMS
    if herokuflag : app.config.from_object('config.ProdConfig')
    else : app.config.from_object('config.DevConfig')
    
    # initialise plugins
    register_extensions(app)

    # vital section : "here are all the pieces of my program"
    with app.app_context():
        #RESET DB in dev env
        if SQLPOPULATE_AT_STARTUP and not herokuflag : 
            from .models import init_db
            init_db()

        # blueprint for auth routes in our app
        from .views import routes as routes_blueprint
        app.register_blueprint(routes_blueprint)

        # others blueprints for app
        # ...

        # try out of several markdown libs
        from flaskext.markdown import Markdown
        Markdown(app)

        return app