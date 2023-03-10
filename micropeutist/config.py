''' Configuration and instansiate Flask and Database'''
import os
from logging.config import dictConfig
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# config logging
dictConfig({
    "version": 1,
    "formatters": {
        "default":{
            "format":
            "[%(asctime)s] %(levelname)s. modul %(module)s, function %(funcName)s: %(message)s",
        }
    },
    "handlers": {
        "size-rotate": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "micropeutist.log",
            "maxBytes": 1000000,
            "backupCount": 5,
            "formatter": "default",
        },
        "console": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "default",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "micropeutist.log",
            "formatter": "default",
        }
    },
    "root": {"level": "DEBUG", "handlers": ["console", "size-rotate"]}
})

app = Flask(__name__)
ma = Marshmallow(app)

# app.config['SECRET_KEY'] = os.environ.get(SECRET_KEY)
app.config['SECRET_KEY'] ="SoMe very unique and very secret key"

#configure DB
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
if not DB_PASS:
    DB_PASS = ''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{DB_USER}:{DB_PASS}@localhost/micropeutist'
db = SQLAlchemy(app)

MIGRATION_DIR = os.path.join('micropeutist', 'migrations')
migrate = Migrate(app, db, directory=MIGRATION_DIR)
