''' ORM Models '''
from sqlalchemy import ForeignKey, String, Date, Column, Integer
from sqlalchemy.orm import relationship

from ..config import db


class Doctor(db.Model): #pylint: disable=too-few-public-methods
    '''Declare Model Doctor'''
    __tablename__ = 'doctors'

    id              = Column(Integer, primary_key=True)
    first_name      = Column(String(30), nullable=False)
    last_name       = Column(String(30), nullable=False)
    grade           = Column(String(30))
    specialization  = Column(String(30))
    email           = Column(String(30))

    patient = relationship("Patient", back_populates="doctor")

    def __init__(self, first_name, last_name, grade, specialization, email): #pylint: disable=too-many-arguments
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade
        self.specialization = specialization
        self.email = email


class Patient(db.Model): #pylint: disable=too-few-public-methods
    '''Declare Model Patient'''
    __tablename__ = 'patients'

    id              = Column(Integer, primary_key=True)
    first_name      = Column(String(30), nullable=False)
    last_name       = Column(String(30), nullable=False)
    gender          = Column(String(6))
    birthday        = Column(Date)
    health_state    = Column(String(255), nullable=True)
    email           = Column(String(30))
    doctor_id       = Column(Integer, ForeignKey("doctors.id"))

    doctor = relationship("Doctor", back_populates="patient")

    def __init__(self, first_name, last_name, gender, birthday, health_state, email): #pylint: disable=too-many-arguments
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.birthday = birthday
        self.health_state = health_state
        self.email = email
