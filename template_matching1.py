import cv2
import numpy as np

img = cv2.imread("/home/manju/Desktop/MSIL/15/breakage_data_500_images/breakage_15_04_2021_1.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

template = cv2.imread("/home/manju/Pictures/ref.png",cv2.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
thr = 0.7
loc = np.where(res >= thr)[::-1]
print(loc)
for i in zip(*loc):
    print(i)
    cv2.rectangle(img,i,(i[0]+w, i[1]+h),(0,0,255),2)

    
cv2.imshow("image",img)
cv2.imshow("template",template)

cv2.waitKey(0)
cv2.destroyAllWindows()

