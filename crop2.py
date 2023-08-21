import cv2
import glob
import os
import os.path

files = glob.glob("/home/manju/python_programs/opencv/igbtt/first_camera_GVX/*.jpg")
out = "/home/manju/python_programs/opencv/igbtt/first_camera_GVX_crop/"
if not os.path.isdir(out):
    os.mkdir(out)
count = 0
for file in files:
    count += 1
    img = cv2.imread(file)
    crop_img = img[642:1463, 2818:3426]
    try:

        cv2.imwrite(out + "1M39AD_fourth_" + str(count) + ".jpg", crop_img)
        if count >= 25:
            break
        print(count, "cropped successfull....", file)
    except:
        continue
