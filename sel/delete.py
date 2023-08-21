

import os
import xml.etree.ElementTree as et
import shutil

path = '/home/manju/Desktop/MR244/'

res = os.listdir(path)


for file in res:
	if file.endswith('.xml'):
		tree = et.parse(path+file)

		for elt in tree.iter():
			if elt.tag == 'name':
				if not os.path.isdir(elt.text):
					print('creating..directory',elt.text)
					os.mkdir(elt.text)
					shutil.copyfile(path+file,elt.text+'/'+file)
					shutil.copyfile(path+file,elt.text+'/'+file.split('.')[0]+'.jpg')

				else:
					shutil.copyfile(path+file,elt.text+'/'+file)
					shutil.copyfile(path+file,elt.text+'/'+file.split('.')[0]+'.jpg')
					







