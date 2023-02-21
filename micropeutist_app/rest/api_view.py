''' RESTfull service implementation '''
from flask import jsonify

from ..service.services import get_doctor_list
from ..config import app

@app.route("/api")
@app.route("/api/doctors")
def api():
    ''' API controller for Doctor list'''
    data = get_doctor_list()
    return jsonify(data)
