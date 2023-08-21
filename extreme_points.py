
import cv2
import numpy as np


image = 'cylinder.jpg'
img = cv2.imread(image)
img = cv2.resize(img,(640,480))

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, thr = cv2.threshold(gray_img,50,100,10)
contours,e= cv2.findContours(thr,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# print(contours,type(contours))
print(len(contours))
print(contours[0])
cv2.drawContours(img,contours,-1,(0,255,0),2)

cv2.imshow('image',img)
cv2.imshow('thr',thr)
cv2.waitKey(0)




# leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
# rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
# topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
# bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])


