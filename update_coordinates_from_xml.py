
import xml.etree.ElementTree as ET
import glob

path = '/home/manju/Downloads/xml/*.xml'

res = glob.glob(path)

for file in res:

	tree = ET.parse(file)

	root = tree.getroot()
	for object in root.findall('object'):
		name = object.find('bndbox')

		for i in name:

			flo = float(i.text)
			flo = round(flo)
			flo = str(flo)

			i.text = flo


			print(i.text,flo)

	tree.write(file)

