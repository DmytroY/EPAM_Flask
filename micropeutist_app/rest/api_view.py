from flask import jsonify

from ..service.service import get_doctor_list
from ..application import app

@app.route("/api")
@app.route("/api/doctors")
def api():
    data = get_doctor_list()
    return jsonify(data)