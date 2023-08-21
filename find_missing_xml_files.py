
import os
import shutil

path = r"D:\indomim_tirupati\third_part_data\cum_40_jun_15_22\cum_40_jun_15_22\\"


def find_missing(path):
	res = os.listdir(path)
	jpg,xml = [],[]

	for i in res:

		if i.endswith('.xml'):
			k = i.split('.')	
			jpg.append(k[0])
		
		else:
			if i.endswith('.jpg'):
				k = i.split('.')
				xml.append(k[0])

	count = 0
	for i in jpg:
		if not i in xml:
			count += 1
			print("Missing items are: "+i+".xml",count)
			# print("Deleting files are: "+i+".xml",count)
			os.remove(path+i+'.xml')


	print("Total jpg are:",len(xml))
	print("Total xml are:",len(jpg))
	

find_missing(path)
