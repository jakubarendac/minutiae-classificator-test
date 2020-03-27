from PyQt5 import QtWidgets, QtGui, QtCore

class Label(QtWidgets.QLabel):
    def __init__(self, parent, name, size = 10, is_bold = False, weight = -1 , alignment='left-center'):
        super(Label, self).__init__(parent)

        font = QtGui.QFont()
        font.setPointSize(size)
        font.setBold(is_bold)
        font.setWeight(weight)

        self.setFont(font)
        self.setAlignment(self.set_alignment(alignment))
        self.setObjectName(name)

    def set_alignment(self, alignment):
        switcher = {
            'center-center': QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter,
            'center-top': QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop,
            'center-bottom': QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom,
            'left-center': QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter,
            'left-top': QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop,
            'left-bottom': QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom,
            'right-center': QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter,
            'right-top': QtCore.Qt.AlignRight|QtCore.Qt.AlignTop,
            'right-bottom': QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom,
        }

        return switcher.get(alignment, None)
