from PyQt5 import QtWidgets

class FileDialog(QtWidgets.QFileDialog):
    def __init__(self, parent = None):
        QtWidgets.QFileDialog.__init__(self, parent)

    def open(self, label ,path = None, filter = None):
        file_name, _filter = self.getOpenFileName(self, label, path, filter)
        
        return file_name