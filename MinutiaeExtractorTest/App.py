from gui.Gui import Gui
from logic.Engine import Engine
from logic.MinutiaeReader import MinutiaeReader

class App:
    def __init__(self):
        self.__engine = Engine()
        self.__minutiae_reader = MinutiaeReader()
        self.__gui = Gui(self.__engine, self.__minutiae_reader)


def main():
    App()

if __name__ == "__main__":
    main()