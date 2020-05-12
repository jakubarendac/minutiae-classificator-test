from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
import cv2
import matplotlib

from gui.utils.MinutiaeUtils import show_extracted_minutiae

class Canvas(FigureCanvas):
    def __init__(self, parent = None):
        fig = Figure()
 
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

 
    def plot(self, image_path, extracted_minutiae):
        image = cv2.imread(image_path, 0)
        imageData = np.squeeze(image)

        plt = self.figure.add_axes([0,0,1,1])
        plt.axis('off')
        show_extracted_minutiae(extracted_minutiae, plt)
        plt.imshow(imageData, cmap='gray')

    def save(self, image_path, extracted_minutiae):
        image = cv2.imread(image_path, 0)
        imageData = np.squeeze(image)
    
        plt.imshow(imageData,cmap='gray')
        
        plt.hold(True)
        
        show_extracted_minutiae(extracted_minutiae, plt)

        plt.axis('off')
        ax = plt.gca()
        ax.xaxis.set_major_locator(matplotlib.ticker.NullLocator())
        ax.yaxis.set_major_locator(matplotlib.ticker.NullLocator())
        plt.savefig('manually_extracted.png', pad_inches=0, transparent=True)


    def show_plot(self, image, extracted_minutiae):
        self.plot(image, extracted_minutiae)
        self.save(image, extracted_minutiae)