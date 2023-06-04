
from glob import glob
from math import floor
import os
import xml.etree.ElementTree as ET
import cv2
import shutil
import argparse
import sys
from transformer import Transformer



def check_path_dir(path):
	if not os.path.isdir(path):
		return False
	else:
		return True


def move_file(in_file,out_dir):
	if not os.path.exists(in_file):
		return "input file does not exists"

	base_file = os.path.basename(in_file)
	out_file = os.path.join(out_dir,base_file)

	if not os.path.isdir(out_dir):
		os.makedirs(out_dir)
		shutil.move(in_file,out_file)
	else:
		shutil.move(in_file,out_file)
	return True

def find_all_classes(path):
	if not os.path.isdir(path):
		return {}

	class_names = []
	for (root_path, folders, files) in os.walk(path):

		for file in files:
			file = os.path.join(root_path,file)
			if file.endswith('.xml'):
				tree = ET.parse(os.path.join(path,file))
				root = tree.getroot()
				for elt in root.iter():
					if elt.tag == 'name':
						class_names.append(elt.text)				

	temp = {}
	for i in set(class_names):
		temp[i] = class_names.count(i)
	return temp	

def find_all_classes_recursive(path):
	if not os.path.isdir(path):
		return []
	response = []
	for root_path, directories, files in os.walk(path):
		if directories == []:
			directories = [path]
		

		for directory in directories:
			xml_count = 0
			sub_dir = os.path.join(root_path,directory)
			class_names = []
			files = os.listdir(os.path.join(sub_dir))
			for file in files:
				if file.endswith('.xml'):
					xml_count += 1
					tree = ET.parse(os.path.join(sub_dir,file))
					root = tree.getroot()
					for elt in root.iter():
						if elt.tag == 'name':
							class_names.append(elt.text)				
						
			temp = {}
			temp['folder_path'] = sub_dir
			temp['total bounding box'] = len(class_names)
			temp["total annotated images"] = xml_count
			for i in set(class_names):
				temp[i] = class_names.count(i)
			
			if len(class_names) != 0:
				response.append(temp)

	return response	


def find_extra_images(input_path,remove=False,move=None):
	"""

	"""
	## check path 
	if not os.path.exists(input_path):
		return "incorrect path"

	check_file_type = ['jpg','JPG','png','PNG','bmp','BMP']
	extra_images = []
	images, xmls = [], []



	for i in os.walk(input_path):
		root_path = i[0]
		folders = i[1]
		files = i[2]
		for file in files:
			file = os.path.join(root_path,file)
			if file.endswith('.xml'):
				xmls.append(file.split('.')[0])
			else:
				images.append(file)

	for image in images:
		img = image.split('.')[0]
		if not img in xmls:
			extra_images.append(image)

	if remove:
		for ff in extra_images:
			os.remove(ff)
		# return extra_images,len(extra_images),"Deleted extra images"
		return {'extra_images':extra_images,'count':len(extra_images),'message':"Deleted extra images"}


	if move:
		for ff in extra_images:
			mf = move_file(ff,move)
		return {'extra_images':extra_images,'count':len(extra_images),'message':f"moved extra images to {move}"}

	return {"extra_images":extra_images,"count":len(extra_images),"message":f"found extra {len(extra_images)} images"}


def find_no_class_names(path,remove=False):
	if not os.path.isdir(path):
		return f"{path} path does not exists."


	## initilizing empty varibles here	
	empty_names = []
	

	for i in os.walk(path):
		root_path = i[0]
		folders = i[1]
		files = i[2]
		


		for file in files:
			file = os.path.join(root_path,file)

			if file.endswith('.xml'):
				tree = ET.parse(file)
				root = tree.getroot()
				l = [elt.tag for elt in root.iter()]
				if 'name' not in l:
					empty_names.append(file)
	if remove == True:
		for ef in empty_names:

			os.remove(ef)
			try:
				os.remove(ef.replace('.xml',".jpg"))
			except:
				pass
			try:
				os.remove(ef.replace('.xml',".JPG"))
			except:
				pass
			try:
				os.remove(ef.replace('.xml',".png"))
			except:
				pass
			try:
				os.remove(ef.replace('.xml',".PNG"))
			except:
				pass
			try:
				os.remove(ef.replace('.xml',".jpeg"))
			except:
				pass
			try:
				os.remove(ef.replace('.xml',".JPEG"))
			except:
				pass

		return f"{len(empty_names)*2} files deleted."
	return empty_names


def rename_class_name(folder_path, old_class, new_class):
	if not os.path.isdir(folder_path):
		return {"message":"Folder not exists"}
	
	all_classes = find_all_classes(folder_path)
	if not old_class in list(all_classes.keys()):
		return {"message":f"{old_class} not exists"}


	for (root_path,folders,files) in os.walk(folder_path):

		for file in files:
			if file.endswith('.xml'):
				file = os.path.join(root_path,file)
				tree = ET.parse(file)
				for elt in tree.iter():
					if elt.tag == 'name' and elt.text == old_class:
						elt.text = new_class
				tree.write(file)

	return {"message":f"changed from {old_class} to {new_class}"}


