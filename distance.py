

import cv2
import numpy as np


img = cv2.imread('/home/manju/Pictures/scr.png')


imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# cnt1 = cv.drawContours(im, contours, 1, (0,0,255), 3)
# cnt2 = cv.drawContours(im, contours, 3, (0,0,255), 3)


# contours,hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[1]
contour_img = np.zeros_like(img)
cv2.fillPoly(contour_img, contours, 220)



cv2.imshow('image',img)
cv2.waitKey(0)


