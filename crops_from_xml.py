from genericpath import isdir
import shutil
import glob
import os
import xml.etree.ElementTree as ET
import cv2
import bson





path = r'D:\indomim_tirupati\indoData\segregated\chamfer_thread\\'

out = r'D:\indomim_tirupati\indoData\segregated\chamfer_thread_out\\'


def create_directory(path):
	if not os.path.isdir(path):
		print('creating directory ....', path)
		os.makedirs(path)

create_directory(out)


res = glob.glob(path+'*.xml')

for xml_file in res:
	print(xml_file)     

	image = xml_file.replace('.xml','.jpg')
	fname = image.split('\\')[-1].split('.')[0]

	img = cv2.imread(image)

	tree = ET.parse(xml_file)

	root = tree.getroot()
	for object in root.findall('object'):
		name = object.find('name').text
		bndbox = object.find('bndbox')
		coordinates = []
		for cords in bndbox:
			coordinates.append(cords.text)
	  
		f = out+name

		create_directory(f)
	   

		img_crop = img[int(coordinates[1]):int(coordinates[3]), int(coordinates[0]):int(coordinates[2])]
	  
		cv2.imwrite(f'{f}/{fname}_{str(bson.ObjectId())}.jpg',img_crop)

