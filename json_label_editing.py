
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
						for key in j:
							if key == 'label':
								print(j[key])

								j[key] = label
								print(j[key])
								print('*********')

		fr.close()

		with open(path+file, 'w') as json_file:
		  json.dump(data, json_file,indent=4)


# Input path directory
path = '/home/manju/Downloads/Deeplab_Images/'

# Required Label name
label_name = 'Black_Sealent'
json_label_edit(path,label_name)