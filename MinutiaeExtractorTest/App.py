from PyQt5 import QtWidgets
#from MinutiaeClassificator.MinutiaeExtractorWrapper import MinutiaeExtractorWrapper

from gui.Gui import Gui

class App:
    def __init__(self):
        #self.__minutiae_classificator = MinutiaeExtractorWrapper()
        self.__gui = Gui()


def main():
    App()

if __name__ == "__main__":
    main()