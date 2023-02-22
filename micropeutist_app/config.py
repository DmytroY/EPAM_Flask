''' Configuration and instansiate Flask and Database'''
import os

from flask import Flask, session
from flask_session import Session
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from tempfile import mkdtemp

app = Flask(__name__)

# app.config['SECRET_KEY'] = os.environ.get(SECRET_KEY)
app.config['SECRET_KEY'] = 'secret_string_bla-bla-bla'

# Configure session to use filesystem (instead of signed cookies)
# app.config["SESSION_FILE_DIR"] = mkdtemp()
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)

#configure DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/micropeutist'
db = SQLAlchemy(app)

MIGRATION_DIR = os.path.join('micropeutist_app', 'migrations')
migrate = Migrate(app, db, directory=MIGRATION_DIR)
