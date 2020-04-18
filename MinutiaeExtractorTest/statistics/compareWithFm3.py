from __future__ import division
from datetime import datetime
import os
import sys
import math

sys.path.append(os.path.realpath('../logic/'))

from MinutiaeReader import MinutiaeReader
from Engine import Engine


images_path = "/home/jakub/projects/biometric DBs/FVC_Fingerprint_DB/FVC2004/test/"
manually_extracted_path = "/home/jakub/projects/biometric DBs/FM3/test/"

RADIUSES = [15, 20, 25]
THETA_RESERVE = 25

def find_manually_extracted_file(manually_extracted, file_name):
    found_manually_extracted_file = None

    for manually_extracted_file in manually_extracted:
        if manually_extracted_file.file_name == file_name:
            found_manually_extracted_file = manually_extracted_file
            break

    return found_manually_extracted_file


def get_is_in_radius(center_x, center_y, radius, x, y):
    dist = math.sqrt((center_x - x) ** 2 + (center_y - y) ** 2)
    return dist <= radius

def get_formatted_angle(angle_to_format):
    if(angle_to_format > 180):
        return 360 - angle_to_format

    return angle_to_format

def get_has_correct_angle(manually_extracted_angle, extracted_angle):
    extracted_angle_deg = math.degrees(extracted_angle)

    formatted_extracted_angle = get_formatted_angle(extracted_angle_deg)
    found_manually_extracted_angle = get_formatted_angle(manually_extracted_angle)

    angles_difference = abs(found_manually_extracted_angle - formatted_extracted_angle)

    return angles_difference <= THETA_RESERVE

def get_is_extracted_correctly(extracted_item, manually_extracted, radius, check_angle = False):
    is_extracted_correctly = False

    for manually_extracted_item in manually_extracted.minutiae_data:
        is_in_radius = get_is_in_radius(
            manually_extracted_item.xPosition,
            manually_extracted_item.yPosition,
            radius,
            extracted_item[0],
            extracted_item[1])

        has_correct_angle = get_has_correct_angle(manually_extracted_item.theta, extracted_item[2]) if check_angle else True
            
        if is_in_radius & has_correct_angle:
            is_extracted_correctly = True
            break

    return is_extracted_correctly


def get_correctly_extracted_items(manually_extracted, extracted, radiuses):
    correctly_extracted = dict()

    correctly_extracted_by_radius = []
    correctly_extracted_angle_by_radius = []

    for radius in radiuses:
        correctly_extracted_items = []
        correctly_extracted_items_angle = []

        for extracted_item in extracted.minutiae_data:
            is_extracted_correctly = get_is_extracted_correctly(
                extracted_item, manually_extracted, radius)

            is_extracted_correctly_angle = get_is_extracted_correctly(
                extracted_item, manually_extracted, radius, check_angle = True)

            if is_extracted_correctly:
                correctly_extracted_items.append(extracted_item)

            if is_extracted_correctly_angle:
                correctly_extracted_items_angle.append(extracted_item)

        correctly_extracted_by_radius.append(correctly_extracted_items)
        correctly_extracted_angle_by_radius.append(correctly_extracted_items_angle)

    correctly_extracted['correctly_extracted_by_radius'] = correctly_extracted_by_radius
    correctly_extracted['correctly_extracted_angle_by_radius'] = correctly_extracted_angle_by_radius

    return correctly_extracted


