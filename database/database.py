import mysql.connector

class Database:

    def __init__(self, db_name):
        self._db_name = db_name

    def set_host(self, localhost):
        self._localhost = localhost

    def set_username(self, username):
        self._username = username

    def set_password(self, password):
        self._password = password
    
    def set_table_name(self, table_name):
        self._table_name = table_name
    
    def create_database(self):
        db = mysql.connector.connect(
            host = self._localhost,
            user = self._username,
            passwd  = self._password,
        )

        cursor = db.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS " + self._db_name)

        return "Database " + self._db_name + "telah dibuat!"
    
    def create_connection(self):
        db = mysql.connector.connect(
            host        = self._localhost,
            user        = self._username,
            password    = self._password,
            database    = self._db_name,    
        )

        self._db = db

    def create_table(self):
        self.create_connection()

        cursor = self._db.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS " + self._table_name + " (user_id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255) UNIQUE, passwd VARCHAR(255), nama VARCHAR(255), email VARCHAR(255), phone_num VARCHAR(255), tgl_lahir DATE, address VARCHAR(255), grade VARCHAR(255), date_joined  DATETIME)")

        return "Tabel " + self._table_name + " telah dibuat!"