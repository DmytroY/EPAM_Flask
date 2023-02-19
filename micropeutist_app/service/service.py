from sqlalchemy import inspect

from ..application import db
from ..models.models import Doctor, Patient



def to_dict(obj):
    '''this procedure reseived an object selected from DB
    and return object atributes as dictionary'''
    result = {}
    for item in inspect(obj).mapper.column_attrs:
        result[item.key] = getattr(obj, item.key)
    return result


def get_doctor_list():
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
