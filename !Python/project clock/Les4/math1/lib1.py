# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QLineEdit,\
    QPushButton, QTextEdit
#from PyQT4.QtCore import QObject, SIGNAL
class Form1(QWidget):#класс наследование от родителя QWidget    
    def __init__(self):#"""Конструктор класса"""
        super().__init__()
        self.createWidgets()
        self.packWidgets()
        self.createWindow()
        self.configSlots()
        
    def createWidgets(self):
        self.label1= QLabel("Введите коэффициенты уравнения:")
        self.label2= QLabel("a=")
        self.label3= QLabel("b=")
        self.label4= QLabel("c=")
        self.edit1=QLineEdit()
        self.edit2=QLineEdit()
        self.edit3=QLineEdit()
        self.button1=QPushButton("Решить уравнение")
        self.button2=QPushButton("Очистить поля")
        self.edit4=QTextEdit()
    
    def packWidgets(self):
        grid=QGridLayout(self)
        grid.addWidget(self.label1,0,0,1,2)#объединение ячеек
        grid.addWidget(self.label2,1,0)
        grid.addWidget(self.label3,2,0)
        grid.addWidget(self.label4,3,0)
        grid.addWidget(self.edit1,1,1)
        grid.addWidget(self.edit2,2,1)
        grid.addWidget(self.edit3,3,1)
        grid.addWidget(self.button1,4,0,1,2)
        grid.addWidget(self.button2,5,0,1,2)
        grid.addWidget(self.edit4,6,0,1,2)
    
    def createWindow(self):
        self.setStyleSheet("font: italic 11pt arial")
        self.setWindowTitle("Решение квадратных уравнений")
        self.show()
        
    def configSlots(self):
        self.button1.clicked.connect(self.slot1)
        self.button2.clicked.connect(self.slot2)
#QOBject.connect(self.button1, SIGNAL("clicked()"),sef.slot1)  for Qt4    
    def slot1(self):
        a =float(self.edit1.text())
        b =float(self.edit2.text())
        c =float(self.edit3.text())
        self.edit4.append("В этом поле будет ответ")
        
    def slot2(self):
        self.edit1.clear()
        self.edit2.clear()
        self.edit3.clear()