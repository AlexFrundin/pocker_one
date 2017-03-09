# -*- coding: utf-8 -*-

import sys
from lib import Form1
from PyQt5.QtWidgets import QApplication

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=Form1()
    win.show()
    sys.exit(app.exec_())
