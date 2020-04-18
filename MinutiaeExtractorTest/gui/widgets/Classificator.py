from PyQt5 import QtWidgets, QtCore, QtGui

from gui.components.Label import Label
from gui.components.Image import Image
from gui.components.Canvas import Canvas

class Classificator(QtWidgets.QVBoxLayout):
    def __init__(self, application):
        QtWidgets.QVBoxLayout.__init__(self)

        self.setSpacing(6)
        self.setObjectName("classificator")

        self.classificator_layout = QtWidgets.QVBoxLayout()
        self.classificator_layout.setSpacing(6)
        self.classificator_layout.setObjectName("classificator_layout")

        self.label_section_classification = Label(application, "label_section_classification", 20, True, 75, 'center-top')
        self.label_input_image = Label(application, "label_input_image")
        self.label_extracted_image = Label(application, "label_extracted_image")
        self.label_output_image = Label(application, "label_output_image")

        self.classificator_layout.addWidget(self.label_section_classification)
        self.classificator_layout.addWidget(self.label_input_image)

        self.input_image = Image(application, "input_image")
        self.extracted_image = Image(application, "extracted_image")
        self.output_image = Image(application, "output_image")
        self.canvas = Canvas(application)

        self.classificator_layout.addWidget(self.input_image)
        self.classificator_layout.addWidget(self.label_extracted_image)
        self.classificator_layout.addWidget(self.canvas)
        self.classificator_layout.addWidget(self.label_output_image)
        self.classificator_layout.addWidget(self.output_image)
        
        self.addLayout(self.classificator_layout)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_section_classification.setText(_translate("minutiae_classificator", "Classificator"))
        self.label_input_image.setText(_translate("minutiae_classificator", "Input image:"))
        self.label_extracted_image.setText(_translate("minutiae_classificator", "Manually extracted minutiae image:"))
        self.label_output_image.setText(_translate("minutiae_classificator", "Output image:"))
