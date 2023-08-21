import os
import re
import cv2

path = '/home/manju/Desktop/bewww/train/'
out_path = '/home/manju/Desktop/lincode/crop_out_192/'

xml_files, jpg_files = [],[]

for file in os.listdir(path):
    if file.endswith('.xml'):
        xml_files.append(file)
    if file.endswith('.jpg'):
        jpg_files.append(file)

for xml_file in xml_files:
    fr = open(path+xml_file)
    data = fr.read()

    xmin = re.search('(<xmin>)(\d+)(</xmin>)',data).group(2)
    ymin = re.search('(<ymin>)(\d+)(</ymin>)',data).group(2)
    xmax = re.search('(<xmax>)(\d+)(</xmax>)',data).group(2)
    ymax = re.search('(<ymax>)(\d+)(</ymax>)',data).group(2)

    xmin,ymin,xmax,ymax = int(xmin),int(ymin),int(xmax),int(ymax)
    print(xml_file,xmin,ymin,xmax,ymax)
    # print(xml_file.split('.')[0]+'.jpg')
    # rename_jpg = xml_file.split('.')[0]+'.jpg'
    # if rename_jpg in jpg_files:
    #     img = cv2.imread(path+rename_jpg)
    #     crop_img = img[ymin:ymax, xmin:xmax]
    #     cv2.imwrite(out_path+rename_jpg,crop_img)