def get_relative_values(
        manually_extracted,
        extracted,
        file_name,
        extracted_correctly_by_radius,
        output_file):
    output_file.write('File: ' + file_name + '\n')
    output = dict()
    output_values_without_angle = []
    output_values_with_angle = []

    radius = 15

    for extracted_correctly in extracted_correctly_by_radius['correctly_extracted_by_radius']:
        output_values = dict()

        correctly_extracted = len(extracted_correctly) / len(extracted)
        incorrectly_extracted = (
            len(extracted) - len(extracted_correctly)) / len(extracted)
        correctly_extracted_from_manually_extracted = len(
            extracted_correctly) / len(manually_extracted)
        not_extracted_from_manually_extracted = (
            len(manually_extracted) - len(extracted_correctly)) / len(manually_extracted)

        output_values['correctly_extracted'] = correctly_extracted
        output_values['incorrectly_extracted'] = incorrectly_extracted
        output_values['correctly_extracted_from_manually_extracted'] = correctly_extracted_from_manually_extracted
        output_values['not_extracted_from_manually_extracted'] = not_extracted_from_manually_extracted

        output_file.write('\tRadius: ' + str(radius) + '\n')
        output_file.write(
            '\tcorrectly_extracted: ' +
            str(correctly_extracted) +
            '\n')
        output_file.write(
            '\tincorrectly_extracted: ' +
            str(incorrectly_extracted) +
            '\n')
        output_file.write(
            '\tcorrectly_extracted_from_manually_extracted: ' +
            str(correctly_extracted_from_manually_extracted) +
            '\n')
        output_file.write(
            '\tnot_extracted_from_manually_extracted: ' +
            str(not_extracted_from_manually_extracted) +
            '\n')
        output_file.write('\n')

        radius += 5

        output_values_without_angle.append(output_values)

    radius = 15

    output_file.write('\tChecked angle\n\n')

    for extracted_correctly in extracted_correctly_by_radius['correctly_extracted_angle_by_radius']:
        output_values = dict()

        correctly_extracted = len(extracted_correctly) / len(extracted)
        incorrectly_extracted = (
            len(extracted) - len(extracted_correctly)) / len(extracted)
        correctly_extracted_from_manually_extracted = len(
            extracted_correctly) / len(manually_extracted)
        not_extracted_from_manually_extracted = (
            len(manually_extracted) - len(extracted_correctly)) / len(manually_extracted)

        output_values['correctly_extracted'] = correctly_extracted
        output_values['incorrectly_extracted'] = incorrectly_extracted
        output_values['correctly_extracted_from_manually_extracted'] = correctly_extracted_from_manually_extracted
        output_values['not_extracted_from_manually_extracted'] = not_extracted_from_manually_extracted

        output_file.write('\tRadius: ' + str(radius) + '\n')
        output_file.write(
            '\tcorrectly_extracted_with_angle: ' +
            str(correctly_extracted) +
            '\n')
        output_file.write(
            '\tincorrectly_extracted_with_angle: ' +
            str(incorrectly_extracted) +
            '\n')
        output_file.write(
            '\tcorrectly_extracted_from_manually_extracted_with_angle: ' +
            str(correctly_extracted_from_manually_extracted) +
            '\n')
        output_file.write(
            '\tnot_extracted_from_manually_extracted_with_angle: ' +
            str(not_extracted_from_manually_extracted) +
            '\n')
        output_file.write('\n')

        radius += 5

        output_values_with_angle.append(output_values)

    output['output_values_without_angle'] = output_values_without_angle
    output['output_values_with_angle'] = output_values_with_angle
    
    return output

sum_15_correctly_extracted = 0
sum_15_incorrectly_extracted = 0
sum_15_correctly_extracted_from_manually_extracted = 0
sum_15_not_extracted_from_manually_extracted = 0
sum_20_correctly_extracted = 0
sum_20_incorrectly_extracted = 0
sum_20_correctly_extracted_from_manually_extracted = 0
sum_20_not_extracted_from_manually_extracted = 0
sum_25_correctly_extracted = 0
sum_25_incorrectly_extracted = 0
sum_25_correctly_extracted_from_manually_extracted = 0
sum_25_not_extracted_from_manually_extracted = 0
sum_15_correctly_extracted_angle = 0
sum_15_incorrectly_extracted_angle = 0
sum_15_correctly_extracted_from_manually_extracted_angle = 0
sum_15_not_extracted_from_manually_extracted_angle = 0
sum_20_correctly_extracted_angle = 0
sum_20_incorrectly_extracted_angle = 0
sum_20_correctly_extracted_from_manually_extracted_angle = 0
sum_20_not_extracted_from_manually_extracted_angle = 0
sum_25_correctly_extracted_angle = 0
sum_25_incorrectly_extracted_angle = 0
sum_25_correctly_extracted_from_manually_extracted_angle = 0
sum_25_not_extracted_from_manually_extracted_angle = 0

minutiae_reader = MinutiaeReader()
manually_extracted = minutiae_reader.get_extracted_minutiae_data(
    manually_extracted_path)