def remove_xml_files(path):
	if not os.path.isdir(path):
		return {"message":f"{path} path does not exists"}
	files = glob(os.path.join(path,'*.xml'))
	for file in files:
		os.remove(file)

def create_txt_file(classes):
	fw = open('classes.txt','w')
	for clss in classes:
		fw.write(clss+'\n')
	fw.close()
	return os.path.join(os.getcwd(),'classes.txt')



def xml2txt(xml_dir,out_dir):
	parser = argparse.ArgumentParser(description="Formatter from ImageNet xml to Darknet text format")
	parser.add_argument("-xml", help="Relative location of xml files directory" ,default='xml')
	parser.add_argument("-out", help="Relative location of output txt files directory", default="out")
	parser.add_argument("-c", help="Relative path to classes file", default="classes.txt")
	args = parser.parse_args()

	xml_dir = os.path.join(os.path.dirname(os.path.realpath('__file__')), xml_dir)
	if not os.path.exists(xml_dir):
		print("Provide the correct folder for xml files.")
		sys.exit()

	out_dir = os.path.join(os.path.dirname(os.path.realpath('__file__')), out_dir)
	if not os.path.exists(out_dir):
		os.makedirs(out_dir)

	if not os.access(out_dir, os.W_OK):
		print("%s folder is not writeable." % out_dir)
		sys.exit()
	
	
	transformer = Transformer(xml_dir=xml_dir, out_dir=out_dir)
	transformer.transform()



def split_folder(folder_path,size,image_type='jpg'):
	if not os.path.isdir(folder_path):
		return {"message":f"{folder_path} path does not exists"}
	temp_size_bytes = size * 1000000
	print(temp_size_bytes)
	temp_size = 0
	folder_count = 1

	out_folders = []
	for file in glob(os.path.join(folder_path,'*.xml')):
		xml = file
		
		image = file.replace('.xml',f".{image_type}")
		xml_size = os.path.getsize(xml)
		image_size = os.path.getsize(image)
		t_size = xml_size + image_size
		temp_size += t_size
		if temp_size >= temp_size_bytes:
			folder_count += 1
			temp_size = 0

		f_path = os.path.join(folder_path,str(folder_count))
		out_folders.append(f_path)
		if not os.path.isdir(f_path):
			os.makedirs(f_path)

		shutil.copyfile(xml,os.path.join(f_path,os.path.basename(xml)))
		shutil.copyfile(image,os.path.join(f_path,os.path.basename(image)))
	
	for path in list(set(out_folders)):
		classes = find_all_classes(path)
		classes = list(classes.keys())
		classes_path = create_txt_file(classes)
		xml2txt(path,path)
		remove_xml_files(path)
		shutil.copyfile('classes.txt',os.path.join(path,'classes.txt'))



	return {"message":f" {folder_count} folders created", "destination_folders":list(set(out_folders))}


def split_images_from_folder(folder_path,no_of_folders,emails):
	image_types = ['jpg','JPG','png','PNG','bmp','BMP']

	if not os.path.isdir(folder_path):
		return {"message":"folder does not exists."}
	
	if no_of_folders != len(emails):
		return {"message":"emails and folders should be equal"}
	

	files = os.listdir(folder_path)

	xml_file_length = glob(os.path.join(folder_path,'*.xml'))
	xml_file_length = len(xml_file_length)

	t_files =  (len(files) - xml_file_length)
	files_split_each = floor(t_files / no_of_folders)
	print(files_split_each)

	counter = 0

	mail_index = 0

	for m in emails:
		if not os.path.isdir(os.path.join(folder_path,m)):
			os.makedirs(os.path.join(folder_path,m))
	
	for file in files:
		file_type = file.split('.')[-1]
		if file_type in image_types:
			
			if counter == files_split_each:
				counter = 0
				mail_index += 1
			try:
				email = emails[mail_index]
			except:
				email = emails[-1]
			
			shutil.copyfile(os.path.join(folder_path,file),os.path.join(folder_path,email,file))
			counter += 1

	return {"message":f" Data copied to {emails} in given path. "}

def delete_class_names(path,classes_list):
	
	for (root_path,folders,files) in os.walk(path):
		for file in files:
			if file.endswith('.xml'):
				file = os.path.join(root_path,file)	
				tree = ET.parse(file)
				root = tree.getroot()
				for object in root.findall('object'):
					name = object.find('name').text
					print(name, classes_list)

					if name in classes_list: 
						root.remove(object)
					
				tree.write(file)
	resp = {"message":f"deleted {classes_list}"}
	return resp



if __name__ =="__main__":

	# resp = split_images_from_folder(r'D:\sansera_conrod_burr\burr\test',5,["mail12","mail22","wdw","sf","wefdewfw"])
	# print(resp)
	
	# resp = split_folder(r'D:\sansera_conrod_burr\burr\test',4)
	# print(resp)

	resp= find_extra_images(r'D:\sansera_conrod_burr\burr\test',remove=False,move=None)
	print(resp)

	# resp = find_no_class_names(r'D:\sansera_conrod_burr\burr\test',remove=True)
	# print(resp)

	# resp = rename_class_name(r'D:\sansera_conrod_burr\burr\test')
	# print(resp)





