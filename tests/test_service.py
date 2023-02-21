'''test cases for services '''
from sqlalchemy import String, Column, Integer

from micropeutist_app.service.services import to_dict, db
#from micropeutist_app.config import db


def test_to_dict():
    ''' testing procedure to_dict() in service module'''

    class TestModel(db.Model):
        '''Declare test Model'''
        __tablename__ = 'test_model'
        id      = Column(Integer, primary_key=True)
        name    = Column(String(30), nullable=False)
        age     = Column(Integer, nullable=False)

        def __init__(self, name, age):
            self.name = name
            self.age = age

    test_obj = TestModel("Albert", 42)

    # procedure to test
    test_dict = to_dict(test_obj)

    # check result
    assert test_dict.get("name") == "Albert"
    assert test_dict.get("age") == 42
