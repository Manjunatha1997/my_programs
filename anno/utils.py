import os
import shutil
import xml.etree.ElementTree as ET

from black import shutdown

def do_something():
	return "message"

def check_path_dir(path):
	if not os.path.isdir(path):
		return False
	else:
		return True


def find_extra_images(path,remove=False,move=None):
	res = os.listdir(os.path.join(path))
	jpg,xml = [],[]
	for i in res:

		if i.endswith('.jpg'):
			k = i.split('.')	
			jpg.append(k[0])
		
		else:
			if i.endswith('.xml'):
				k = i.split('.')
				xml.append(k[0])

	count = 0
	extra_images = []
	for i in jpg:
		if not i in xml:
			count += 1
			extra_images.append(os.path.join(i+'.jpg'))

	
	if remove == True:
		for fil in extra_images:
			os.remove(os.path.join(path,fil))
		return {"Images":extra_images,"Count":count,"Message":"Deleted"}
	if move:
		# if not os.path.isdir(move):
		# 	return {"message":"path not exists"}
		for f in extra_images:
			if not os.path.isdir(move):
				os.makedirs(move)

			shutil.move(os.path.join(path,f),os.path.join(move,f))
		return {"Images":extra_images,"Count":len(extra_images),"Message":'Moved'}
	
	if len(extra_images) == 0:
		return {"message":"No extra images found"}
	if len(extra_images) > 0:
		return {"Images":extra_images,"count":count}
	
	

def all_class_names(path):
	class_names = []
	files = os.listdir(os.path.join(path))
	for file in files:
		if file.endswith('.xml'):
			tree = ET.parse(os.path.join(path,file))
			root = tree.getroot()
			for elt in root.iter():
				if elt.tag == 'name':
					class_names.append(elt.text)
					# print(file)
				if elt.tag == 'name' and elt.text == 'chamfer_absence':
					print(file)
	
	temp = {}
	for i in class_names:
		temp[i] = class_names.count(i)
	return temp

