import os
import glob
import xml.etree.ElementTree as ET
import cv2

path = r'C:\Users\Manju\Downloads\burr\burr_cross_hole\\'


# files = os.listdir(path)
files = glob.glob(path+'*.xml')


for file in files:

	tree = ET.parse(file)
	root = tree.getroot()
	for elt in tree.iter():
		# if elt.tag == 'name' and elt.text == 'Top_Right':
		if elt.tag == 'name' and elt.text == 'burr':
			elt.text = 'burr_cross_hole'
			print(elt.text)
			# cv2.imwrite('D:\\indoData\\datasetjan11\\dents_extra\\35_19_hole_presence\\')


	tree.write(file)
	print(file)
		
