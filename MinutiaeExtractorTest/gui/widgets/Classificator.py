from PyQt5 import QtWidgets, QtCore, QtGui

from gui.components.Label import Label
from gui.components.Canvas import Canvas
from gui.components.Tab import Tab

class Classificator(QtWidgets.QVBoxLayout):
    def __init__(self, application):
        QtWidgets.QVBoxLayout.__init__(self)

        self.setSpacing(6)
        self.setObjectName("classificator")

        self.classificator_layout = QtWidgets.QVBoxLayout()
        self.classificator_layout.setSpacing(6)
        self.classificator_layout.setObjectName("classificator_layout")

        self.label_section_classification = Label(application, "label_section_classification", 20, True, 75, 'center-top')

        self.classificator_layout.addWidget(self.label_section_classification)

        self.tabs = QtWidgets.QTabWidget()
        self.input_image_tab = Tab(application)
        self.extracted_image_tab = Tab(application)
        self.output_image_tab = Tab(application)

        self.tabs.addTab(self.input_image_tab, 'Input image')
        self.tabs.addTab(self.extracted_image_tab, 'Manually extracted minutiae image')
        self.tabs.addTab(self.output_image_tab, 'Output image')
        self.classificator_layout.addWidget(self.tabs)
        
        self.addLayout(self.classificator_layout)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_section_classification.setText(_translate("minutiae_classificator", "Classificator"))
