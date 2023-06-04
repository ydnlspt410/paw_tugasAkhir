from flask import Flask, render_template, request, redirect, url_for, session
import pymysql


app = Flask(__name__)
app.secret_key = "123456789"


# Fungsi koneksi database
def connect_db():
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="",  # kosongkan punya kalian kalau ga ada password di phpmyadmin
        database="pawl",  # nama database yang kalian buat
    )
    return db


# Fungsi untuk memeriksa keberhasilan login
def check_login(username, password):
    db = connect_db()
    cursor = db.cursor()

    # Query untuk memeriksa username dan password
    query = "SELECT * FROM t_kasir WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    db.close()

    return result


# Fungsi untuk menambahkan pengguna baru
def add_user(username, email, no_telpon, password):
    usr = connect_db()
    cursor = usr.cursor()

    # Query untuk menambahkan pengguna baru
    query = "INSERT INTO Register (username, email, no_telpon, password) VALUES (%s,%s, %s, %s)"
    cursor.execute(query, (username, email, no_telpon, password))
    usr.commit()

    usr.close()


# fungsi untuk menampilkan semua data pada tabel register
def get_all_register():
    reg = connect_db()
    cursor = reg.cursor()

    # query untuk menampilkan
    query = "SELECT * FROM t_kasir"
    cursor.execute(
        query,
    )
    result = cursor.fetchall()

    reg.close()

    return result


@app.route("/")
def homepage():
    return render_template("homepage.html")


# fungsi login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        result = check_login(username, password)

        if result:
            session["username"] = username
            return redirect("/")
        else:
            return render_template("login.html", error="Username atau password salah")

    return render_template("login.html")


# fungsi registrasi
@app.route("/registrasi", methods=["GET", "POST"])
def registrasi():
    if request.method == "POST":
        username = request.form["username"]
        email = request.fotm["email"]
        no_telpon = request.form["no_telpon"]
        password = request.form["password"]


        # verifikasi apakah username sudah digunakan
        db = connect_db()
        cursor = db.curs or ()
        query = "SELECT * FROM t_kasir WHERE username=%s"
        cursor.execute(query, username)
        result = cursor.fetchone()

        if result:
            error = "Username sudah digunakan"
            return render_template("register.html", error=error)

        # menambahkan pengguna baru
        add_user(username, email, password, no_telpon)
        session["username"] = username
        return redirect("/login")

    return render_template("register.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
