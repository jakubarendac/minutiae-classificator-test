import numpy as np
import matplotlib.pyplot as plt

def show_extracted_minutiae(minutiae_data, plt):
    if(len(minutiae_data) > 0):
        for minutiae in minutiae_data:
            print minutiae.xPosition, minutiae.yPosition
            plt.plot(minutiae.xPosition, minutiae.yPosition, 'rs', fillstyle='none', linewidth=1)
            # plt.plot([minutiae.xPosition, minutiae.xPosition+r*np.cos(o)], [minutiae.yPosition, minutiae.yPosition+r*np.sin(o)], 'r-')
            # if drawScore == True:
            #     plt.text(x - 10, y - 10, '%.2f' % s, color='yellow', fontsize=4)