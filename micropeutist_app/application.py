from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# import configuration class with address of connection to DB and secret key
from .config import Config 

app = Flask(__name__)

# take configuration options from Config class and initialize DB engines
app.config.from_object(Config) 
db = SQLAlchemy(app)

# should be here to avoid cirsular import
from .models.models import Doctor, Patient

migrate = Migrate(app, db)

# routes and Web controllers

from .views import web_view

#routes and RESTful service implementation
from .rest import api_view
