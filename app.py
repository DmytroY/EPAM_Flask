from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuring MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'tutorial'
mysql = MySQL(app)

@app.route('/')
def users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT user, host FROM mysql.user''')
    rv = cur.fetchall()
    return str(rv)

# @app.route("/")
# def index():

#     return render_template("index.html")

# @app.route("/response", methods=["POST"])
# def response():
#     name = request.form.get("id") + " times"
#     return render_template("index.html", name=name)

if __name__ == '__main__':
    app.run(debug=True)

