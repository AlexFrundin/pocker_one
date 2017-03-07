# -*- coding: utf-8 -*-
from sys import argv, exit
from module1 import Window
from PyQt5.QtWidgets import QApplication

if __name__=="__main__":
    app = QApplication(argv)
    win = Window()
    win.show()
    exit(app.exec_())
