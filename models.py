import pymysql
import config

db = cursor = None

class InventarisasiBesi:
    def __init__(self, no, id_produk, nama, harga, tanggal, total, kategori):
        self.no = no
        self.id_produk = id_produk
        self.nama = nama
        self.harga = harga
        self.tanggal = tanggal
        self.total = total
        self.kategori = kategori

    def openDB(self):
        global db, cursor
        db = pymysql.connect(host=config.DB_HOST, user=config.DB_USER, password=config.DB_PASS, database=config.DB_NAME)
        cursor = db,cursor()

    def closeDB(self):
        global db, cursor
        db.close()

    def selectDB(self):
        self.openDB()
        cursor.execute("SELECT * FROM t_produk")
        container = []
        for no,id_produk, nama, harga, tanggal, total, kategori in cursor.fetchall():
            container.append((no, id_produk, nama, harga, tanggal, total, kategori))
        self.closeDB()
        return container
    
    def insertDB(self, data):
        self.openDB()
        cursor.execute("INSERT INTO t_produk (id_produk, nama, harga, tanggal, total, kategori) VALUES ('%s', '%s')" % data)
        db.commit()
        self.closeDB()

    def updateDB(self, data):
        self.openDB()
        cursor.execute("UPDATE t_produk SET id_produk='%s', nama='%s', harga='%s', tanggal='%s', total='%s', kategori='%s' WHERE no='%s'" % data)
        db.commit()
        self.closeDB()

    def deleteDB(self, no):
        self.openDB()
        print("DELETE FROM t_produk WHERE no='%s'" % no)
        cursor.execute("DELETE FROM t_produk WHERE no='%s'" % no)
        db.commit()
        self.closeDB()