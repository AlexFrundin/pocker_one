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
    cur.close()
    db.commit()
    db.close()


def update_DB(obj,name,number):
    print("****")
    db=sqlite3.connect('{}.sqlite'.format(obj.name))
    cur=db.cursor()
    cur.execute("INSERT INTO Contact (name, number_) values (?,?)",(name,number))
    cur.close()
    db.commit()
    db.close()


def loadToDB(obj):
    db=sqlite3.connect('{}.sqlite'.format(obj.name))
    cur=db.cursor()
    #delete ignore primary key if ->cur.execute("DELETE FROM Contact")
    cur.executescript("""DROP TABLE if exists CONTACT;
                    CREATE TABLE Contact
                    (id integer primary key autoincrement,
                     name varchar(20),
                     number_ varchar(10));

    """)
    db.commit()
    for name, number in obj.get_contact():
        #format not work(((
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

def loadContact(obj):
    db=sqlite3.connect('{}.sqlite'.format(obj.name))
    cur=db.cursor()
    cur.execute("SELECT * FROM Contact")
    data=cur.fetchall()
    for item in data:
        yield (item[1:])
