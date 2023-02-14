from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'

db = SQLAlchemy(app)
class students(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))  
   addr = db.Column(db.String(200))
   pin = db.Column(db.String(10))

def __init__(self, name, city, addr,pin):
   self.name = name
   self.city = city
   self.addr = addr
   self.pin = pin

db.create_all()

# Configuring MySQL
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'password'
# app.config['MYSQL_DB'] = 'tutorial'
# mysql = MySQL(app)


@app.route("/")
def show_all():
   return render_template('show_all.html', students = students.query.all() )

# def index():
#     return render_template("index.html")

# @app.route("/response", methods=["POST"])
# def response():
#     name = request.form.get("id") + " times"
#     return render_template("index.html", name=name)

if __name__ == '__main__':
    app.run(debug=True)

