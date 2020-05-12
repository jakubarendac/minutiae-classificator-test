import os
from MinutiaeClassificator.MinutiaeClassificatorWrapper import MinutiaeClassificator
from MinutiaeClassificator.exceptions.MinutiaeClassificatorExceptions import CoarseNetPathMissingException, FineNetPathMissingException, ClassifyNetPathMissingException, MinutiaeNetNotLoadedException, ClassifyNetNotLoadedException

class Minutiae:
    def __init__(self, file_name, minutiae_data):
        self.file_name = file_name
        self.minutiae_data = minutiae_data

    def print_data(self):
        print("name: ", self.file_name, " data: ", self.minutiae_data.shape[0]) 

class Engine:
    def __init__(self):
        self.__minutiae_classificator = MinutiaeClassificator()

    def set_coarse_net_path(self, path):
        self.__minutiae_classificator.get_coarse_net_path(path)

    def set_fine_net_path(self, path):
        self.__minutiae_classificator.get_fine_net_path(path)

    def set_classify_net_path(self, path):
        self.__minutiae_classificator.get_classify_net_path(path)

    def load_extraction_module(self):
        try:
            self.__minutiae_classificator.load_extraction_module()
            print 'loaded extraction module'

        except CoarseNetPathMissingException:
            print 'coarse net missing'
        except FineNetPathMissingException:
            print 'fine net missing'

    def load_classification_module(self):
        try:
            self.__minutiae_classificator.load_classification_module()
            print 'loaded classification module'

        except ClassifyNetPathMissingException:
            print 'classify net missing'

    def load_modules(self):
        self.load_extraction_module()
        self.load_classification_module()

        print 'loaded both modules'

    def get_extracted_minutiae(self, image_folder,as_image = True):
        minutiae_files = []

        for subdir, dirs, files in os.walk(image_folder):
            for file_name in files:
                file_path = image_folder + file_name

                minutiae_data = self.get_single_extracted_minutiae(file_path, as_image)

                file_name_without_extension = os.path.splitext(os.path.basename(file_name))[0]
                minutiae = Minutiae(file_name_without_extension, minutiae_data)
                minutiae_files.append(minutiae)

        return minutiae_files
    
    def get_single_extracted_minutiae(self, image_path, as_image = True):
        try:
            return self.__minutiae_classificator.get_extracted_minutiae(image_path, as_image)
        except MinutiaeNetNotLoadedException:
            print 'extraction module not loaded'


    def get_single_classified_minutiae(self, image_path,as_image = True):
        try:
            return self.__minutiae_classificator.get_extracted_and_classified_minutiae(image_path, as_image)
        except MinutiaeNetNotLoadedException:
            print 'extraction module not loaded'
            
        except ClassifyNetNotLoadedException:
            print 'classification module not loaded'


