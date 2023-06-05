import pymysql
import config

db = cursor = None

class Users:
    def __init__(self, username=None, email=None, no_telpon=None, password=None):
        self.username = username
        self.email = email
        self.no_telpon = no_telpon
        self.password = password
        
    def openDB(self):
        global db, cursor
        db = pymysql.connect(host=config.DB_HOST, user=config.DB_USER, password=config.DB_PASS, database=config.DB_NAME)
        cursor = db.cursor()

    def closeDB(self):
        global db, cursor
        db.close()
        
    def selectDB(self):
        self.openDB()
        cursor.execute("SELECT * FROM t_kasir")
        container = []
        for username, email, no_telp, password in cursor.fetchall():
            container.append((username,email,no_telp, password))
            self.closeDB()
            
        return container

    def insertDB(self, data):
        self.openDB()
        cursor.execute("INSERT INTO t_kasir (username, email, no_telp, password) VALUES ('%s', '%s', '%s', '%s')" % data)
        db.commit()
        self.closeDB()
    
    def getDBbyNo(self, no):
        self.openDB()
        cursor.execute("SELECT * FROM bukutelepon WHERE no='%s'" % no)
        data = cursor.fetchone()
        return data
    
    def updateDB(self, data):
        self.openDB()
        cursor.execute("UPDATE bukutelepon SET nama='%s', no_telp='%s' WHERE no='%s'" % data)
        db.commit()
        self.closeDB()
        
    def deleteDB(self, no):
        self.openDB()
        print("DELETE FROM bukutelepon WHERE no='%s'" % no)
        cursor.execute("DELETE FROM bukutelepon WHERE no='%s'" % no)
        db.commit()
        self.closeDB()
