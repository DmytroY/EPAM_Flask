''' ORM Models '''
from sqlalchemy import ForeignKey, String, Date, Column, Integer
from sqlalchemy.orm import relationship

from ..config import db, ma


class Doctor(db.Model): #pylint: disable=too-few-public-methods
    '''class Doctor declares Model Doctor.
    It has attributes: first_name, last_name, grade, specialization, email'''
    __tablename__ = 'doctors'

    id              = Column(Integer, primary_key=True)
    first_name      = Column(String(30), nullable=False)
    last_name       = Column(String(30), nullable=False)
    grade           = Column(String(30))
    specialization  = Column(String(30))
    email           = Column(String(30), unique=True)

    patient = relationship("Patient", back_populates="doctor")

    def __init__(self, **kwargs):
        ''' Doctor object constructor
        usage example: new_doctor = Doctor({'first_name': name1, 'last_name': name2, 'grade': somegrade, 'specialization': ddsfsd, 'email':eee@ee.ee})'''
        for key in kwargs:
            setattr(self, key, kwargs.get(key))

        # self.first_name = first_name
        # self.last_name = last_name
        # self.grade = grade
        # self.specialization = specialization
        # self.email = email


class Patient(db.Model): #pylint: disable=too-few-public-methods
    '''class Patient declares Model Patient.
    It has attributes: first_name, last_name, gender, birthday, health_state, email, doctor_id.
    Attribute doctor_id used as foreign key to Doctor class'''
    __tablename__ = 'patients'

    id              = Column(Integer, primary_key=True)
    first_name      = Column(String(30), nullable=False)
    last_name       = Column(String(30), nullable=False)
    gender          = Column(String(6))
    birthday        = Column(Date)
    health_state    = Column(String(255), nullable=True)
    email           = Column(String(30), unique=True)
    doctor_id       = Column(Integer, ForeignKey("doctors.id"))

    doctor = relationship("Doctor", back_populates="patient")

    def __init__(self, first_name, last_name, gender, birthday, health_state, email): #pylint: disable=too-many-arguments
        ''' Patient object constructor
        usage: new_patient = Patient(<first_name>, <last_name>, <gender>, <birthday>, <health_state>, <email>)'''
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.birthday = birthday
        self.health_state = health_state
        self.email = email

class DoctorSchema(ma.Schema):
    class Meta:

        fields = ('id', 'first_name', 'last_name', 'grade', 'specialization', 'email', )

class PatientSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'gender', 'birthday', 'health_state', 'email', 'doctor_id')

doctor_schema = DoctorSchema()
doctors_schema = DoctorSchema(many=True)

patient_schema = PatientSchema()
patients_schema = PatientSchema(many=True)
