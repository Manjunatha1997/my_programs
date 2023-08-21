import cv2
import numpy as np
import glob

inp_path = "/home/manju/Desktop/task/*.jpg"
files = glob.glob(inp_path)
print(files)

lst = []
for file in files:
	print(file)
	img = cv2.imread(file,0)

	template = cv2.imread("/home/manju/Desktop/temp.jpg", cv2.IMREAD_GRAYSCALE)
	w, h = template.shape[::-1]

	res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)

	thr = 0.8
	loc = np.where(res >= thr)[::-1]
	loc = zip(*loc)

try:

	for i in loc:
		print(i)
		lst.append(i)
except:
	print(lst,len(lst),len(lst))



