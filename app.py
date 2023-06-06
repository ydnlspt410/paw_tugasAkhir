from flask import Flask, render_template, request, redirect, session
import pymysql

app = Flask(__name__)
app.secret_key = 'secret_key'

# Fungsi koneksi database


def connect_db():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',  # kosongkan punya kalian kalau ga ada password di phpmyadmin
        database='pawl'  # nama database yang kalian buat
    )
    return conn

# Fungsi untuk memeriksa keberhasilan login


def check_login(username, password):
    conn = connect_db()
    cursor = conn.cursor()

    # Query untuk memeriksa username dan password
    query = "SELECT * FROM t_kasir WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    conn.close()

    return result

# Fungsi untuk menambahkan pengguna baru


def add_user(username, email, password):
    conn = connect_db()
    cursor = conn.cursor()

    # Query untuk menambahkan pengguna baru
    query = "INSERT INTO t_kasir (username, email, password) VALUES (%s, %s, %s)"
    cursor.execute(query, (username, email, password))
    conn.commit()

    conn.close()

# fungsi untuk menampilkan semua data pada tabel register


def get_all_register():
    conn = connect_db()
    cursor = conn.cursor()

    # query untuk menampilkan
    query = "SELECT * FROM t_kasir"
    cursor.execute(query,)
    result = cursor.fetchall()

    conn.close()

    return result
# Fungsi dashboard (hanya dapat diakses setelah login)

# Fungsi login

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        result = check_login(username, password)

        # Memeriksa keberhasilan login
        if result:
            session['username'] = username
            return redirect(url_for('dash-admin'))
            # if username == 'admin':
            #     return redirect('/dash-admin')
            # else:
            #     return redirect('/dash-kasir')
        else:
            error = 'Username atau password salah'
            return render_template('login.html', error=error)

    return render_template('login.html')

# Fungsi register


@app.route('/registrasi', methods=['GET', 'POST'])
def registrasi():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Memeriksa apakah username sudah digunakan
        conn = connect_db()
        cursor = conn.cursor()
        query = "SELECT * FROM t_kasir WHERE username=%s"
        cursor.execute(query, username)
        result = cursor.fetchone()

        if result:
            error = 'Username sudah digunakan'
            return render_template('registrasi.html', error=error)

        # Menambahkan pengguna baru
        add_user(username, password, email)
        session['username'] = username
        return redirect('/login')

    return render_template('registrasi.html')

# Fungsi logout
@app.route('/dash-admin')
def admin():
    return render_template('dash-admin.html')

@app.route('/dash-kasir')
def kasir():
    return render_template('dash-kasir.html')

@app.route('/form-input-inventaris')
def input_inventaris():
    return render_template('form-input-inventaris.html')

@app.route('/form-input-pemasok')
def input_pemasok():
    return render_template('form-input-pema.html')

@app.route('/form-input-tran')
def transaksi():
    return render_template('form-input-tran.html')

@app.route('/inven-admin')
def crud_admin():
    return render_template('inven-admin.html')

@app.route('/inven-kasir')
def crud_kasir():
    return render_template('inven-kasir.html')

@app.route('/pema-admin')
def pemasok():
    return render_template('pema-admin.html')

@app.route('/transaksi-admin')
def transaksi_admin():
    return render_template('tran-admin.html')

@app.route('/transaksi-kasir')
def transaksi_kasir():
    return render_template('tran-kasir.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')


if __name__ == '__main__':
    app.run()
