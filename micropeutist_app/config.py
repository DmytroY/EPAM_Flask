# import os

class Config(object):
    # SECRET_KEY = os.environ.get(SECRET_KEY) or "secret_string_bla-bla-bla"
    SECRET_KEY = "secret_string_bla-bla-bla"

    # configure DB connection
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysqlpass@localhost/micropeutist'
    SQLALCHEMY_TRACK_MODIFICATIONS = False