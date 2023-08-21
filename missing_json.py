import os
import shutil


path = '/home/manju/Downloads/manjunath/with_cam2/'




def find_missing(path):
	res = os.listdir(path)
	jpg,json = [],[]

	for i in res:

		if i.endswith('.jpg'):
			k = i.split('.')	
			jpg.append(k[0])
		
		else:
			if i.endswith('.json'):
				k = i.split('.')
				json.append(k[0])

	count = 0
	for i in jpg:
		if not i in json:
			count += 1
			print("Missing items are: "+i+".jpg",count)
			# print("Deleting files are: "+i+".jpg",count)
			# os.remove(path+i+'.jpg')
			# shutil.move(path+i+'.jpg','/home/manju/Downloads/manjunath/extra_json/'+i+'.jpg')


	print("Total json are:",len(json))
	print("Total jpg are:",len(jpg))
	
find_missing(path)
