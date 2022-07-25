import xml.etree.ElementTree as ET
import glob
import os
import re
import numpy as np

def size_comparison():
    old_dir = os.path.abspath('s20_ai/xlm_output_files/original/*.xml')
    new_dir = os.path.abspath('s20_ai/xlm_output_files/annotated/*.xml')
    old_data = []
    new_data = []

    for filepath in glob.iglob(old_dir):
        #old_data.append(os.path.basename(filepath))
        old_data.append(filepath)

    for filepath2 in glob.iglob(new_dir):
        #new_data.append(os.path.basename(filepath2))
        new_data.append(filepath2)

    f = open("sizeof_model_vs_annotation.csv", "w")
    f.write("index,size_model,size_annotation")
    f.write('\n')
    f.close()



    i = 0
    while i < len(old_data):
        xMin = []
        xMax = []
        yMin = []
        yMax = []


        tree = ET.parse(old_data[i])
        root = tree.getroot()

        tree2 = ET.parse(new_data[i])
        root2 = tree2.getroot()

        for coords in root.iter('xmin'):
            xMin.append(coords.text)

        for coords2 in root.iter('xmax'):
            xMax.append(coords2.text)

        for coords3 in root.iter('ymin'):
            yMin.append(coords3.text)

        for coords4 in root.iter('ymax'):
            yMax.append(coords4.text)

        old_area = (int(xMax[0]) - int(xMin[0])) * (int(yMax[0]) - int(yMin[0]))
        new_area = 0

        if len(xMax) > 1:
            new_area = (int(xMax[1]) - int(xMin[1])) * (int(yMax[1]) - int(yMin[1]))

        f = open("sizeof_model_vs_annotation.csv", "a")
        f.write(str(i) + ',' + str(old_area) + ',' + str(new_area))
        f.write('\n')
        f.close()

        i += 1

if __name__ == "__main__":
    #size_comparison()
    a = np.asarray([[1, 2, 3], [40, 50, 60], [70, 80, 90]])
    np.savetxt("csv_files\\foo.csv", a.transpose(), delimiter=",")