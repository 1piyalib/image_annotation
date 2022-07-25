import xml.etree.ElementTree as ET
"""
Reads image annotation information stored in Pascal VOC format
"""
class xml_parser:
    def __init__(self, filename, element_text):
        self.element_text = element_text
        self.file_name = filename
        self.voc_name_tag = "name"
        self.voc_coordinate_tag = "bndbox"

    def read_number_of_tags(self):
        tree = ET.parse(self.file_name)
        root = tree.getroot()
        num_of_tags = 0
        for child in root.iter(self.voc_name_tag):
            if child.text == self.element_text:
                 num_of_tags = num_of_tags + 1
        return(num_of_tags)

    def read_coordinates(self):
        tree = ET.parse(self.file_name)
        root = tree.getroot()
        coordinates_list = []  #list of list of coordinates
        for child in root.iter(self.self.voc_coordinate_tag):
            print(child.text)


        return(coordinates_list)