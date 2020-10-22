import os
from flask import Flask

from .views import app
from . import models

SQLPOPULATE_AT_STARTUP = True

# Connect sqlalchemy to app
models.db.init_app(app)


if SQLPOPULATE_AT_STARTUP :
    #@app.cli.command()
    #def init_db():
    models.init_db()