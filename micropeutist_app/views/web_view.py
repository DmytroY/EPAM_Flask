''' WEB controller '''
from flask import render_template, redirect, request, flash

from ..service.services import get_doctor_list, set_doctor, get_doctor
from ..config import app


@app.route("/")
@app.route("/doctors")
def doctors():
    '''list of doctors'''
    data = get_doctor_list()
    return render_template("doctor_list.html", data=data)

@app.route("/new_doctor", methods=["GET", "POST"])
def new_doctor():
    '''add new doctor'''
    if request.method == "POST":
        data = {}
        data['first_name'] = request.form.get("first_name")
        data['last_name'] = request.form.get("last_name")
        data['grade'] = request.form.get("grade")
        data['specialization'] = request.form.get("specialization")
        data['email'] = request.form.get("email")
        feedback = set_doctor(data)
        if feedback == 'success':
            flash('New doctor record created!',  category='message')
        else: flash(feedback, category='error')
        return redirect("/")
    return render_template("new_doctor.html")

@app.route('/doctor', methods=['GET'])
def doctor():
    '''Show a doctor data be id or by email
    usage: /doctor/?id=<unic id number or unic email>'''
    id = request.args.get('id')
    print("=== I AM HERE, id =", id)
    doctor_list = get_doctor(id)
    return render_template("doctor.html", data=doctor_list)
