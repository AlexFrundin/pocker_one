# -*- coding: utf-8 -*-

import sys
from lib1 import Form1
from PyQt5.QtWidgets import QApplication

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=Form1()
    sys.exit(app.exec_())
