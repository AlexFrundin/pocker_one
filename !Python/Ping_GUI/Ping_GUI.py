import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QToolTip,
QTextEdit, QLineEdit, QGridLayout, QVBoxLayout, QHBoxLayout,
QMessageBox, QProgressBar, QDesktopWidget, qApp, QLabel)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QBasicTimer, Qt
from ipaddress import ip_address as ip
from re import findall
from os import system, popen, path

class Example (QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        print('Labels...')
        firstIP = QLabel('First IP address:')
        lastIP = QLabel('Last IP address:')
        resultLabel = QLabel('Result:')
        
        self.firstIPedit = QLineEdit()
        self.lastIPedit = QLineEdit()
        self.resultEdit = QTextEdit()

        print('Progress bar...')	
        self.pbar = QProgressBar(self)

        print('Buttons...')
        quitButton = QPushButton('Quit', self)
        quitButton.clicked.connect(qApp.quit)
        quitButton.setToolTip('Close application')

        self.startButton = QPushButton('Start', self)
        self.startButton.clicked.connect(self.doAction)
        self.startButton.setShortcut('Enter')
        self.startButton.setToolTip('Start process')

        self.timer = QBasicTimer()
        self.step = 0

        print('Labels grid...')       
        grid = QGridLayout()   
        grid.setSpacing(10)

        grid.addWidget(firstIP, 1, 0)
        grid.addWidget(self.firstIPedit, 1, 1)
        
        grid.addWidget(lastIP, 2, 0)
        grid.addWidget(self.lastIPedit, 2, 1)

        grid.addWidget(resultLabel, 3, 0)
        grid.addWidget(self.resultEdit, 3, 1, 5, 1)

        print('Layouts...')
        hbox = QHBoxLayout()
        hbox.addWidget(self.startButton)
        hbox.addWidget(self.pbar)

        hbox.addWidget(quitButton)

        vbox = QVBoxLayout()
        vbox.addLayout(grid)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        print('Window...')
        self.center()
        self.resize(500, 300)
        self.setWindowTitle('Ping your network')
        self.setWindowIcon(QIcon('icon.png'))
        self.show()

        print('Done.')

    def center(self):
        # Always set window on the center of monitor
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def closeEvent(self, event):
        # Quit message if pressed 'X' button on top
        reply = QMessageBox.question(self, 'Message', "Are you sure to Quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes: 
            event.accept()            
        else: 
            event.ignore()

    def timerEvent(self, e):
        # Some rules for progress bar
        self.step = self.step + (100 / self.valueIP)
        self.pbar.setValue(self.step)

        if self.step >= 100:
            self.step = 0
            self.timer.stop()
            self.startButton.setText('Finished')
            return

    def doAction(self):
            print('Operation started...')
            self.resultEdit.setPlainText('')
            self.startButton.setText('Start')
            self.timer.start(100, self) # Start progress bar
            try:
                f_hn = ip(self.firstIPedit.text())
                l_hn = ip(self.lastIPedit.text())
                self.valueIP = 0
                if f_hn > l_hn:
                    tmp = f_hn
                    f_hn = l_hn
                    l_hn = tmp

            except ValueError:
                # Message if user entered incorrect address. Will break function.
                print('IP address is incorrect. Enter again.')
                QMessageBox.warning(self, 'Warning!', 'IP address is incorrect. Enter again.', QMessageBox.Cancel | QMessageBox.NoButton, QMessageBox.Cancel)
                return

            f_hn -= 1
            while f_hn != l_hn:
                # This loop need to count how will work progress bar on percentage
                f_hn += 1
                self.valueIP += 1

            f_hn -= self.valueIP
            QApplication.processEvents() # Will update QTextEdit in loop. 
            while f_hn != l_hn:
                f_hn += 1
                self.resultEdit.append('\nping ' + str(f_hn))
                result = findall('\d+', popen('ping -n 2 -w 100 ' + str(f_hn)).read()) # Make digit list from ping result
                if len(result) > 15:
                    self.resultEdit.append(str(f_hn) + ' - in use\n')
                else:
                    self.resultEdit.append(str(f_hn) + ' - is free\n')
                QApplication.processEvents()

if __name__ == '__main__':
    print('Starting application...')
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())