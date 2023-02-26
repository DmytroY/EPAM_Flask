''' CRUD operations '''
from datetime import datetime, timedelta

from ..config import db
from ..models.model import *

YEAR = timedelta(days=365, hours=6)

def get_age(patient_id) -> int:
    ''' calculate age by id of patient'''
    patient = Patient.query.filter_by(id=patient_id).first()
    patient_dict = patient_schema.dump(patient)
    birthday = datetime.strptime(patient_dict['birthday'], '%Y-%m-%d')
    return int((datetime.today() - birthday)/YEAR)

# ======= DOCTORS ======
def get_doctors() -> list:
    ''' select all records from doctors and add patient count to each record
    return type is list of dicts'''
    doctors = Doctor.query.all()
    doctor_list = doctors_schema.dump(doctors)
    # add to each doctor number of related patients
    for doctor in doctor_list:
        id = doctor["id"]
        doctor["patient_count"] = Patient.query.filter_by(doctor_id = id).count()
    return doctor_list

def create_doctor(data: dict) -> str:
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

def receive_doctor(tag: str) -> list:
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

            # add age for each patient
            for patient in doctor_dict["patients"]:
                patient['age'] = get_age(patient['id'])
        return doctor_dict
    return None

def update_doctor(data: dict) -> str:
    '''updating existing doctor record
    return either "success" or error description '''
    if data['id']:
        doctor = Doctor.query.filter_by(id=data.get('id')).first()
    else:
        doctor = Doctor.query.filter_by(email=data.get('email')).first()

    if doctor:
        doctor.first_name = data.get('first_name')
        doctor.last_name = data.get('last_name')
        doctor.grade = data.get('grade')
        doctor.specialization = data.get('specialization')
        doctor.email = data['email']
        db.session.commit()
        return 'success'
    return 'Error. No record with such key'

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

# ====== PATIENTS =======
def get_patients(**criterias: dict) -> list:
    ''' filter records from patients '''
    if not criterias:
        patients = Patient.query.all()
    elif criterias['doctor_id']:
        patients = Patient.query.\
            filter(Patient.birthday.between(criterias['birthday_since'], criterias['birthday_till'])).\
            filter(Patient.doctor_id == criterias['doctor_id']).\
            all()
    else:
        patients = Patient.query.\
            filter(Patient.birthday.between(criterias['birthday_since'], criterias['birthday_till'])).\
            all()

    patient_list = patients_schema.dump(patients)
    # add patient age and related doctor info
    for patient_dict in patient_list:
        # add age
        patient_dict['age'] = get_age(patient_dict['id'])
        # add related doctor
        doctor = Doctor.query.filter_by(id=patient_dict["doctor_id"]).first()
        if doctor:
            patient_dict["doctor"] = doctor_schema.dump(doctor)
        else:
            patient_dict["doctor"] = None
    return patient_list

def create_patient(data: dict) ->str:
    ''' creating new doctor record
    return either "success" or error description '''
    is_exist = Patient.query.filter_by(email=data.get('email')).first()
    if is_exist:
        return "Error. This email already exist in Patient records"

    # creating record
    with db.session() as session:
        new_patient = Patient(**data)
        session.add(new_patient)
        session.commit()
    return "success"

def receive_patient(tag: str) -> list:
    '''get patient info by id or by email'''
    # define what is tag and select patient data
    if tag.isdigit():
        patient = Patient.query.filter_by(id=int(tag)).first()
    else:
        patient = Patient.query.filter_by(email=tag).first()

    if patient:
        patient_dict = patient_schema.dump(patient)

        # add relative doctor
        doctor = Doctor.query.filter_by(id=patient_dict['doctor_id']).first()
        patient_dict['doctor'] = doctor
        return patient_dict
    return None

def update_patient(data: dict) -> str:
    '''updating existing patient record'''
    if data['id']:
        patient = Patient.query.filter_by(id=data.get('id')).first()
    else:
        patient = Patient.query.filter_by(email=data.get('email')).first()

    if patient:
        patient.first_name = data.get('first_name')
        patient.last_name = data.get('last_name')
        patient.gender = data.get('gender')
        patient.birthday = data.get('birthday')
        patient.health_state = data['health_state']
        patient.email = data['email']
        patient.doctor_id = data['doctor_id']
        db.session.commit()
        return 'success'
    return 'Error. No record with such key'

def delete_patient(tag: str) -> str:
    '''delete patient selected by id or by email'''
    # define what is tag and delete doctor data
    if tag.isdigit():
        patient = Patient.query.filter_by(id=int(tag)).first()
    else:
        patient = Patient.query.filter_by(email=tag).first()

    if patient:
        with db.session() as session:
            session.delete(patient)
            session.commit() 
        return "success"
    return "No such patient record in the database"
