import cv2
import glob
import os
import os.path

files = glob.glob("/home/manju/python_programs/opencv/igbtt/fifth_camera_GVM/*.jpg")
out = "/home/manju/python_programs/opencv/igbtt/fifth_camera_GVM_crop/"
if not os.path.isdir(out):
	os.mkdir(out)
count = 0
for file in files:
	count += 1
	img = cv2.imread(file)
	crop_img = img[1379:841, 708:299]
	try:
		cv2.imwrite(out+"30APF10_"+str(count)+".jpg", crop_img)
		if count >= 50:
			break
		print(count,"cropped successfull....",file)
	except:
		continue