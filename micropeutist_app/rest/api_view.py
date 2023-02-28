''' RESTfull service implementation '''
from flask import jsonify, request

from ..service.crud import get_doctors, create_doctor
from ..service.crud import update_doctor, receive_doctor, delete_doctor
from ..service.crud import get_patients, create_patient
from ..service.crud import update_patient, receive_patient, delete_patient
from ..config import app


# ========= DOCTORS ========
@app.route('/api/')
@app.route('/api/doctors/')
def api_doctors():
    ''' API to get list of doctors'''
    return jsonify(get_doctors()), 200

@app.route("/api/create_doctor/", methods=["POST"])
def api_create_doctor():
    '''api for add new doctor'''
    data = {}
    data['first_name'] = request.form.get("first_name")
    data['last_name'] = request.form.get("last_name")
    data['grade'] = request.form.get("grade")
    data['specialization'] = request.form.get("specialization")
    data['email'] = request.form.get("email")
    feedback = create_doctor(data)
    if feedback == 'success':
        return jsonify(message='Doctor ' + data['last_name'] + ' have been added'), 201
    return jsonify(message=feedback), 409

@app.route('/api/receive_doctor/', methods=['GET'])
def api_receive_doctor():
    '''API to get a doctor data be id or by email
    usage: /api/doctor/?id=<unic id number or unic email>'''
    key = request.args.get('id')
    feedback = receive_doctor(key)
    if feedback:
        return jsonify(feedback), 200
    return jsonify(message='There is no such doctor in database'), 204

@app.route("/api/update_doctor/", methods=['PUT'])
def api_update_doctor():
    '''API to update a doctor data if email exist in records'''
    data = {}
    data['id'] = request.form.get("id")
    data['first_name'] = request.form.get("first_name")
    data['last_name'] = request.form.get("last_name")
    data['grade'] = request.form.get("grade")
    data['specialization'] = request.form.get("specialization")
    data['email'] = request.form.get("email")
    feedback = update_doctor(data)
    if feedback == 'success':
        return jsonify(message='Doctor ' + data['last_name'] + ' have been updated'), 201
    return jsonify(message=feedback), 409

@app.route("/api/delete_doctor/", methods=["DELETE"])
def api_delete_doctor():
    '''API to delete a doctor data be id or by email
    parameter in body is id=<unic id number or unic email>'''
    key = request.form.get('id')
    feedback = delete_doctor(key)
    if feedback == 'success':
        return jsonify(message='Doctor with id/email = ' + key + ' have been deleted'), 200
    return jsonify(message=feedback), 409

# ======== PATIENTS ==============
@app.route("/api/patients/")
def api_patients():
    '''API to get list of patients'''
    return jsonify(get_patients()), 200

@app.route('/api/create_patient/', methods=["POST"])
def api_create_patient():
    '''API for creating new patient'''
    data = {}
    data['first_name'] = request.form.get("first_name")
    data['last_name'] = request.form.get("last_name")
    data['gender'] = request.form.get("gender")
    data['birthday'] = request.form.get("birthday")
    data['health_state'] = request.form.get("health_state")
    data['email'] = request.form.get("email")
    data['doctor_id'] = request.form.get("doctor_id")
    feedback = create_patient(data)
    if feedback == 'success':
        return jsonify(message='Patient ' + data['last_name'] + ' have been added'), 201
    return jsonify(message=feedback), 409

@app.route('/api/receive_patient/', methods=['GET'])
def api_receive_patient():
    '''API to get a patient data be id or by email
    usage: /api/doctor/?id=<unic id number or unic email>'''
    key = request.args.get('id')
    feedback = receive_patient(key)
    if feedback:
        return jsonify(feedback), 200
    return jsonify(message='There is no such patient in database'), 204

@app.route('/api/update_patient/', methods=['PUT'])
def api_update_patient():
    '''API for updating existing patient record'''
    data = {}
    data['id'] = request.form.get("id")
    data['first_name'] = request.form.get("first_name")
    data['last_name'] = request.form.get("last_name")
    data['gender'] = request.form.get("gender")
    data['birthday'] = request.form.get("birthday")
    data['health_state'] = request.form.get("health_state")
    data['email'] = request.form.get("email")
    data['doctor_id'] = request.form.get("doctor_id")
    feedback = update_patient(data)
    if feedback == 'success':
        return jsonify(message='Patient ' + data['last_name'] + ' have been updated'), 201
    return jsonify(message=feedback), 409

@app.route('/api/delete_patient/', methods=["DELETE"])
def api_delete_patient():
    '''API for delete patient'''
    key = request.form.get('id')
    feedback = delete_patient(key)
    if feedback == 'success':
        return jsonify(message='PAtient with id/email = ' + key + ' have been deleted'), 200
    return jsonify(message=feedback), 409
