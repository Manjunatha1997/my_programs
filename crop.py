
import os
import glob
import xml.etree.ElementTree as ET
import cv2
import bson
from matplotlib import image

path = r'D:\sansera_conrod_burr\burrCopy\\'

print(path)
# files = os.listdir(path)
files = glob.glob(path+'*.xml')
print(files)
out_path = r'D:\sansera_conrod_burr\burrCopy_out\\'

if not os.path.isdir(out_path):
	os.makedirs(out_path)

for file in files:
	# xmin,ymin,xmax,ymax = 216,134,403,291

	# image = cv2.imread(file)
	# crop_image = image[int(ymin):int(ymax),int(xmin):int(xmax)]
	# print(crop_image)
	# cv2.imwrite(f'{out_path}{str(bson.ObjectId())}.png',crop_image)
	
	tree = ET.parse(file)
	root = tree.getroot()
	for object in root.findall('object'):
		name = object.find('name').text
		xmin = object.find('bndbox/xmin').text
		ymin = object.find('bndbox/ymin').text
		xmax = object.find('bndbox/xmax').text
		ymax = object.find('bndbox/ymax').text

		img = file.replace('.xml','.jpg')
		# image = tyuioplokjmuyhgtvfrcdxzsedcxswz
		image = cv2.imread(img)
		print(xmin,ymin,xmax,ymax)


		crop_image = image[int(ymin):int(ymax),int(xmin):int(xmax)]
		print(crop_image)
		if not os.path.isdir(os.path.join(out_path,name)):
			os.makedirs(os.path.join(out_path,name))
		
		cv2.imwrite(f'{os.path.join(out_path,name)}/{str(bson.ObjectId())}.jpg',crop_image)
		
		