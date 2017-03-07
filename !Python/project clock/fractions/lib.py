# -*- coding: utf-8 -*-

from PyQt5.uic import loadUi #функция загрузки макета
from PyQt5.QtWidgets import QWidget, QMessageBox
from fractions import Fraction
class Form1 (QWidget):
    def __init__(self):
        super().__init__()
        loadUi("form1.ui",self)
        self.pushButton.clicked.connect(self.slot1)
    
    def slot1(self):
        try:
            a= int(self.lineEdit.text())
            b= int(self.lineEdit_2.text())
            c= int(self.lineEdit_3.text())
            d= int(self.lineEdit_4.text())
            if b==0:
                QMessageBox.critical(self,"Error","На ноль делить нельзя")
                self.lineEdit_2.setFocus()
            if d==0:
                QMessageBox.critical(self,"Error","На ноль делить нельзя")
                self.lineEdit_4.setFocus()
        
            if (self.radioButton.isChecked()):
                st="+"
                x=Fraction(a,b)+Fraction(c,d)
                
            elif (self.radioButton_2.isChecked()):
                st="-"
                x=Fraction(a,b)-Fraction(c,d)
                
            elif (self.radioButton_3.isChecked()):
                st="*"
                x=Fraction(a,b)*Fraction(c,d)
              
               
            elif (self.radioButton_4.isChecked()):
                if c==0:
                    QMessageBox.critical(self,"Error","На ноль делить нельзя")
                    self.lineEdit_3.setFocus()
                st="/"
                x=Fraction(a,b)/Fraction(c,d)
            else:
                QMessageBox.ctitical(self,"Error","Не выбрано действие")
            
            num = x.numerator
            denom = x.denominator
            #логика для корректного вывода дроби
            if num==0:
                cel="0"
                denom=0
            elif num<0 and abs(num)<=denom:
                cel="-"
                num*=-1
            elif num<0 and abs(num) > denom:
                num*=-1                
                i=num//denom
                num=num-(i*denom)
                if num==0:
                    num=1
                cel=str(i)
                cel="-"+cel
            elif num>denom:
                i=num//denom
                num=num-i*denom
                if num==0:
                    num=1
                cel=str(i)
            else:
                cel=" "
                
            self.lineEdit_7.setText(cel)
            self.lineEdit_5.setText(str(num))
            self.lineEdit_6.setText(str(denom))
            self.textEdit.append("\n"+str(a)+"  "+str(b)+"     "+str(num)+"\n"+chr(151)+st+chr(151)+"="+str(cel)+"\n"+str(c)+"  "+str(d)+"     "+str(denom))
        
        except:
            QMessageBox.critical(self,"Error","Так нельзя")
           # self.lineEdit.setFocus()
           # self.lineEdit.setText("Int")
            
   