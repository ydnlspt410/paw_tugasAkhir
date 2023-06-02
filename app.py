from flask import Flask, render_template, request, redirect, url_for, session
from models import InventarisasiBesi as db
import mysql.connector


app = Flask(__name__)
app.secret_key = '123456789'

@app.route('/')
def homepage():
    return render_template('homepage.html')

# fungsi login
@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        cursor = db.cursor()
        cursor.execute("SELECT * FROM t_kasir WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()

        if user:
            session["username"] = username
            return redirect("/")
        else:
            return render_template("login.html", error="Username atau password salah")

    return render_template("login.html")

#fungsi registrasi 
@app.route('/registrasi', methods=['GET', 'POST'])
def registrasi():
    if request
@app.route("/dash-admin")
def dash_admin ():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
