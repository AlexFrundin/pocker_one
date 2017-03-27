from PyQt5.QtWidgets import (QWidget, QAction, QApplication, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QMessageBox, QMenu, QPushButton, QSpinBox, QSystemTrayIcon, QTextEdit, QVBoxLayout, QTableWidget, QTableWidgetItem, QComboBox, QAbstractItemView, QCheckBox, QTreeWidget, QTreeWidgetItem, QMainWindow, QFileSystemModel, QTreeView)
from PyQt5.QtNetwork import (QTcpServer, QTcpSocket, QHostAddress, QUdpSocket, QNetworkInterface)
from PyQt5.QtCore import (QObject, QByteArray, QDataStream, QIODevice, QAbstractItemModel, QModelIndex)
from PyQt5.QtGui import QIcon
from os import system, path, walk


class TreeUSB(QMainWindow):
    def __init__(self):
        super(TreeUSB, self).__init__()

        rootDir = 'C:\\Users\\a.frundin\\Documents\\repositoriy'
        tree = QTreeWidget(self)
        tree.setHeaderLabel(rootDir)
        for dirName, subDir, fileName in walk(rootDir):
            item = QTreeWidgetItem(tree, [subDir])



        self.setCentralWidget(tree)

if True:
    import sys
    app = QApplication(sys.argv)
    window = TreeUSB()
    window.show()
    sys.exit(app.exec_())


"""
    for files in fileName:
        QTreeWidgetItem(item, [files])
"""
