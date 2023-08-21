
import numpy as np
import imgaug as ia
import imgaug.augmenters as iaa
import cv2
import xml.etree.ElementTree as ET
import glob
import imageio


input_path = 'C:\\Users\\Manju\\Pictures\\Camera Roll\\maini_mea\\'


res = glob.glob(input_path+'*.jpg')


## Augmentations

affine = iaa.Affine(scale=(0.5, 1.5))
contrast = iaa.LogContrast(gain=(0.6, 1.4), per_channel=True)
hue = iaa.MultiplyHue((0.5, 1.5))
gray_scale = iaa.Grayscale(alpha=(0.0, 1.0))
brightness = iaa.AddToBrightness((-30, 30))

augment_list = {'contrast':contrast,'affine':affine,"hue":hue,"gray_scale":gray_scale,"brightness":brightness}


for img in res:

	for augment in augment_list:

		
		# reading the image
		image = imageio.imread(img)

		# augmenting the image
		images_aug = augment_list[augment](image=image)

		# writing the augmented image 
		cv2.imwrite(img.replace('.jpg',augment+'.jpg'),images_aug)
		print(augment,'augmented..... for ',img)
		
	print('****************************************')




