from flask import Flask, render_template, request, redirect, session, url_for
import pymysql


app = Flask(__name__)
app.secret_key = '123456789'

# Fungsi koneksi database

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',  # kosongkan punya kalian kalau ga ada password di phpmyadmin
    database='pawl'  # nama database yang kalian buat
    )



# Fungsi untuk memeriksa keberhasilan login
def check_login(username, password):
    cursor = connection.cursor()

    # Query untuk memeriksa username dan password
    query = 'SELECT * FROM t_kasir WHERE username=%s AND password=%s'
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    
    connection.close()
    
    return result


# Fungsi untuk menambahkan pengguna baru
def add_user(username, email, no_telpon, password):
    cursor = connection.cursor()

    # Query untuk menambahkan pengguna baru
    query = 'INSERT INTO t_kasir (username, email, no_telpon, password) VALUES (%s,%s, %s, %s)'
    cursor.execute(query, (username, email, no_telpon, password))
    connection.commit()

    connection.close()


# fungsi untuk menampilkan semua data pada tabel register
def get_all_register():
    cursor = connection.cursor()

    # query untuk menampilkan
    query = 'SELECT * FROM t_kasir'
    cursor.execute(
        query,
    )
    result = cursor.fetchall()
    
    connection.close()

    return result

@app.route('/')
def homepage():
    return render_template('homepage.html')

# fungsi login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        result = check_login(username, password)

        if result:
            session['username'] = username
            return redirect(url_for('dash-admin'))
        else:
            return render_template('login.html', error='Username atau password salah')

    return render_template('login.html')


# fungsi registrasi
@app.route('/registrasi', methods=['GET', 'POST'])
def registrasi():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        no_telpon = request.form['no_telpon']
        password = request.form['password']


        # verifikasi apakah username sudah digunakan
        cursor = connection.cursor()
        query = 'SELECT * FROM t_kasir WHERE username=%s'
        cursor.execute(query, username)
        result = cursor.fetchone()

        if result:
            error = 'Username sudah digunakan'
            return render_template('register.html', error=error)

        # menambahkan pengguna baru
        add_user(username, email, no_telpon, password)
        session['username'] = username
        return redirect('/login')

    return render_template('registrasi.html')

@app.route('/dash-admin')
def dash_admin():
    return render_template('dash-admin.html')

if __name__ == '__main__':
    app.run()