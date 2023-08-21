
import json

with open('/home/manju/Downloads/Deeplab_Images/sagar1.json') as f:
	data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
	
	
	for i in data:
		if i == 'shapes':
			for j in data[i]:
				# print(j,type(j))
				for key in j:
					# print(key,type(key))
					if key == 'label':
						print(j[key])
						j[key] = 'replaced....'
						print(j[key])

	# json.dump(data,f)
	print(data,type(data))
