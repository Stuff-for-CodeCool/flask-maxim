from flask import Flask, render_template, request
from connection import delete_answe

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ceva/<int:id>")
def ceva(id):
    return render_template("form.html", titlu=id)


@app.route("/alta", methods=["POST"])
def alta():
    titlu = request.form.get("titlu", "0")
    lst = request.form.get("lst", 17)
    radio = request.form.get("radio", 1234)
    #   request.form.get("ce-e-la-name-la-input", valoare_default)

    return f"Am primit asa: titlu = {titlu}, lst = {lst}, radio = {radio}"


if __name__ == "__main__":
    app.run(debug=True)
