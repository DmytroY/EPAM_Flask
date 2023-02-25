''' Configuration and instansiate Flask and Database'''
import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
ma = Marshmallow(app)

# app.config['SECRET_KEY'] = os.environ.get(SECRET_KEY)
app.config['SECRET_KEY'] = 'secret_string_bla-bla-bla'

#configure DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/micropeutist'
db = SQLAlchemy(app)

MIGRATION_DIR = os.path.join('micropeutist_app', 'migrations')
migrate = Migrate(app, db, directory=MIGRATION_DIR)
