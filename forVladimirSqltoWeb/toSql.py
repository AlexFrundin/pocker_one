import sqlite3

def print_db():
    db = sqlite3.connect('one.sqlite')
    cur = db.cursor()
    cur.execute("SELECT * FROM Contact")
    data = cur.fetchall()
    for i in data:
        yield i
