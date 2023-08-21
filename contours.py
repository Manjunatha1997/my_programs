import cv2
import numpy as np

image = '/home/manju/Desktop/MSIL/19/wavyness_breakage_19_04_2021/wavyness_breakage_19_04_2021_1.jpg'
image = 'shapes.jpg'
img = cv2.imread(image)
img = cv2.resize(img,(640,480))

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, thr = cv2.threshold(gray_img,127,255,0)
_,contours,_ = cv2.findContours(thr,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)


temp = []
for c in contours:
    print(cv2.contourArea(c))
    temp.append(cv2.contourArea(c))
    print(c,'every contour')


print(contours[0])
cv2.drawContours(img,contours,-1,(0,0,255),4)

cv2.imshow('image',img)
cv2.waitKey(0)

