import os
# Database initialization
SQLPOPULATE_AT_STARTUP = False

basedir = os.path.abspath(os.path.dirname(__file__))
#print(basedir)

#testbasedir = os.path.abspath(os.path.join(basedir, os.pardir))
#print(testbasedir)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(testbasedir, 'repository/app.db')
