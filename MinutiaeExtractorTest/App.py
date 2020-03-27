from gui.Gui import Gui
from logic.Engine import Engine

class App:
    def __init__(self):
        self.__engine = Engine()
        self.__gui = Gui(self.__engine)


def main():
    App()

if __name__ == "__main__":
    main()