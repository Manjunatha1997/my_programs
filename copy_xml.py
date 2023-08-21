import os
import shutil
import xml.etree.ElementTree as ET
import cv2

inp_path = "/home/manju/Desktop/test/"

xml_file = "/home/manju/Desktop/test/MR_0.xml"

####################################################################

if not inp_path.endswith('/'):
	inp_path = inp_path+'/'


res  = os.listdir(inp_path)

for file in res:
	f = file.split('.')[0]+'.xml'	
	try:
		shutil.copyfile(xml_file,inp_path+f)
	except:
		pass



path = inp_path
files = os.listdir(path)

for file in files:

	if file.endswith('.xml'):
		
		tree = ET.parse(path+file)
		
		for elt in tree.iter():
			if elt.tag == 'folder':
				elt.text = (path.split('/')[-2])

			if elt.tag == 'filename':
				elt.text = file.split('.')[0]+'.jpg'

			if elt.tag == 'path':
				elt.text = (path+file.split('.')[0]+'.jpg')

			if elt.tag == 'width':
				img = (path+file.split('.')[0]+'.jpg')
				img = cv2.imread(img)
				h,w,c = img.shape
				elt.text = str(w)
			if elt.tag == 'height':
				img = (path+file.split('.')[0]+'.jpg')
				img = cv2.imread(img)
				h,w,c = img.shape
				elt.text = str(h)
			


		tree.write(path+file)