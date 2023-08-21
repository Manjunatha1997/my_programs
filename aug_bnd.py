from cProfile import label

from numpy import size
import imgaug as ia
import imgaug.augmenters as iaa
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage
import xml.etree.ElementTree as ET

import cv2

# ia.seed(1)

# image = ia.quokka(size=(480, 640))
image = cv2.imread('C:\\Users\\Manju\\Desktop\\test\\dent_2a_22_4.jpg')

print(type(image))

# read custom image using imgaug
# image = ia.quokka(size=(480, 640))



cv2.imshow('image',image)




xml_file = 'C:\\Users\\Manju\\Desktop\\test\\dent_2a_22_4.xml'
tree = ET.parse(xml_file)

labels_and_coords = []

root = tree.getroot()
for object in root.findall('object'):
	name = object.find('name').text
	xmin = int(object.find('bndbox/xmin').text)
	ymin = int(object.find('bndbox/ymin').text)
	xmax = int(object.find('bndbox/xmax').text)
	ymax = int(object.find('bndbox/xmax').text)
	labels_and_coords.append({'name': name, 'xmin': xmin, 'ymin': ymin, 'xmax': xmax, 'ymax': ymax})

# print(labels_and_coords)


# bbs = BoundingBoxesOnImage([
# 	BoundingBox(x1=65, y1=100, x2=200, y2=150,label='label1'),
# 	BoundingBox(x1=150, y1=80, x2=200, y2=130,label='label2'),
# ], shape=image.shape)

bbsc = BoundingBoxesOnImage([
	BoundingBox(labels_and_coords[0]['xmin'], labels_and_coords[0]['ymin'], labels_and_coords[0]['xmax'], labels_and_coords[0]['ymax'],label=labels_and_coords[0]['name']),
	BoundingBox(labels_and_coords[1]['xmin'], labels_and_coords[1]['ymin'], labels_and_coords[1]['xmax'], labels_and_coords[1]['ymax'],label=labels_and_coords[1]['name']),
	BoundingBox(labels_and_coords[2]['xmin'], labels_and_coords[2]['ymin'], labels_and_coords[2]['xmax'], labels_and_coords[2]['ymax'],label=labels_and_coords[2]['name']),
	BoundingBox(labels_and_coords[3]['xmin'], labels_and_coords[3]['ymin'], labels_and_coords[3]['xmax'], labels_and_coords[3]['ymax'],label=labels_and_coords[3]['name']),
	BoundingBox(labels_and_coords[4]['xmin'], labels_and_coords[4]['ymin'], labels_and_coords[4]['xmax'], labels_and_coords[4]['ymax'],label=labels_and_coords[4]['name']),
	BoundingBox(labels_and_coords[5]['xmin'], labels_and_coords[5]['ymin'], labels_and_coords[5]['xmax'], labels_and_coords[5]['ymax'],label=labels_and_coords[5]['name']),
	BoundingBox(labels_and_coords[6]['xmin'], labels_and_coords[6]['ymin'], labels_and_coords[6]['xmax'], labels_and_coords[6]['ymax'],label=labels_and_coords[6]['name']),
	BoundingBox(labels_and_coords[7]['xmin'], labels_and_coords[7]['ymin'], labels_and_coords[7]['xmax'], labels_and_coords[7]['ymax'],label=labels_and_coords[7]['name']),
	BoundingBox(labels_and_coords[8]['xmin'], labels_and_coords[8]['ymin'], labels_and_coords[8]['xmax'], labels_and_coords[8]['ymax'],label=labels_and_coords[8]['name']),
	BoundingBox(labels_and_coords[9]['xmin'], labels_and_coords[9]['ymin'], labels_and_coords[9]['xmax'], labels_and_coords[9]['ymax'],label=labels_and_coords[9]['name']),
	BoundingBox(labels_and_coords[10]['xmin'], labels_and_coords[10]['ymin'], labels_and_coords[10]['xmax'], labels_and_coords[10]['ymax'],label=labels_and_coords[10]['name']),
	BoundingBox(labels_and_coords[11]['xmin'], labels_and_coords[11]['ymin'], labels_and_coords[11]['xmax'], labels_and_coords[11]['ymax'],label=labels_and_coords[11]['name']),
	BoundingBox(labels_and_coords[12]['xmin'], labels_and_coords[12]['ymin'], labels_and_coords[12]['xmax'], labels_and_coords[12]['ymax'],label=labels_and_coords[12]['name']),
	BoundingBox(labels_and_coords[13]['xmin'], labels_and_coords[13]['ymin'], labels_and_coords[13]['xmax'], labels_and_coords[13]['ymax'],label=labels_and_coords[13]['name']),
	BoundingBox(labels_and_coords[14]['xmin'], labels_and_coords[14]['ymin'], labels_and_coords[14]['xmax'], labels_and_coords[14]['ymax'],label=labels_and_coords[14]['name']),
	BoundingBox(labels_and_coords[15]['xmin'], labels_and_coords[15]['ymin'], labels_and_coords[15]['xmax'], labels_and_coords[15]['ymax'],label=labels_and_coords[15]['name']),
	BoundingBox(labels_and_coords[16]['xmin'], labels_and_coords[16]['ymin'], labels_and_coords[16]['xmax'], labels_and_coords[16]['ymax'],label=labels_and_coords[16]['name']),
	BoundingBox(labels_and_coords[17]['xmin'], labels_and_coords[17]['ymin'], labels_and_coords[17]['xmax'], labels_and_coords[17]['ymax'],label=labels_and_coords[17]['name']),

	], shape=image.shape)


# print(bbsc)

# exit()
seq = iaa.Sequential([
	iaa.Multiply((1.2, 1.5)), # change brightness, doesn't affect BBs
	iaa.Affine(
		translate_px={"x": 40, "y": 60},
		scale=(0.5, 0.7)
	) # translate by 40/60px on x/y axis, and scale to 50-70%, affects BBs
])

# Augment BBs and images.
bbs = bbsc

image_aug, bbs_aug = seq(image=image, bounding_boxes=bbs)

# print coordinates before/after augmentation (see below)
# use .x1_int, .y_int, ... to get integer coordinates
for i in range(len(bbs.bounding_boxes)):
	before = bbs.bounding_boxes[i]
	after = bbs_aug.bounding_boxes[i]
	print("BB %d: (%.4f, %.4f, %.4f, %.4f, %s) -> (%.4f, %.4f, %.4f, %.4f, %s)" % (
		i,
		before.x1, before.y1, before.x2, before.y2, before.label,
		after.x1, after.y1, after.x2, after.y2, after.label)
	)

# image with BBs before/after augmentation (shown below)
image_before = bbs.draw_on_image(image, size=2)
image_after = bbs_aug.draw_on_image(image_aug, size=2, color=[0, 0, 255])


cv2.imshow('image_before', image_before)
cv2.imshow('image_after', image_after)

cv2.waitKey(0)
