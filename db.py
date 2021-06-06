import sqlite3

class Database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        sql=("""
        CREATE TABLE IF NOT EXISTS system(
            id Integer Primary Key,
            application text,
            username text,
            password text
        )
        """)
        self.cur.execute(sql)
        self.con.commit()

    def insert(self,application,username,password):
        self.cur.execute("INSERT INTO system values(NULL,?,?,?)", (application,username,password))
        self.con.commit()
    def fetch(self):
        self.cur.execute("SELECT * from system")
        rows=self.cur.fetchall()
        return rows

    def remove(self,id):
        self.cur.execute("delete from system where id=?",(id,))
        self.con.commit()

    def update(self, id, application, username, password):
        data = (application, username, password, id)
        self.cur.execute(
            "update system set application=?, username=?, password=? where id=?",
                         data)
        self.con.commit()

    def readPasswords(self, user):
        self.cur.execute("SELECT application,username,password FROM system WHERE username='" + user + "'")
        passwords = self.cur.fetchall()
        return passwords


