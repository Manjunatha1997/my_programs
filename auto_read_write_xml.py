

from os import path
import os
import xml.etree.ElementTree as ET
from pascal_voc_writer import Writer
import glob
import cv2




# xmlfile = 'D:\\indoData\\dataset19\\completeGood\\1\\g110.xml' # cat1
xmlfile = 'D:\\indoData\\dataset19\\completeGood\\2\\g11.xml' # cat2
# xmlfile = 'D:\\indoData\\dataset19\\completeGood\\3\\g12.xml' # cat3
# xmlfile = 'D:\\indoData\\dataset19\\completeGood\\4\\g13.xml' # cat4
# xmlfile = 'D:\\indoData\\dataset19\\completeGood\\5\\g14.xml' # cat5 ** No xml data found,skip this file
# xmlfile = 'D:\\indoData\\dataset19\\completeGood\\6\\g15.xml' # cat6
# xmlfile = 'D:\\indoData\\dataset19\\completeGood\\7\\g16.xml' # cat7
# xmlfile = 'D:\\indoData\\dataset19\\completeGood\\8\\g17.xml' # cat8
# xmlfile = 'D:\\indoData\\dataset19\\completeGood\\9\\g18.xml' # cat9
# xmlfile = 'D:\\indoData\\dataset19\\completeGood\\10\\g19.xml' # cat10

# xmlfile = 'D:\\indoData\\dataset22\\dataset22\\dent\\dent_a_22\\dent15_a_22_1.xml'

mainImagepath = 'D:\\indoData\\dataset19\\completeGood\\2\\*.jpg'



main_xml_file = ET.parse(xmlfile)

root = main_xml_file.getroot()

label_cord = []

for i in main_xml_file.iter():
	if i.tag == 'width':
		width = i.text
		# label_cord.append({'width' :i.text})

	if i.tag == 'height':
		height = i.text
		# label_cord.append({'height':i.text})	

for object in root.findall('object'):
	name = object.find('name').text
	bndbox = object.find('bndbox')

	crd = [name]
	for cord in bndbox:
		crd.append(cord.text)

	label_cord.append(crd)
	





res = glob.glob(mainImagepath)

print(res)

for file in res:
	img = cv2.imread(file)
	width, height,depth = img.shape
	print(width,height)


	writer = Writer(file,height,width)
	for i in label_cord:
		print(i)
		writer.addObject(i[0],i[1],i[2],i[3],i[4])
	
	writer.save(file.replace('.jpg','.xml'))