minutiae_extractor = Engine()
minutiae_extractor.set_coarse_net_path(
    "/home/jakub/projects/minutiae-extractor/models/CoarseNet.h5")
minutiae_extractor.set_fine_net_path(
    "/home/jakub/projects/minutiae-extractor/models/FineNet.h5")
minutiae_extractor.load_extraction_module()

extracted = minutiae_extractor.get_extracted_minutiae(
    images_path, as_image=False)

date_time = datetime.now().strftime('%Y%m%d-%H%M%S')

output_file_name = 'compared_with_fm3_' + date_time + '.txt'

output_file = open(output_file_name, 'a')

for extracted_file in extracted:
    manually_extracted_file = find_manually_extracted_file(
        manually_extracted, extracted_file.file_name)

    correctly_extracted_items = get_correctly_extracted_items(
        manually_extracted_file, extracted_file, RADIUSES)

    relative_values = get_relative_values(
        manually_extracted_file.minutiae_data,
        extracted_file.minutiae_data,
        extracted_file.file_name,
        correctly_extracted_items,
        output_file)

    sum_15_correctly_extracted += relative_values['output_values_without_angle'][0]['correctly_extracted']
    sum_15_incorrectly_extracted += relative_values['output_values_without_angle'][0]['incorrectly_extracted']
    sum_15_correctly_extracted_from_manually_extracted += relative_values['output_values_without_angle'][0]['correctly_extracted_from_manually_extracted']
    sum_15_not_extracted_from_manually_extracted += relative_values['output_values_without_angle'][0]['not_extracted_from_manually_extracted']
    sum_20_correctly_extracted += relative_values['output_values_without_angle'][1]['correctly_extracted']
    sum_20_incorrectly_extracted += relative_values['output_values_without_angle'][1]['incorrectly_extracted']
    sum_20_correctly_extracted_from_manually_extracted += relative_values['output_values_without_angle'][1]['correctly_extracted_from_manually_extracted']
    sum_20_not_extracted_from_manually_extracted += relative_values['output_values_without_angle'][1]['not_extracted_from_manually_extracted']
    sum_25_correctly_extracted += relative_values['output_values_without_angle'][2]['correctly_extracted']
    sum_25_incorrectly_extracted += relative_values['output_values_without_angle'][2]['incorrectly_extracted']
    sum_25_correctly_extracted_from_manually_extracted += relative_values['output_values_without_angle'][2]['correctly_extracted_from_manually_extracted']
    sum_25_not_extracted_from_manually_extracted += relative_values['output_values_without_angle'][2]['not_extracted_from_manually_extracted']
    sum_15_correctly_extracted_angle += relative_values['output_values_with_angle'][0]['correctly_extracted']
    sum_15_incorrectly_extracted_angle += relative_values['output_values_with_angle'][0]['incorrectly_extracted']
    sum_15_correctly_extracted_from_manually_extracted_angle += relative_values['output_values_with_angle'][0]['correctly_extracted_from_manually_extracted']
    sum_15_not_extracted_from_manually_extracted_angle += relative_values['output_values_with_angle'][0]['not_extracted_from_manually_extracted']
    sum_20_correctly_extracted_angle += relative_values['output_values_with_angle'][1]['correctly_extracted']
    sum_20_incorrectly_extracted_angle += relative_values['output_values_with_angle'][1]['incorrectly_extracted']
    sum_20_correctly_extracted_from_manually_extracted_angle += relative_values['output_values_with_angle'][1]['correctly_extracted_from_manually_extracted']
    sum_20_not_extracted_from_manually_extracted_angle += relative_values['output_values_with_angle'][1]['not_extracted_from_manually_extracted']
    sum_25_correctly_extracted_angle += relative_values['output_values_with_angle'][2]['correctly_extracted']
    sum_25_incorrectly_extracted_angle += relative_values['output_values_with_angle'][2]['incorrectly_extracted']
    sum_25_correctly_extracted_from_manually_extracted_angle += relative_values['output_values_with_angle'][2]['correctly_extracted_from_manually_extracted']
    sum_25_not_extracted_from_manually_extracted_angle += relative_values['output_values_with_angle'][2]['not_extracted_from_manually_extracted']


output_file.write('Average values - radius 15: ' + '\n')
output_file.write('\taverage_correctly_extracted: ' +
                  str(sum_15_correctly_extracted / len(extracted)) + '\n')
