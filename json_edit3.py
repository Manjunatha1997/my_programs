
import json
import glob
import os


def json_label_edit(path,label=None):

	files = os.listdir(path)

	for file in files:
		if file.endswith('.json'):

			fr = open(path+file,'r')
			data = json.load(fr)
			for i in data:
				if i == 'shapes':
					for j in data[i]:
						# print(j,type(j))
						for key in j:
							# print(key,type(key))
							if key == 'label':
								print(j[key])

								j[key] = label
								print(j[key])
								print('*********')

		# print(data,type(data))
		fr.close()

		with open(path+file, 'w') as json_file:
		  json.dump(data, json_file,indent=4)


path = '/home/manju/Downloads/tttttt/'
json_label_edit(path,'hello')