from PyQt5 import QtWidgets, QtGui
from PIL.ImageQt import ImageQt

class Image(QtWidgets.QGraphicsView):
    def __init__(self, parent, name):
        QtWidgets.QGraphicsView.__init__(self, parent)

        self.setObjectName(name)
        self.scene = QtWidgets.QGraphicsScene() 
        self.setScene(self.scene)

    def show_image(self, image, from_image = False):
        if from_image:
            qt_image = ImageQt(image)
            self.scene.addPixmap(QtGui.QPixmap.fromImage(qt_image))
        else:
            self.scene.addPixmap(QtGui.QPixmap(image))
