# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 13:53:32 2015

@author: student
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,\
    QLineEdit, QPushButton
#from PyQT5.QtGui import QIcon
#ЗА ДОСТУП К ИНФОРМАЦИОННЫМ РЕСУРСАМ СИСТЕМЫ, А 

app=QApplication(sys.argv)

win=QWidget()
#win.setGeometry(100,100,400,300)
win.setWindowTitle("Great_Cool_Calculator")
#icon=QIcon(")
#win.setWindowIcon(icon)
#app.setWindowIcon(icon)
label = QLabel()
label.setText("Введите выражение здесь")
label.setStyleSheet("font: italic 24pt arial; color: darkcyan; \
border: 2px solid gray; background-color: yellow")

edit1=QLineEdit()
edit1.setPlaceholderText("Таки здесь")
label.setStyleSheet("font: italic 14pt consolas; color: darkcyan; \
border: 2px solid gray; background-color: red")

button=QPushButton()
button.setText("вычислить")
button

box = QVBoxLayout()
box.addWidget(label)
box.addWidget(edit1)
win.setLayout(box)


win.show()

sys.exit(app.exec_())