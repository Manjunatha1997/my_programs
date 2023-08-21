import glob
import json

path = '/home/manju/Downloads/PAVI/'

res = glob.glob(path+'*.json')


all_classes = []

for file in res:
	fr = open(file,'r')
	data = json.load(fr)
	for i in data:
		if i == 'shapes':
			for j in data[i]:
				# print(j,type(j))
				for key in j:
					# print(key,type(key))
					if key == 'label':
						# print(j[key])
						all_classes.append(j[key])

print(set(all_classes))

						