''' RESTfull service implementation '''
from flask import jsonify, redirect, request

from ..service.services import get_doctor_list, get_doctor, set_doctor, delete_doctor, update_doctor
from ..config import app
#from ..models.model import Doctor, Patient, doctor_schema, patient_schema

# ========= DOCTORS ========
@app.route('/api')
@app.route('/api/')
@app.route('/api/doctors')
@app.route('/api/doctors/')
def api_doctor_list():
    ''' API to get list of doctors'''
    return jsonify(get_doctor_list()), 200

@app.route('/api/doctor/', methods=['GET'])
def api_receive_doctor():
    '''API to get a doctor data be id or by email
    usage: /api/doctor/?id=<unic id number or unic email>'''
    id = request.args.get('id')
    feedback = get_doctor(id)
    if feedback:
        return jsonify(feedback), 200
    return jsonify(message='There is no such doctor in database'), 204

@app.route("/api/new_doctor", methods=["POST"])
def api_create_doctor():
    '''api for add new doctor'''
    data = {}
    data['first_name'] = request.form.get("first_name")
    data['last_name'] = request.form.get("last_name")
    data['grade'] = request.form.get("grade")
    data['specialization'] = request.form.get("specialization")
    data['email'] = request.form.get("email")
    feedback = set_doctor(data)
    if feedback == 'success':
        return jsonify(message='Doctor ' + data['last_name'] + ' have been added'), 201
    return jsonify(message=feedback), 409
 
@app.route("/api/delete_doctor", methods=["DELETE"])
def api_delete_doctor():
    '''API to delete a doctor data be id or by email
    parameter in body is id=<unic id number or unic email>'''
    id = request.form.get('id')
    feedback = delete_doctor(id)
    if feedback == 'success':
        return jsonify(message='Doctor with id/email = ' +id + ' have been deleted'), 200
    return jsonify(message=feedback), 409

@app.route("/api/update_doctor", methods=['PUT'])
def api_update_doctor():
    '''API to update a doctor data if email exist in records'''
    data = {}
    data['first_name'] = request.form.get("first_name")
    data['last_name'] = request.form.get("last_name")
    data['grade'] = request.form.get("grade")
    data['specialization'] = request.form.get("specialization")
    data['email'] = request.form.get("email")
    feedback = update_doctor(data)
    if feedback == 'success':
        return jsonify(message='Doctor ' + data['last_name'] + ' have been updated'), 201
    return jsonify(message=feedback), 409

# ======== PATIENTS ==============
# @app.route('/api/patient/', methods=['GET'])
# def api_receive_patient():
#     '''API to get a patient data be id or by email
#     usage: /api/doctor/?id=<unic id number or unic email>'''
#     id = request.args.get('id')
#     feedback = get_patient(id)
#     if feedback:
#         return jsonify(feedback), 200
#     return jsonify(message='There is no such doctor in database'), 204