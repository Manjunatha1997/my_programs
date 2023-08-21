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






class Augment:
	def __init__(self,image_path,augment_type):
		self.image_path = image_path
		self.augment_type = augment_type
	
	def read_image(self):
		image = cv2.imread(self.image_path)
		return image
	

	def getting_labels_and_coordinatyes(self):
				
		xml_file = self.image_path.replace('.jpg','.xml')
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


	def augment_image_bndbox(self):
		
		bbs_list = []
		labels_and_coords = Augment(image_path,aug_dict).getting_labels_and_coordinatyes()
		image = Augment(image_path,aug_dict).read_image()
		for i in labels_and_coords:
			bbs_list.append(BoundingBox(i['xmin'],i['ymin'],i['xmax'],i['ymax'],i['name']))

		bbs = BoundingBoxesOnImage(bbs_list,shape=image.shape)

		# seq = iaa.Sequential([
		# 	iaa.Multiply((1.2, 1.5)), # change brightness, doesn't affect BBs
		# 	# translate by 40/60px on x/y axis, and scale to 50-70%, affects BBs
		# ])
		# Augment BBs and images.
		augments = []

		for aug_type,aug in self.augment_type.items():
			image_aug, bbs_aug = aug(image=image, bounding_boxes=bbs)
			augments.append((image_aug,bbs_aug,bbs,aug_type))

		# return image_aug, bbs_aug, bbs
		return augments



	def write_augment_image(self):
		augmented_images = []

		for image_aug,bbs_aug,bbs,aug_type in Augment(image_path,aug_dict).augment_image_bndbox():
			a = []


			cv2.imwrite(self.image_path.replace('.jpg','_'+aug_type+'.jpg'),image_aug)
			a.append(self.image_path.replace('.jpg','_'+aug_type+'.jpg'))
			a.append(bbs_aug)
			a.append(bbs)
			augmented_images.append(a)



		return augmented_images
		
		# return self.image_path.replace('.jpg',+'_'+self.augment_type+'.jpg')


	def write_augment_xml(self):
		
		# bbs = Augment().augment_image_bndbox()[3]
		# bbs_aug = Augment().augment_image_bndbox()[2]

		augmented_images = Augment(image_path,aug_dict).write_augment_image()

		for i in augmented_images:
			augment_image = i[0]
			bbs_aug = i[1]
			bbs = i[2]
			shape = Augment(image_path,aug_dict).read_image().shape
			


			writer = Writer(augment_image, shape[1], shape[0])




			for i in range(len(bbs.bounding_boxes)):
				before = bbs.bounding_boxes[i]
				after = bbs_aug.bounding_boxes[i]
				writer.addObject(after.label, int(after.x1), int(after.y1), int(after.x2), int(after.y2))
			writer.save(augment_image.replace('.jpg','.xml'))




seq = iaa.Sequential([
	iaa.Multiply((1.2, 1.5)), # change brightness, doesn't affect BBs
	# translate by 40/60px on x/y axis, and scale to 50-70%, affects BBs
])

seq1 = iaa.Sequential([
	iaa.Multiply((0.5, 1)), # change brightness, doesn't affect BBs
	# translate by 40/60px on x/y axis, and scale to 50-70%, affects BBs
])
aug_dict = {'seq':seq,'seq1':seq1}



source_path = 'C:\\Users\\Manju\\Desktop\\test\\*.jpg'

res = glob.glob(source_path)


for image_path in res:
	print(image_path)

	a1 = Augment(image_path,aug_dict)
	a1.read_image()
	a1.getting_labels_and_coordinatyes()
	a1.augment_image_bndbox()
	a1.write_augment_image()
	a1.write_augment_xml()




