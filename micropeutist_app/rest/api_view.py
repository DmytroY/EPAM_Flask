from flask import jsonify

from ..service.services import get_doctor_list
from ..config import app

@app.route("/api")
@app.route("/api/doctors")
def api():
    data = get_doctor_list()
    return jsonify(data)