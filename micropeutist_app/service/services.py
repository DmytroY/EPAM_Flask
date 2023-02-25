''' CRUD operations '''
#from sqlalchemy import inspect
from datetime import datetime, date, timedelta

from ..config import db
from ..models.model import *

def get_doctor_list() -> list:
    ''' select all records from doctors and add patient count to each record
    return type is list of dicts'''
    doctors = Doctor.query.all()
    doctor_list = doctors_schema.dump(doctors)
    # add to each doctor number of related patients
    for doctor in doctor_list:
        id = doctor["id"]
        doctor["patient_count"] = Patient.query.filter_by(doctor_id = id).count()
    return doctor_list


def get_doctor(tag: str) -> list:
    '''get doctor info by id or by email'''
    # define what is tag and select doctor data
    if tag.isdigit():
        doctor = Doctor.query.filter_by(id=int(tag)).first()
    else:
        doctor = Doctor.query.filter_by(email=tag).first()

    if doctor:
        doctor_dict = doctor_schema.dump(doctor)

        # add list of related patients
        patients = Patient.query.filter_by(doctor_id=doctor_dict['id']).all()
        if patients:
            doctor_dict["patients"] = patients_schema.dump(patients)

        # calculate age of each patient
        YEAR = timedelta(days=365, hours=6)
        for patient in doctor_dict["patients"]:
            birthday = datetime.strptime(patient['birthday'], '%Y-%m-%d')
            patient['age'] = int((datetime.today() - birthday)/YEAR)
            # print("=== birthday :", patient['birthday'])
            # print("=== date.now() ",date.today() )
            # patient['age'] = date.now() - patient['birthday']
            # print("=== patient['age']", patient['age'])
        return doctor_dict
    return None


def set_doctor(data: dict) -> str:
    '''creating new doctor record
    return either "success" or error description '''
    is_exist = Doctor.query.filter_by(email=data.get('email')).first()
    if is_exist:
        return "Error. This email already exist in Doctor records"

    # creating record
    with db.session() as session:
        new_doctor = Doctor(**data)
        session.add(new_doctor)
        session.commit()
        return "success"


def update_doctor(data: dict) -> str:
    '''updating existing doctor record
    return either "success" or error description '''
    doctor = Doctor.query.filter_by(email=data.get('email')).first()
    if doctor:
        doctor.first_name = data.get('first_name')
        doctor.last_name = data.get('last_name')
        doctor.grade = data.get('grade')
        doctor.specialization = data.get('specialization')
        db.session.commit()
        return 'success'
    return 'Error. No record with such email'


def delete_doctor(tag: str) -> str:
    '''delete doctor selected by id or by email'''
    # define what is tag and delete doctor data
    if tag.isdigit():
        doctor = Doctor.query.filter_by(id=int(tag)).first()
    else:
        doctor = Doctor.query.filter_by(email=tag).first()

    if doctor:
        with db.session() as session:
            session.delete(doctor)
            session.commit() 
        return "success"
    return "No such doctor record in the database"