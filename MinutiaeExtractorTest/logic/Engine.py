from MinutiaeClassificator.MinutiaeExtractorWrapper import MinutiaeExtractorWrapper

class Engine:
    def __init__(self):
        self.__minutiae_classificator = MinutiaeExtractorWrapper()

    def set_coarse_net_path(self, path):
        self.__minutiae_classificator.get_coarse_net_path(path)

    def set_fine_net_path(self, path):
        self.__minutiae_classificator.get_fine_net_path(path)

    def set_classify_net_path(self, path):
        self.__minutiae_classificator.get_classify_net_path(path)

    def load_modules(self):
        self.__minutiae_classificator.load_extraction_module()
        self.__minutiae_classificator.load_classification_module()

