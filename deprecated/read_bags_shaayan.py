import xml.etree.ElementTree as ET
import glob
import csv
import os
from xml_parser import xml_parser

#csv file to store
#f = open('C:\\code\\internship\\csv_file.csv', 'w')
f = open('csv_file.csv', 'w')
writer = csv.writer(f)
header = ["File Name","Bags", "Annotated Bags", "Difference"]
writer.writerow(header)
#all_files = glob.glob("C:\\Users\\shaayan\\Documents\\USB_drive\Kadapa\\Kadappa_New\\*xml")
all_files = glob.glob("C:\\code\\s20_ai\\xlm_output_files\\original\\*xml")
annotated_dir = "C:\\code\\s20_ai\\xlm_output_files\\original\\annotated"

total_bags = 0
difference_of_bags = 0
total_bags_new = 0
for one_file in all_files:

    xparse = xml_parser(one_file, "bag")
    num_tags = xparse.read_number_of_tags()
    xparse.read_coordinates()


    tree = ET.parse(one_file)
    root = tree.getroot()
    bags_each_file = 0
    bags_each_file_new = 0
    for name in root.iter('name'):

        if name.text == 'bag':
            total_bags = total_bags + 1
            bags_each_file = bags_each_file + 1
            one_file_new = os.path.join(annotated_dir, os.path.basename(one_file))
            tree = ET.parse(one_file_new)
            root = tree.getroot()

        new_bags_each_file = 0
        for name2 in root.iter('name'):
            if name2.text == 'bag':
                total_bags_new = total_bags_new + 1
                bags_each_file_new = bags_each_file_new + 1

        difference_of_bags = bags_each_file - bags_each_file_new
        data = [os.path.basename(one_file_new), bags_each_file, bags_each_file_new, abs(difference_of_bags)]
        writer.writerow(data)


def get_num_of_bags(file_name):
    number_of_bags = 0


    return(number_of_bags)


"""
open command prompt in the directory
$git init
$git add --all
$git commit -m "initial commit"
"""