import xml.etree.ElementTree as ET
import glob
import os
import re


def compare_bags():
    old_dir = os.path.abspath('xml_files/original/*.xml')
    new_dir = os.path.abspath('xml_files/annotated/*.xml')
    output_file = "csv_files\\bag_output.csv"

    old_data = []
    new_data = []

    for filepath in glob.iglob(old_dir):
        #old_data.append(os.path.basename(filepath))
        old_data.append(filepath)

    for filepath2 in glob.iglob(new_dir):
        #new_data.append(os.path.basename(filepath2))
        new_data.append(filepath2)

    old_data.sort(key=lambda var:[int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', var)]) #numerical order
    new_data.sort(key=lambda var:[int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', var)]) #numerical order

    # print(old_data)

    f = open(output_file, "w")
    f.write("file_name,index,bags_model,bags_after_annotation,Annotations")
    f.write("\n")
    f.close()

    i = 0
    while i < len(old_data):
        tree = ET.parse(old_data[i])
        root = tree.getroot()

        oldBagCount = 0
        for name in root.iter('name'):
            oldBagCount += 1
        #print(os.path.basename(old_data[i]) + ',' + str(oldBagCount))


        tree2 = ET.parse(new_data[i])
        root2 = tree2.getroot()

        newBagCount = 0
        for name in root2.iter('name'):
            newBagCount += 1
        #print(os.path.basename(new_data[i]) + ',' + str(newBagCount))

        #if(newBagCount > oldBagCount):
        f = open(output_file, "a")
        f.write(os.path.basename(old_data[i]) + ',' + str(i) + ',' + str(oldBagCount) + ',' + str(newBagCount) + ',' + str(newBagCount - oldBagCount)) #old filename, new filename, how many more bags it has
        f.write('\n')

        i += 1

    f.close()


if __name__ == "__main__":
    compare_bags()