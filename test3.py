import os
import shutil
path = '/home/manju/Desktop/new/'
res = os.walk(path)



out = '/home/manju/Desktop/out/'
count = 0
for obj in res:
	root = obj[0]
	files = obj[2]

	for file in files:
		if file.endswith('.jpg'):
			count += 1
			if count <= 3:
				# print(root+'/'+file,count)
				shutil.copyfile(root+'/'+file,out+file)
	else:
		count = 0
		print('*'*50)

res1 = os.walk(path)

for obj1 in res1:
	root1 = obj1[0]
	files1 = obj1[2]

	for xml_file in files1:
		if xml_file.endswith('.xml'):
			for img in os.listdir(out):
				if img.split('.')[0] == xml_file.split('.')[0]:
					# print(xml_file)
					shutil.copyfile(root1+'/'+xml_file,out+xml_file)