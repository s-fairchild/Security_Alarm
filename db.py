import sqlite3
from time import strftime, gmtime

class Sqlite3Db:
    def __init__(self, filedb='alarm.db'):
        self.filedb = filedb
        self.init_database()
        self.lastrowid = 0
    
    def create_connection(self):
        try:        
            conn = sqlite3.connect(self.filedb)
            cursor = conn.cursor()
            return conn, cursor
        except Exception as e:
            print(f"Unable to connect to sqlite3 database {self.filedb}, {e}")
    
    def init_database(self):
        conn, cursor = self.create_connection()
        create_table = """ CREATE TABLE IF NOT EXISTS alarm(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    created DATETIME DEFAULT CURRENT_TIMESTAMP,
                    start_time TIMESTAMP,
                    end_time TIMESTAMP
                    ); """
        cursor.execute(create_table)
        conn.commit()
        cursor.close()

    def save_start_time(self):
        conn, cursor = self.create_connection()
        new_row = f""" INSERT INTO alarm(created, start_time) VALUES(\"{strftime("%Y-%m-%d %H:%M:%S", gmtime())}\",\
                \"{strftime("%H:%M:%S", gmtime())}\"); """
        cursor.execute(new_row)
        self.lastrowid = cursor.lastrowid
        conn.commit()
        conn.close()

    def save_end_time(self):
        conn, cursor = self.create_connection()
        row = f""" UPDATE alarm SET end_time = \"{strftime("%H:%M:%S", gmtime())}\" where id = {self.lastrowid} """
        cursor.execute(row)
        conn.commit()
        conn.close()