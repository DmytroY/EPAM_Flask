from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/response", methods=["POST"])
def response():
    name = request.form.get("id") + " times"
    return render_template("index.html", name=name)

if __name__ == '__main__':
    app.run(debug=True)