output_file.write('\taverage_incorrectly_extracted: ' +
                  str(sum_15_incorrectly_extracted / len(extracted)) + '\n')
output_file.write('\taverage_correctly_extracted_from_manually_extracted: ' +
                  str(sum_15_correctly_extracted_from_manually_extracted / len(extracted)) + '\n')
output_file.write('\taverage_not_extracted_from_manually_extracted: ' +
                  str(sum_15_not_extracted_from_manually_extracted / len(extracted)) + '\n')
output_file.write('Average values - radius 20: ' + '\n')
output_file.write('\taverage_correctly_extracted: ' +
                  str(sum_20_correctly_extracted / len(extracted)) + '\n')
output_file.write('\taverage_incorrectly_extracted: ' +
                  str(sum_20_incorrectly_extracted / len(extracted)) + '\n')
output_file.write('\taverage_correctly_extracted_from_manually_extracted: ' +
                  str(sum_20_correctly_extracted_from_manually_extracted / len(extracted)) + '\n')
output_file.write('\taverage_not_extracted_from_manually_extracted: ' +
                  str(sum_20_not_extracted_from_manually_extracted / len(extracted)) + '\n')
output_file.write('Average values - radius 25: ' + '\n')
output_file.write('\taverage_correctly_extracted: ' +
                  str(sum_25_correctly_extracted / len(extracted)) + '\n')
output_file.write('\taverage_incorrectly_extracted: ' +
                  str(sum_25_incorrectly_extracted / len(extracted)) + '\n')
output_file.write('\taverage_correctly_extracted_from_manually_extracted: ' +
                  str(sum_25_correctly_extracted_from_manually_extracted / len(extracted)) + '\n')
output_file.write('\taverage_not_extracted_from_manually_extracted: ' +
                  str(sum_25_not_extracted_from_manually_extracted / len(extracted)) + '\n')

output_file.write('\nAverage values with angle - radius 15: ' + '\n')
output_file.write('\taverage_correctly_extracted_angle: ' +
                  str(sum_15_correctly_extracted_angle / len(extracted)) + '\n')
output_file.write('\taverage_incorrectly_extracted: ' +
                  str(sum_15_incorrectly_extracted_angle / len(extracted)) + '\n')
output_file.write('\taverage_correctly_extracted_from_manually_extracted_angle: ' +
                  str(sum_15_correctly_extracted_from_manually_extracted_angle / len(extracted)) + '\n')
output_file.write('\taverage_not_extracted_from_manually_extracted_angle: ' +
                  str(sum_15_not_extracted_from_manually_extracted_angle / len(extracted)) + '\n')
output_file.write('Average values with angle - radius 20: ' + '\n')
output_file.write('\taverage_correctly_extracted_angle: ' +
                  str(sum_20_correctly_extracted_angle / len(extracted)) + '\n')
output_file.write('\taverage_incorrectly_extracted_angle: ' +
                  str(sum_20_incorrectly_extracted_angle / len(extracted)) + '\n')
output_file.write('\taverage_correctly_extracted_from_manually_extracted_angle: ' +
                  str(sum_20_correctly_extracted_from_manually_extracted_angle / len(extracted)) + '\n')
output_file.write('\taverage_not_extracted_from_manually_extracted+_angle: ' +
                  str(sum_20_not_extracted_from_manually_extracted_angle / len(extracted)) + '\n')
output_file.write('Average values with angle - radius 25: ' + '\n')
output_file.write('\taverage_correctly_extracted_angle: ' +
                  str(sum_25_correctly_extracted_angle / len(extracted)) + '\n')
output_file.write('\taverage_incorrectly_extracted_angle: ' +
                  str(sum_25_incorrectly_extracted_angle / len(extracted)) + '\n')
output_file.write('\taverage_correctly_extracted_from_manually_extracted_angle: ' +
                  str(sum_25_correctly_extracted_from_manually_extracted_angle / len(extracted)) + '\n')
output_file.write('\taverage_not_extracted_from_manually_extracted_angle: ' +
                  str(sum_25_not_extracted_from_manually_extracted_angle / len(extracted)) + '\n')

output_file.close()

print 'preslo cele'
