import os
import xml.etree.ElementTree as ET
import glob
import csv
#print(os.path.isdir("C:\\Users\\Piyali\\Documents\\garza\\annotations"))  #seeing if path is directory

#file_list = list(glob.glob("C:\\Users\\Piyali\\Documents\\garza\\annotations\\*"))

def num_bags_from_xml():

    file_list = list(glob.glob("C:\\code\\s20_ai\\xlm_output_files\\original\\*"))
    dir_annotation = "C:\\code\\s20_ai\\xlm_output_files\\annotated"
    csv_file = open('file_and_bags.csv', 'w', encoding='UTF8', newline='')
    fieldnames = ['file_name', 'bags',"bags_after","changes"]

    #for annotated bags/files
    total_bags_annotated=0
    bag_for_file_annotated = 0
    rows =[]
    #for original bags/files
    total_bags=0
    bag_for_file = 0

    for one_file in file_list:

        #read the original file
        tree = ET.parse(one_file)
        root = tree.getroot()
        bag_for_file = 0
        for child in root.iter("name"):
            #print(child.tag, child.text)
            total_bags = total_bags + 1
            bag_for_file = bag_for_file + 1
        #print(bag_for_file)
        exact_filename = os.path.basename(one_file)

        #other_one_file =
        #do the same for bags after
        annotated_file = os.path.join(dir_annotation,exact_filename)
        tree = ET.parse(annotated_file)
        root = tree.getroot()
        bag_for_file_annotated = 0
        for child in root.iter("name"):
            #print(child.tag, child.text)
            total_bags_annotated = total_bags_annotated + 1
            bag_for_file_annotated = bag_for_file_annotated + 1
        #print(bag_for_file_annotated)

        rows.append({'file_name': exact_filename, 'bags': bag_for_file, 'bags_after': bag_for_file_annotated, "changes": (bag_for_file_annotated- bag_for_file)})

    #write data to csv file
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

    print(total_bags)
    csv_file.close()
    return

def read_num_bags_from_file(file_name):
    num_of_bag = 0
    #your code here
    return(num_of_bag)



if __name__ == "__main__":
    dir_original = "C:\\code\\practice\Kadappa_New\\*"
    dir_annotation = "C:\\code\\practice\\kadapa_New_annotation"
    csv_file_name = 'file_and_bags.csv'
    num_bags_from_xml()


"""
open command prompt in the directory
$git init
$git add --all
$git commit -m "initial commit"
"""