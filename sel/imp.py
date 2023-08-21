import cv2
import os

path = '/home/manju/python_programs/sel/burr/'
res = os.listdir(path)

for i in res:
    img = path+i
    img = cv2.imread(img)
    cv2.imwrite(path+i,img)


