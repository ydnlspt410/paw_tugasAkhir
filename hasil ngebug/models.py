# file : models.py
# definisi class untuk user dalam session

import pymysql
import config

db = cursor = None

class MPengguna():
    def __init__(self, username=None, email=None, password=None):
        self.username = username
        self.email = email
        self.password = password
        
    def openDB(self):
        global db, cursor
        db = pymysql.connect(host=config.DB_HOST, user=config.DB_USER, password=config.DB_PASS, database=config.DB_NAME)
        cursor = db.cursor()
        
    def closeDB(self):
        global db, cursor
        db.close()
        
    def auth(self):
        self.openDB()
        cursor.execute("SELECT * FROM t_kasir WHERE username = '%s' AND password = MDS('%s')") % (self.username, self.password)
        count_account = cursor.fetchone()
        self.closeDB()
        return True if count_account>0 else False
    
    def add_user(self):
        self.openDB()
        query = "INSERT INTO t_kasir (username, email, password) VALUES (%s, %s, %s)"
        values = (self.username, self.email, self.password)
        result = cursor.execute(query, values)
        db.commit()
        self.closeDB()
