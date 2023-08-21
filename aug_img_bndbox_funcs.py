import imgaug as ia
import imgaug.augmenters as iaa
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage
import cv2
import xml.etree.ElementTree as ET
import imageio
from matplotlib import image
from numpy import append
from pascal_voc_writer import *
import glob
from sys import platform






## Augmentations

brightness_high = iaa.Sequential([iaa.Multiply((1.2, 1.5)),])

brightness_low = iaa.Sequential([iaa.Multiply((0.5, 1)),])

drop = iaa.Dropout2d(p=0.5)

median_blur = iaa.MedianBlur(k=(3, 11))

contrast = iaa.GammaContrast((0.5, 2.0))

rotate_180 = iaa.Affine(rotate=(180))

rotate_90 = iaa.Affine(translate_percent={"x": (0.1,-0.1),"y": (0.1,-0.1)},rotate=(-360,360), scale=0.5)





def crate_dest_path_dir(dest_path):
	if not os.path.isdir(dest_path):
		os.makedirs(dest_path)

def read_image(image_path):
	image = cv2.imread(image_path)
	return image


def getting_labels_and_coordinatyes():
			
	xml_file = image_path.replace('.jpg','.xml')
	tree = ET.parse(xml_file)
	root = tree.getroot()

	labels_and_coords = []
	for object in root.findall('object'):
		name = object.find('name').text
		xmin = int(object.find('bndbox/xmin').text)
		ymin = int(object.find('bndbox/ymin').text)
		xmax = int(object.find('bndbox/xmax').text)
		ymax = int(object.find('bndbox/ymax').text)
		labels_and_coords.append({'name': name, 'xmin': xmin, 'ymin': ymin, 'xmax': xmax, 'ymax': ymax})
	return labels_and_coords


def augment_image_bndbox():
		
	bbs_list = []
	labels_and_coords = getting_labels_and_coordinatyes()
	image = read_image(image_path)
	for i in labels_and_coords:
		bbs_list.append(BoundingBox(i['xmin'],i['ymin'],i['xmax'],i['ymax'],i['name']))

	bbs = BoundingBoxesOnImage(bbs_list,shape=image.shape)
	augments = []

	for aug_type,aug in augment_type.items():
		image_aug, bbs_aug = aug(image=image, bounding_boxes=bbs)
		augments.append((image_aug,bbs_aug,bbs,aug_type))
	return augments


def write_augment_image():
	augmented_images = []

	for image_aug,bbs_aug,bbs,aug_type in augment_image_bndbox():
		a = []
		if platform == "linux" or platform == "linux2":
			aug_image_path = image_path.split('/')[-1]
		
		elif platform == "win32":
			aug_image_path = image_path.split('\\')[-1]
		
		cv2.imwrite(dest_path+aug_image_path.replace('.jpg','_'+aug_type+'.jpg'),image_aug)
		a.append(dest_path+aug_image_path.replace('.jpg','_'+aug_type+'.jpg'))
		a.append(bbs_aug)
		a.append(bbs)
		augmented_images.append(a)

	return augmented_images
		
def write_augment_xml():
	augmented_images = write_augment_image()

	for i in augmented_images:
		augment_image = i[0]
		bbs_aug = i[1]
		bbs = i[2]
		shape = read_image(image_path).shape
		writer = Writer(augment_image, shape[1], shape[0])
		for i in range(len(bbs.bounding_boxes)):
			before = bbs.bounding_boxes[i]
			after = bbs_aug.bounding_boxes[i]
			writer.addObject(after.label, int(after.x1), int(after.y1), int(after.x2), int(after.y2))
		writer.save(augment_image.replace('.jpg','.xml'))


if __name__ == '__main__':
	aug_dict = {'brightness_high':brightness_high,'brightness_low':brightness_low,'drop':drop,'median_blur':median_blur,'contrast':contrast,'rotate_90':rotate_90,'rotate_180':rotate_180}

	augment_type = aug_dict
	source_path = 'C:/Users/Manju/Desktop/test'

	dest_path = source_path+'_aug/'
	print(source_path, dest_path)
	crate_dest_path_dir(dest_path)



	res = glob.glob(source_path+'/*.jpg')


	for image_path in res:
		write_augment_xml()




