import os
import struct

from bitstring import BitArray

MINUTIAE_DATA_LENGTH = 6
THETA_RESOLUTION = 1.40625

def split_array(arr, size):
     arrs = []
     while len(arr) > size:
         pice = arr[:size]
         arrs.append(pice)
         arr   = arr[size:]
     arrs.append(arr)
     return arrs

def to_bin(string):
    res = ''
    for char in string:
        tmp = bin(ord(char))[2:]
        tmp = '%08d' %int(tmp)
        res += tmp
    return res

def remove_first_bits(string):
    s = list(string)

    s[0] = '0'
    s[1] = '0'

    return "".join(s)


def get_position_value(arr_position):
    bin_part_1 = to_bin(arr_position[0])
    bin_part_2 = to_bin(arr_position[1])
    masked_bin_part_1 = remove_first_bits(bin_part_1)

    binary_value = BitArray(bin=masked_bin_part_1+bin_part_2)

    return binary_value.uint

def get_minutiae_data(arr):
    xPosition = get_position_value(arr[0:2])
    yPosition = get_position_value(arr[2:4])
    theta = ord(arr[4]) * THETA_RESOLUTION
    quality = ord(arr[5])

    data = MinutiaeData(xPosition, yPosition, theta, quality)

    return data

class Minutiae:
    def __init__(self, file_name, minutiae_data):
        self.file_name = file_name
        self.minutiae_data = minutiae_data

    def print_data(self):
        print("name: ", self.file_name, " data: ", len(self.minutiae_data)) 

class MinutiaeData:
    def __init__(self, xPosition, yPosition, theta, quality):
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.theta = theta
        self.quality = quality

    def print_data(self):
        print("X: ", self.xPosition, " Y: ", self.yPosition, " theta: ", self.theta, " quality: ", self.quality) 

class MinutiaeReader:
    def __init__(self):
        pass

    def get_single_extracted_minutiae_data(self, file_path):
        minutiae_data = []

        with open(file_path, "rb") as file:
            file_data = list(file.read())
        
            raw_minutiae_data = file_data[28:-2]

            minutiae_data_list = split_array(raw_minutiae_data, MINUTIAE_DATA_LENGTH)

            for minutiae_data_item in minutiae_data_list:
                single_minutiae_data = get_minutiae_data(minutiae_data_item)
                minutiae_data.append(single_minutiae_data)

        return minutiae_data

    def get_extracted_minutiae_data(self, folder_path):
        minutiae_files = []

        for subdir, dirs, files in os.walk(folder_path):
            for file_name in files:
                file_path = folder_path + file_name

                minutiae_data = self.get_single_extracted_minutiae_data(file_path)

                file_name_without_extension = os.path.splitext(os.path.basename(file_name))[0]
                minutiae = Minutiae(file_name_without_extension, minutiae_data)
                minutiae_files.append(minutiae) 

        return minutiae_files 