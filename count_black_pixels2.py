import cv2
import numpy as np

count = 0
img = cv2.imread('/home/manju/Pictures/image.jpg')
# img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

if len(img.shape) == 3:
    for i in img:
        for j in i:
            j = list(j)
            if j == [0]*len(j):
                count += 1
    print('total number of black pixels are:',count)
else:
    if len(img.shape) == 2:
        for i in img:
            i = list(i)
            if i == [0]*len(i):
                count += 1
        print('total number of black pixels are:',count)
