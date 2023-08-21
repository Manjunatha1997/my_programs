import cv2
import os
import glob

path = '/home/manju/python_programs/sel/scratch_defect/*.jpg'
# res = os.listdir(path)

res = glob.glob(path)

if not os.path.isdir('scratch_resized'):
	os.mkdir('scratch_resized')

for i in res:
	print(i)
	img = cv2.imread(i)
	r = cv2.resize(img,(640,480))
	cv2.imwrite('scratch_resized'+'/'+i.split('/')[-1],r)