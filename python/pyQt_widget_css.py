from PyQt4 import QtGui, QtCore


class Notification(QtGui.QLabel):
    def __init__(self, *args, **kwargs):
        super(Notification, self).__init__(*args, **kwargs)

        self.button = QtGui.QToolButton(self)
        self.button.setIcon(QtGui.QIcon('cross.png'))
        self.button.setStyleSheet('border: 0px; padding: 0px;')
        self.button.setCursor(QtCore.Qt.ArrowCursor)
        self.button.clicked.connect(lambda: self.deleteLater())

        frame_width = self.style().pixelMetric(QtGui.QStyle.PM_DefaultFrameWidth)
        button_size = self.button.sizeHint()

        self.setStyleSheet("""padding-right: {0}px;
                            padding-left: 2px;
                            background-color: #bdbdbd;
                            border-width: 2px;
                            border-radius: 5px;
                            border-color: gray;
                            """.format(button_size.width() + frame_width + 1))

        self.setMinimumSize(
            max(self.minimumSizeHint().width(),
                button_size.width() + frame_width * 2 + 2),
            max(self.minimumSizeHint().height(),
                button_size.height() + frame_width * 2 + 2)
        )

    def resizeEvent(self, event):
        width = self.rect().right()
        height = self.rect().height()

        button_size = self.button.sizeHint()
        frame_width = self.style().pixelMetric(QtGui.QStyle.PM_DefaultFrameWidth)
        self.button.move(width - frame_width - button_size.width(),
                         height * 3 // 100)
        super(Notification, self).resizeEvent(event)


app = QtGui.QApplication([])

notif_list = []
window = QtGui.QWidget()
layout = QtGui.QVBoxLayout()
window.setLayout(layout)

for i in range(3):
    my_notif = Notification(text='\nУведомление {}\n'.format(i))
    layout.addWidget(my_notif)
    notif_list.append(my_notif)

layout.addStretch(0)
window.show()
app.exec()
