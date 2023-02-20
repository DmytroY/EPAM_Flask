import os

# class Config(object):
#     # SECRET_KEY = os.environ.get(SECRET_KEY) or "secret_string_bla-bla-bla"
#     SECRET_KEY = "secret_string_bla-bla-bla"

#     # configure DB connection
#     SQLALCHEMY_DATABASE_URI = 'mysql://root:mysqlpass@localhost/micropeutist'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysqlpass@localhost/micropeutist'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)

MIGRATION_DIR = os.path.join('micropeutist_app', 'migrations')
migrate = Migrate(app, db, directory=MIGRATION_DIR)