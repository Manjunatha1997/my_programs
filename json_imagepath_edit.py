import glob
import json


path = '/home/manju/Downloads/tttttt/*.json'

files = glob.glob(path)

for file in files:

	fr = open(file)

	data = json.load(fr)

	for i in data:
		if i == 'imagePath':
			data[i] = file.split('/')[-1].split('.')[0]+'.jpg'

	fr.close()
	with open(file, 'w') as json_file:
	  json.dump(data, json_file,indent=4)
