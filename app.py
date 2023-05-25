from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Koneksi ke database MySQL
conn = mysql.connector.connect(
    host="localhost", user="root", password="", database="transaksi"
)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nama_barang = request.form["nama_barang"]
        jenis_transaksi = request.form["jenis_transaksi"]
        jumlah = request.form["jumlah"]

        # Menyimpan data barang masuk atau keluar ke database
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO transaksi (nama_barang, jenis_transaksi, jumlah) VALUES (%s, %s, %s)",
            (nama_barang, jenis_transaksi, jumlah),
        )
        conn.commit()
        cursor.close()

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
