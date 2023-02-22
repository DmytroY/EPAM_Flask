''' RESTfull service implementation '''
from flask import jsonify

from ..service.services import get_doctor_list
from ..config import app

@app.route("/api")
@app.route("/api/doctors")
def api_doctors():
    ''' API controller for Doctor list'''
    data = get_doctor_list()
    return jsonify(data), 201

@app.route("/api/new_doctor", methods=["GET", "POST"])
def api_new_doctor():
    '''api for add new doctor'''

