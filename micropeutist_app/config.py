''' Configuration and instansiate Flask and Database'''
import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/micropeutist'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

MIGRATION_DIR = os.path.join('micropeutist_app', 'migrations')
migrate = Migrate(app, db, directory=MIGRATION_DIR)
