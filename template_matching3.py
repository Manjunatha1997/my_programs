import cv2
import numpy as np
import os

walk = os.walk("/home/manju/Desktop/lincode/Manju(MR192)")

for obj in walk:
    files = obj[2]
    all_files = []
    for f in files:
        if f.endswith(".jpg"):
            all_files.append(obj[0]+"/"+f)

    for file in all_files:
        # print(file,type(file))
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
        # cv2.imshow("image",img)
        # cv2.imwrite(file,img)
        # cv2.waitKey(0)
    # cv2.destroyAllWindows()



