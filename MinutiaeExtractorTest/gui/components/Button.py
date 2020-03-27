from PyQt5 import QtWidgets

class Button(QtWidgets.QPushButton):
    def __init__(self, parent, name):
        QtWidgets.QPushButton.__init__(self, parent)

        self.setObjectName(name)