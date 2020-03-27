from PyQt5 import QtWidgets

class Button(QtWidgets.QPushButton):
    def __init__(self, parent, name, handleClick):
        QtWidgets.QPushButton.__init__(self, parent)

        self.setObjectName(name)
        self.clicked.connect(handleClick)

    def set_is_disabled(self):
        self.setEnabled(False)