import os
import xml.etree.ElementTree as ET

path = r'D:\indomim_tirupati\indoData\jun9_22\scania_jun7_22\scania_jun7_22\\'


input_
def all_class_names(path):
	files = os.listdir(path)
	for file in files:

		if file.endswith('.xml'):
			class_names = []

			tree = ET.parse(path+file)
			root = tree.getroot()
			for elt in root.iter():
				if elt.tag == 'name':
					class_names.append(elt.text)
					# print(file)
				if elt.tag == 'name' and elt.text == 'solder_bridge':
					print(file)
		

		

			temp = {}
			for i in class_names:
				temp[i] = class_names.count(i)

			# print(class_names)
			print(file,"=====>>",temp)

all_class_names(path)
