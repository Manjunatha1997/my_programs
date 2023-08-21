import glob
import imageio
import imgaug as ia
import imgaug.augmenters as iaa
import numpy as np
import os,shutil
import xml.etree.ElementTree as ET
import xml
import cv2
import xmltodict
import json
import xml.etree.cElementTree as e
import numpy as np
import uuid 
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage
import sys
import time
import threading
from multiprocessing import Process
from pascal_voc_writer import Writer
import glob

path = 'C:\\Users\\lovel\\OneDrive\\Desktop\\testaug\\'

affine = iaa.Affine(scale=(0.5, 1.5))
contrast = iaa.LogContrast(gain=(0.6, 1.4), per_channel=True)

augment_list = {'contrast':contrast,'affine':affine}




def write_xml(image,class_name_and_coordinates):
	img = cv2.imread(image)
	w,h,c = img.shape
	writer = Writer(image, w, h)

	for cord in class_name_and_coordinates:
		writer.addObject(cord[0],cord[1],cord[2],cord[3],cord[4])
	writer.save(image.replace('.jpg','.xml'))

def get_cord(xml):
	tree = ET.parse(xml)
	root = tree.getroot()
	coordinates = []
	for object in root.findall('object'):
		bndbox = object.find('bndbox')
		crd = []
		for cord in bndbox:
			crd.append(int(cord.text))
		coordinates.append(crd)
	
	return coordinates
	
	
x = get_cord(path+'WIN_20210831_12_00_50_Pro.xml')
print(x)


bbsoi = ia.BoundingBoxesOnImage([
    ia.BoundingBox(x1=10.5, y1=20.5, x2=50.5, y2=30.5)
], shape=image.shape)
image_with_bbs = bbsoi.draw_on_image(image)
image_with_bbs = ia.BoundingBox(
    x1=50.5, y1=10.5, x2=100.5, y2=16.5
).draw_on_image(image_with_bbs, color=(255, 0, 0), size=3)
ia.imshow(image_with_bbs)

def objects_coord_aug(jason,augment,image):#json format and which augumantation and image
    object_list = []
    # print(type(jason['annotation']['object']))
    # print(len(jason['annotation']['object']))
    # for i,x in enumerate(jason['annotation']['object']):
    object_dict = {'name': '',
    'pose': 'Unspecified',
    'truncated': '0',
    'difficult': '0',
    'bndbox': {}}
    x = jason['annotation']['object']
    x1,y1,x2,y2 = x['bndbox']['xmin'],x['bndbox']['ymin'],x['bndbox']['xmax'],x['bndbox']['ymax']
    bbs = BoundingBoxesOnImage([BoundingBox(x1=int(x1), x2=int(x2), y1=int(y1), y2=int(y2))], shape=image.shape)
    image_aug, bbs_aug = augment(image=image, bounding_boxes=(bbs))
    coordinates = bbs_aug.to_xyxy_array()
    xmin,ymin,xmax,ymax = (coordinates[0][0]),(coordinates[0][1]),(coordinates[0][2]),(coordinates[0][3])  
    # print(xmin,ymin,xmax,ymax)
    object_dict['name']=x['name']
    object_dict['bndbox']= {'xmin':int(xmin),'ymin':int(ymin),'xmax':int(xmax),'ymax':int(ymax)} 
    object_list=(object_dict)
    # print(object_list)
    return object_list,image_aug,image_aug.shape


def aug_img_bndbox(path ,augment_list):
	for xml in glob.glob(path+'*.xml'):
		for augment in augment_list:
			img = xml.replace('.xml','.jpg')

			# reading the image
			image = imageio.imread(img)

			# augmenting the image
			images_aug = augment_list[augment](image=image)

			# writing the augmented image 
			cv2.imwrite(img.replace('.jpg',augment+'.jpg'),images_aug)


# aug_img_bndbox(path ,augment_list)


