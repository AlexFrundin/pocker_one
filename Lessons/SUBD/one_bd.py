import sqlite3

db=sqlite3.connect('db.sqlite')

cur=db.cursor()

cur.execute("""CREATE TABLE Contact
(id integer primary key autoincrement, name varchar(20), number_ varchar(10))
""")
