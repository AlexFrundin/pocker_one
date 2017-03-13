import pymysql
from PyQt5.QtWidgets import QWidget

class DB():
    def __init__(self, db):
        self.__cursor=db.cursor()
        self.__a=None

    def setA(a):
        self.__a=a

    def getA():
        return self.__a

    a=property(getA,setA)


    def commadDB(comand):
        self.cursor.execute(comand)

    def returnText(self):
        b=[]
        for row in self.cursor:
            a=[]
            for item in row:
                a.append(str(item))
            b.append(' '.join(a))
        return ' '.join(b)

obj=DB("local host")
obj.a=5
print(obj.a)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.my_db=DB("local")
        self.my_db.commadDB("select")
        self.initUI()

    def InitUI():
        pass
