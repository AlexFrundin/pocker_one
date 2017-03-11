import sqlite3
import os



def create_DB(obj):
    db=sqlite3.connect('{}.sqlite'.format(obj.name))
    cur=db.cursor()
    cur.execute("""CREATE TABLE Contact
                    (id integer primary key autoincrement,
                     name varchar(20),
                     number_ varchar(10))
                """)
                    #cur.commit()
    cur.close()
    db.commit()
    db.close()


def update_DB(obj,name,number):
    db=sqlite3.connect('{}.sqlite'.format(obj.name))
    cur=db.cursor()
    cur.execute("INSERT INTO Contact (name, number_) values (?,?)".(name,number))
    cur.close()
    db.commit()
    db.close()


def loadToDB(obj):
    db=sqlite3.connect('{}.sqlite'.format(obj.name))
    cur=db.cursor()
    #delete ignore primary key
    cur.execute("DELETE FROM Contact")
    #format not work(((
    for name, number in obj.get_contact():
        cur.execute("INSERT INTO Contact (name,number_) values (?,?)",(name,number))
    db.commit()
    cur.close()
    db.close()

def printDB(obj):
    db=sqlite3.connect('{}.sqlite'.format(obj.name))
    cur=db.cursor()
    cur.execute("SELECT * FROM Contact")
    data=cur.fetchall()
    for i in data:
        print(i)
