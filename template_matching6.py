import cv2
import numpy as np
import glob
import os, os.path

files = glob.glob("/home/manju/Desktop/task/*.jpg")

lst = []

for file in files:

    img = cv2.imread(file)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    template = cv2.imread("/home/manju/Desktop/temp.jpg", 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

    thr = 0.3
    loc = np.where(res >= thr)[::-1]
    print(loc)
    loc = zip(*loc)
    for i in loc:
        cv2.rectangle(img,i,(i[0]+w,i[1]+h),(0,0,255),2)
    cv2.imshow("image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
