import cv2
import numpy as np
import os

path = "/home/manju/Desktop/test/"
output_path = "/home/manju/Desktop/out/"

files = os.listdir(path)
print(files)
for f in files:
    file = path + f
    print(file)
    img = cv2.imread(file)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    template = cv2.imread("/home/manju/Desktop/template.jpg",cv2.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
    thr = 0.98
    loc = np.where(res >= thr)[::-1]
    loc = zip(*loc)
    for i in loc:
        cv2.rectangle(img,i,(i[0]+w,i[1]+h),(0,0,255),2)
    cv2.imshow(output_path+f,img)
    cv2.imwrite(output_path+f,img)
    # cv2.waitKey(0)
    cv2.destroyAllWindows()