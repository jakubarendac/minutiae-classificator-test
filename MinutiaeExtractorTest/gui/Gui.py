import sys

from PyQt5 import QtCore, QtWidgets

from widgets.Settings import Settings
from.widgets.Classificator import Classificator

class Ui_minutiae_classificator(object):

    def setupUi(self, minutiae_classificator, engine):
        minutiae_classificator.setObjectName("minutiae_classificator")
        minutiae_classificator.resize(968, 709)
        minutiae_classificator.setToolTipDuration(0)

        self.application = QtWidgets.QWidget(minutiae_classificator)
        self.application.setObjectName("application")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.application)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.settings = Settings(self.application, engine)
        self.classificator = Classificator(self.application)
        self.horizontalLayout.addLayout(self.settings)
        self.horizontalLayout.addLayout(self.classificator)

        minutiae_classificator.setCentralWidget(self.application)

        self.retranslateUi(minutiae_classificator)
        self.settings.retranslateUi()
        self.classificator.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(minutiae_classificator)

    def retranslateUi(self, minutiae_classificator):
        _translate = QtCore.QCoreApplication.translate
        minutiae_classificator.setWindowTitle(_translate("minutiae_classificator", "Minutiae Classificator"))


class Gui:
    def __init__(self, engine):
        app = QtWidgets.QApplication(sys.argv)
        minutiae_classificator = QtWidgets.QMainWindow()
        ui = Ui_minutiae_classificator()
        ui.setupUi(minutiae_classificator, engine)
        minutiae_classificator.show()
        sys.exit(app.exec_())
