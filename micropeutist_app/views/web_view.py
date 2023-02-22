''' WEB controller '''
from flask import render_template, redirect, request, flash

from ..service.services import get_doctor_list, set_doctor
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
    