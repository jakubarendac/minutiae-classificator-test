from PyQt5 import QtWidgets, QtGui

class Image(QtWidgets.QGraphicsView):
    def __init__(self, parent, name):
        QtWidgets.QGraphicsView.__init__(self, parent)

        self.setObjectName(name)
        self.scene = QtWidgets.QGraphicsScene() 
        self.setScene(self.scene)

    def show_image(self, image_path):
        self.scene.addPixmap(QtGui.QPixmap(image_path))
