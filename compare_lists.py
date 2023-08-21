
import os
from collections import Counter


path_duplicate = '/home/manju/Downloads/image_data/train/'
path_original = '/home/manju/Downloads/image_data/crop_train_dir/'

original = os.listdir(path_original)

duplicate = []

res = os.walk(path_duplicate)

for obj in res:
	files = obj[2]

	for file in files:
		duplicate.append(file)

res = list((Counter(original) - Counter(duplicate)).elements()) 


print(type(res))
print(res)
# print result 
print("The list after performing the subtraction : " + str(res)) 

print(list(Counter(original)-Counter(duplicate)))
print((Counter(original)-Counter(duplicate)))



