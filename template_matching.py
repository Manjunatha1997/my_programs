import cv2
import numpy as np
img1 = cv2.imread("/home/manju/Downloads/new_ms/test/Mastic_Sealant_24_04_2021_resized_115.jpg")

img = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

template = cv2.imread("/home/manju/Pictures/template.jpg",0)
template2 = cv2.imread("/home/manju/Pictures/template2.jpg",0)
w, h = template.shape[::-1]
w2, h2 = template2.shape[::-1]

res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
res2 = cv2.matchTemplate(img,template2,cv2.TM_CCOEFF_NORMED)

threshold = 0.9
loc = (np.where(res >= 0.9)[::-1])
loc2 = (np.where(res2 >= 0.97)[::-1])

for i in zip(*loc):
	cv2.rectangle(img1,i,(i[0]+w,i[1]+h),(0,255,0),1)
	# print(i,(i[0]+w,i[1]+h))

for i in zip(*loc2):
	cv2.rectangle(img1,i,(i[0]+w2,i[1]+h2),(0,255,0),1)
	# print(i,(i[0]+w,i[1]+h))



cv2.imshow("image", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()