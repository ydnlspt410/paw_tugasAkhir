from flask import Flask, render_template, request, redirect, url_for, session
from models import MPengguna

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234567890'

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/registrasi', methods=['GET', 'POST'])
def registrasi():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # memeriksa username sudah digunakan
        registrasi = MPengguna(username=username)
        result = registrasi.auth()
        
        if result:
            error = 'Username sudah digunakan'
            return render_template('registrasi.html', error=error)
        
        # menambahkan pengguna baru
        tambah = MPengguna(username=username, email=email, password=password)
        tambah.add_user()
        session['username'] = username
        return redirect('/login')
    
    return render_template('registrasi.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        pengguna = MPengguna(username, password)
        if pengguna.auth():
            admin = session['username'] 
            admin = username
            if admin == 'admin':
                return redirect(url_for('dash-admin'))
            return render_template('dash-kasir.html')
        msg = 'Username/Password salah'
        return render_template('login.html', msg=msg)
    return render_template('login.html')

@app.route('/dash-admin')
def dash_admin():
    return render_template('dash-admin.html')


if __name__ == '__main__':
    app.run(debug=True)
        
            