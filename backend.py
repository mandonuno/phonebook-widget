import sqlite3


class Database:
    """Database Class which stores function calls
    to connect, insert, view, search, and delete items
    in SQL database
    """
    def __init__(self, db):
        """Connects and creates the contacts db"""
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS\
                          phonebook (id INTEGER PRIMARY KEY,\
                          first text,\
                          last text,\
                          cell integer,\
                          email text)")
        self.conn.commit()

    def insert(self, first, last, cell, email):
        """Inserts data into contacts db"""
        self.cur.execute("INSERT INTO phonebook VALUES (NULL, ?, ?, ?, ?)",
                         (first, last, cell, email))
        self.conn.commit()

    def view(self):
        """Allows you to view all contacts"""
        self.cur.execute("SELECT * FROM phonebook")
        rows = self.cur.fetchall()
        return rows

    def search(self, first="", last="", cell="", email=""):
        """Searches database for given contact"""
        self.cur.execute("SELECT * FROM phonebook\
                          WHERE first=? OR last=? OR cell=? OR email=?",
                         (first, last, cell, email))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        """Deletes items from database"""
        self.cur.execute("DELETE FROM phonebook WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, first, last, cell, email):
        """Updates database entries"""
        self.cur.execute("UPDATE phonebook\
                          SET first=?, last=?, cell=?, email=? WHERE id=?",
                         (first, last, cell, email, id))
        self.conn.commit()

    def __del__(self):
        """Closes connection to database"""
        self.conn.close()
