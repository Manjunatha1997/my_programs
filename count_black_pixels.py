import cv2
import numpy as np

count = 0
img = cv2.imread('black_image.jpg')
for i in img:
    for j in i:
        j = list(j)
        if j == [0,0,0]:
            count += 1
print('total number of black pixels are:',count)

