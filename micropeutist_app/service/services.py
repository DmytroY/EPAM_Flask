''' CRUD operations '''
from sqlalchemy import inspect

from ..config import db
from ..models.model import Doctor, Patient


def to_dict(obj) -> dict:
    '''this procedure returns object atributes as dictionary'''
    result = {}
    for item in inspect(obj).mapper.column_attrs:
        result[item.key] = getattr(obj, item.key)

    # result = {item: getattr(obj, item.key) for item in inspect(obj).mapper.column_attrs}
    return result


def get_doctor_list() -> list:
    ''' select all records from doctors and add patient count to each record'''
    session = db.session()
    doctors = session.query(Doctor).all()

    result_list = []
    for doc_obj in doctors:
        # convert atributes of a doctor to dict
        doc_dict = to_dict(doc_obj)
        # add related patients count
        doc_dict["patient_count"] = session.query(Patient)\
            .join(Doctor, Patient.doctor)\
            .filter(Doctor.id == doc_dict.get('id')).count()
        result_list.append(doc_dict)

    return result_list

def set_doctor(data: dict) -> str:
    '''creating new doctor record
    return either "success" or error description '''
    print("=== data:", data)
    with db.session() as session:
        # check if same email exist
        if session.query(Doctor).filter(Doctor.email == data.get('email')).count():
            return "Error. This email already exist in Doctor records"

        # creating record
        new_doctor = Doctor(**data)
        session.add(new_doctor)
        session.commit()

    # check new record exist in DB
    with db.session() as session:
        if session.query(Doctor).filter(Doctor.email == data.get('email')).count():
            return "success"
       
    return "Error. New record have not been saved"



