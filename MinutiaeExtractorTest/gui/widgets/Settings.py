from PyQt5 import QtWidgets, QtCore

from gui.components.Button import Button
from gui.components.Label import Label
from gui.components.FileDialog import FileDialog

class Settings(QtWidgets.QVBoxLayout):
    def __init__(self, application, engine):
        QtWidgets.QVBoxLayout.__init__(self)

        self.engine = engine

        self.setSpacing(6)
        self.setObjectName("settings")

        self.settings_layout = QtWidgets.QVBoxLayout()
        self.settings_layout.setSpacing(6)
        self.settings_layout.setObjectName("settings_layout")

        self.label_section_settings = Label(application, "label_section_settings", 20, True, 75, 'center-top')
        self.settings_layout.addWidget(self.label_section_settings)

        self.label_architectures = Label(application, "label_architectures")
        self.settings_layout.addWidget(self.label_architectures)

        self.button_coarse_net = Button(application, "button_coarse_net", self.handle_coarse_net_button_clicked)
        self.settings_layout.addWidget(self.button_coarse_net)

        self.button_fine_net = Button(application, "button_fine_net", self.handle_fine_net_button_clicked)
        self.settings_layout.addWidget(self.button_fine_net)

        self.button_classify_net = Button(application, "button_classify_net", self.handle_classify_net_button_clicked)
        self.settings_layout.addWidget(self.button_classify_net)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.settings_layout.addItem(spacerItem)

        self.label_load_network = Label(application, "label_load_network")
        self.settings_layout.addWidget(self.label_load_network)

        self.button_load_network = Button(application, "button_load_network", self.handle_load_network_modules_button_clicked)
        self.settings_layout.addWidget(self.button_load_network)
        
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.settings_layout.addItem(spacerItem1)

        self.label_do_the_job = Label(application, "label_do_the_job")
        self.settings_layout.addWidget(self.label_do_the_job)

        self.button_choose_image = Button(application, "button_choose_image", self.handle_choose_image_button_clicked)
        self.settings_layout.addWidget(self.button_choose_image)

        self.button_extract = Button(application, "button_extract", self.handle_get_extracted_minutiae)
        self.settings_layout.addWidget(self.button_extract)

        self.button_classify = Button(application, "button_classify", self.handle_get_classified_minutiae)
        self.settings_layout.addWidget(self.button_classify)

        self.button_save_processed_image = Button(application, "button_save_processed_image", self.handle_save_processed_image)
        self.settings_layout.addWidget(self.button_save_processed_image)

        self.dialog = FileDialog()

        self.addLayout(self.settings_layout)

    def set_classificator(self, classificator):
        self.classificator = classificator

    def handle_coarse_net_button_clicked(self):
        coarse_net_path = self.dialog.open("Select CoarseNet pretrained path", None, "H5 files (*.h5)")

        self.engine.set_coarse_net_path(coarse_net_path)
    
    def handle_fine_net_button_clicked(self):
        fine_net_path = self.dialog.open("Select FineNet pretrained path", None, "H5 files (*.h5)")

        self.engine.set_fine_net_path(fine_net_path)

    def handle_classify_net_button_clicked(self):
        classify_net_path = self.dialog.open("Select ClassifyNet pretrained path", None, "H5 files (*.h5)")

        self.engine.set_classify_net_path(classify_net_path)

    def handle_load_network_modules_button_clicked(self):
        self.button_load_network.set_is_disabled()
        
        self.engine.load_modules()


    def handle_choose_image_button_clicked(self):
        input_image = self.dialog.open("Select input image", None, "Images (*.png *.tif)")

        self.classificator.input_image.show_image(input_image)
        self.input_image = input_image

    def handle_get_extracted_minutiae(self):
        extracted_minutiae_image = self.engine.get_extracted_minutiae(self.input_image)

        self.classificator.output_image.show_image(extracted_minutiae_image, True)
        self.processed_image = extracted_minutiae_image

    def handle_get_classified_minutiae(self):
        classified_minutiae_image = self.engine.get_classified_minutiae(self.input_image)

        self.classificator.output_image.show_image(classified_minutiae_image, True)
        self.processed_image = classified_minutiae_image

    def handle_save_processed_image(self):
        self.processed_image.save("processed.png")

       
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
        self.button_save_processed_image.setText(_translate("minutiae_classificator", "Save processed image"))
