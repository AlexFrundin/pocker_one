# -*- coding: utf-8 -*-
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget,QMessageBox

class Window (QWidget):
    def __init__ (self):
        super().__init__()
        loadUi("maket2.ui",self)
        
        #self.listWidget.addItem("Вася = Пупкин")
        
        self.readData()
        
        self.pushButton.clicked.connect(self.slot1)
        self.pushButton_2.clicked.connect(self.slot2)
        self.pushButton_3.clicked.connect(self.slot3)
        
    def readData(self):
        f1 = open("contacts.txt","r")
        s = f1.read()
        f1.close()
        
        a = s.split("\n")
        N = len(a)
        
        self.listWidget.clear()        
        
        if N!=0:
            for i in range(N):
                self.listWidget.addItem(a[i])
       
    def slot1(self):
        cname = self.lineEdit.text()
        cdata= self.lineEdit_2.text()
        if len(cname)==0 or len(cdata)==0:
              QMessageBox.warning(self, "Warning", "Empty field")
        else:
              record = cname + " => " +cdata
              self.listWidget.addItem(record)
              f2 =open ("contacts.txt", "a")
              f2.write("\n"+record)
              f2.close()
              
    def slot2(self):
          pass
    def slot3(self):
          pass