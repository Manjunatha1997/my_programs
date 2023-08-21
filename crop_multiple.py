import os
import glob
import xml.etree.ElementTree as ET
import cv2

path = 'C:\\Users\\lovel\\Downloads\\matrix_annotations\\'

out_path = 'C:\\Users\\lovel\\Downloads\\matrix_annotations_out\\'


if not os.path.isdir(out_path):
	os.mkdir(out_path)

os.chdir(out_path)
# files = os.listdir(path)
files = glob.glob(path+'*.xml')


c = 0
for file in files:
	img = file.split('.')[0] + '.jpg'
	img = cv2.imread(img)
	
	tree = ET.parse(file)
	root = tree.getroot()
	
	for object in root.findall('object'):
		name = object.find('name')
		bndbox = object.find('bndbox')

		lst = []

		for bnd in bndbox:
			lst.append(int(bnd.text))
			if not os.path.isdir(name.text):
				os.mkdir(name.text)

			print(name.text,bnd)

		print('***************',lst,name.text)
		crop_img = img[lst[1]:lst[3],lst[0]:lst[2]]
		# print(crop_img)
		cv2.imwrite(name.text+'/'+name.text+str(c)+'.jpg',crop_img)
		c += 1




