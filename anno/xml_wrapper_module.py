
from genericpath import isdir
from glob import glob
from importlib.resources import path
from math import floor
import os
import xml.etree.ElementTree as ET
import cv2
import shutil
import argparse
import sys
from transformer import Transformer




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
	class_names = []
	files = os.listdir(os.path.join(path))
	for file in files:
		if file.endswith('.xml'):
			tree = ET.parse(os.path.join(path,file))
			root = tree.getroot()
			for elt in root.iter():
				if elt.tag == 'name':
					class_names.append(elt.text)				
	temp = {}
	for i in class_names:
		temp[i] = class_names.count(i)
	return temp	


def find_extra_images(input_path,remove=False,move=None):
	"""

	"""
	## check path 
	if not os.path.exists(input_path):
		return "incorrect path"

	check_file_type = ['jpg','JPG','png','PNG','bmp','BMP']

	files = os.listdir(input_path)
	images, xmls = [], []

	for file in files:
		file_name = file.split('.')[0]
		file_type = file.split('.')[-1]

		if (file_type in check_file_type) and (file_type != 'xml'): 
			images.append(file_name+'.'+file_type)
		if file_type == 'xml':
			xmls.append(file_name)

	extra_images = []

	for img in images:
		imgg = img.split('.')[0]
		imgg = imgg.replace(input_path,'')
		if not imgg in xmls:
			extra_images.append(os.path.join(input_path, img))


	if remove == True:
		for ff in extra_images:
			os.remove(ff)
		# return extra_images,len(extra_images),"Deleted extra images"
		return {'extra_images':extra_images,'count':len(extra_images),'message':"Deleted extra images"}


	if move:
		for ff in extra_images:
			mf = move_file(ff,move)
		return {'extra_images':extra_images,'count':len(extra_images),'message':f"moved extra images to {move}"}

	return {"extra_images":extra_images,"count":len(extra_images),"message":f"found extra {len(extra_images)} images"}


def find_no_class_names(input_path,remove=False):
	if not os.path.isdir(input_path):
		return f"{input_path} path does not exists."
	
	files = os.listdir(input_path)
	empty_names = []
	for file in files:
		if file.endswith('.xml'):
			tree = ET.parse(os.path.join(input_path,file))
			root = tree.getroot()
			l = [elt.tag for elt in root.iter()]
			if 'name' not in l:
				empty_names.append(os.path.join(input_path,file))
	print(empty_names,'**********')
	if remove == True:
		for ef in empty_names:
			os.remove(ef)
		return f"{len(empty_names)} files deleted."
	return empty_names


def rename_class_name(folder_path, old_class, new_class):
	if not os.path.isdir(folder_path):
		return {"message":"Folder not exists"}

	files = glob(os.path.join(folder_path,'*.xml'))
	for file in files:
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
		classes = str(classes.keys())
		classes_path = create_txt_file(classes)
		xml2txt(path,path)
		remove_xml_files(path)



	return {"message":f" {folder_count} folders created", "destination_folders":list(set(out_folders))}

def send_mail(sender,receiver,message,attached_file):
	# Import smtplib for the actual sending function
	import smtplib

	# Import the email modules we'll need
	from email.mime.text import MIMEText

	# Open a plain text file for reading.  For this example, assume that
	# the text file contains only ASCII characters.
	with open(textfile, 'rb') as fp:
		# Create a text/plain message
		msg = MIMEText(fp.read())

	# me == the sender's email address
	# you == the recipient's email address
	msg['Subject'] = 'The contents of %s' % textfile
	msg['From'] = me
	msg['To'] = you

	# Send the message via our own SMTP server, but don't include the
	# envelope header.
	s = smtplib.SMTP('localhost')
	s.sendmail(me, [you], msg.as_string())
	s.quit()

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





if __name__ =="__main__":

	resp = split_images_from_folder(r'D:\sansera_conrod_burr\burr\test',5,["mail12","mail22","wdw","sf","wefdewfw"])
	print(resp)
	
	# resp = split_folder(r'D:\sansera_conrod_burr\burr\test',4)
	# print(resp)

	# resp= find_extra_images(r'D:\sansera_conrod_burr\burr\test',remove=True,move=None)
	# print(resp)

	# resp = find_no_class_names(r'D:\sansera_conrod_burr\burr\test',remove=True)
	# print(resp)

	# resp = rename_class_name(r'D:\sansera_conrod_burr\burr\test')
	# print(resp)





