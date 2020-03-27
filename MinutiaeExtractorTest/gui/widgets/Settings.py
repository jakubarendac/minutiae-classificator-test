from PyQt5 import QtWidgets, QtCore

from gui.components.Button import Button
from gui.components.Label import Label

class Settings(QtWidgets.QVBoxLayout):
    def __init__(self, application):
        QtWidgets.QVBoxLayout.__init__(self)

        self.setSpacing(6)
        self.setObjectName("settings")

        self.settings_layout = QtWidgets.QVBoxLayout()
        self.settings_layout.setSpacing(6)
        self.settings_layout.setObjectName("settings_layout")

        self.label_section_settings = Label(application, "label_section_settings", 20, True, 75, 'center-top')
        self.settings_layout.addWidget(self.label_section_settings)

        self.label_architectures = Label(application, "label_architectures")
        self.settings_layout.addWidget(self.label_architectures)

        self.button_coarse_net = Button(application, "button_coarse_net")
        self.settings_layout.addWidget(self.button_coarse_net)

        self.button_fine_net = Button(application, "button_fine_net")
        self.settings_layout.addWidget(self.button_fine_net)

        self.button_classify_net = Button(application, "button_classify_net")
        self.settings_layout.addWidget(self.button_classify_net)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.settings_layout.addItem(spacerItem)

        self.label_load_network = Label(application, "label_load_network")
        self.settings_layout.addWidget(self.label_load_network)

        self.button_load_network = Button(application, "button_load_network")
        self.settings_layout.addWidget(self.button_load_network)
        
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.settings_layout.addItem(spacerItem1)

        self.label_do_the_job = Label(application, "label_do_the_job")
        self.settings_layout.addWidget(self.label_do_the_job)

        self.button_choose_image = Button(application, "button_choose_image")
        self.settings_layout.addWidget(self.button_choose_image)

        self.button_extract = Button(application, "button_extract")
        self.settings_layout.addWidget(self.button_extract)

        self.button_classify = Button(application, "button_classify")
        self.settings_layout.addWidget(self.button_classify)
        
        self.addLayout(self.settings_layout)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_section_settings.setText(_translate("minutiae_classificator", "Settings"))
        self.label_architectures.setText(_translate("minutiae_classificator", "Choose architectures: "))
        self.button_coarse_net.setText(_translate("minutiae_classificator", " CoarseNet architecture"))
        self.button_fine_net.setText(_translate("minutiae_classificator", "FineNet architecture"))
        self.button_classify_net.setText(_translate("minutiae_classificator", "ClassifyNet architecture"))
        self.label_load_network.setText(_translate("minutiae_classificator", "Load neural networks:"))
        self.button_load_network.setText(_translate("minutiae_classificator", "Load Minutiae Classificator"))
        self.label_do_the_job.setText(_translate("minutiae_classificator", "Do the job:"))
        self.button_choose_image.setText(_translate("minutiae_classificator", "Choose minutiae image"))
        self.button_extract.setText(_translate("minutiae_classificator", "Extract minutiae !"))
        self.button_classify.setText(_translate("minutiae_classificator", "Classify minutiae !"))
