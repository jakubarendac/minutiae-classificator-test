from PyQt5 import QtWidgets

from gui.components.Image import Image
from gui.components.Canvas import Canvas


class Tab(QtWidgets.QWidget):
    def __init__(self, application):
        QtWidgets.QWidget.__init__(self, application)

        self.layout = QtWidgets.QVBoxLayout()
        self.image = Image(application, "image")

        self.layout.addWidget(self.image)

        self.setLayout(self.layout)
        
    def show_image(self, image, from_image):
        self.image.show_image(image, from_image)