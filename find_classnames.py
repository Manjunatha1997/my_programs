import shutil
import glob
import os
import xml.etree.ElementTree as ET

count = 1
def find_classnames(path,num_of_classes):
	files = glob.glob(path+'*.xml')
	for file in files:
		tree = ET.parse(file)
		c = []


		for elt in tree.iter():

			if((elt.tag == 'name')):
				# c.append(elt.text)
				pass



		if len(c) != num_of_classes:
			print(file,c,count)



path = '/home/manju/Desktop/bewww/train/'
num_of_classes = 1

find_classnames(path,num_of_classes)


