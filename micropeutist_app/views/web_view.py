from flask import render_template, redirect, request

from ..service.services import get_doctor_list
from ..config import app


@app.route("/")
@app.route("/doctors")
def doctors():
    data = get_doctor_list()
    return render_template("doctor_list.html", data=data)

@app.route("/new_doctor", methods=["GET", "POST"])
def new_doctor():
    if request.method == "POST":
        pass
        return redirect("/")
    else:
        return render_template("new_doctor.html")
    
