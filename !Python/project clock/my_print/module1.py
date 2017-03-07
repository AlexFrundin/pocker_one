# -*- coding: utf-8 -*-
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget
from time import time, mktime, localtime

class Window (QWidget):
    def __init__ (self):
        super().__init__()
        loadUi("maket1.ui",self)
        self.calcPeriod()
        #это часть мне не особа понятна
        self.timer1=self.startTimer(1000)
        
    def timerEvent(self, event):
        self.calcPeriod()
     #выше специальная функция тоже не ясна   
    def calcPeriod(self):
        time1=time()
        dateX = (2016, 1, 1, 0, 0,0,4,1,0)
        time2 = mktime(dateX)
        delta = time2-time1
        x=localtime(delta)
   # QMessageBox.information(self,"Debugger", str(time1))
   #     QMessageBox.information(self,"Debugger", str(time2))
   #     QMessageBox.information(self,"Debugger", str(x))

        self.lineEdit.setText(str(x.tm_mday))
        self.lineEdit_2.setText(str(x.tm_hour))
        self.lineEdit_3.setText(str(x.tm_min))
        self.lineEdit_4.setText(str(x.tm_sec))