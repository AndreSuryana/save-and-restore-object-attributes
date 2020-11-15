import mysql.connector
import datetime as dt

class Action:
    
    def __init__(self):
        self._localhost     = "localhost"
        self._username      = "root"
        self._password      = ""
        self._db_name       = "tugas_individu_akun_sekuy"
        self._table_name    = "akun_pelajar"
        self.create_connection()

    def create_connection(self):
        db = mysql.connector.connect(
            host     = self._localhost,
            user     = self._username,
            passwd   = self._password,
            database = self._db_name,
        )

        self._db = db

    def save(self, username, passwd, nama, email, phone_num, tgl_lahir, address, grade):
        date_joined = dt.datetime.now()
        val = (username, passwd, nama, email, phone_num, tgl_lahir, address, grade, date_joined)
        
        cursor = self._db.cursor()
        cursor.execute("INSERT INTO " + self._table_name + " (username, passwd, nama, email, phone_num, tgl_lahir, address, grade, date_joined) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", val)
        
        self._db.commit()

        print(cursor.rowcount, "record telah berhasil disimpan!")

    def restore(self, username):
        cursor = self._db.cursor()

        cursor.execute("SELECT * FROM " + self._table_name + " WHERE username = '%s'" % username)

        result = cursor.fetchall()

        return result