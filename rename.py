

import os
import cv2
import time
import xml.etree.ElementTree as ET
import glob
import shutil

path = 'C:\\Users\\Manju\\Desktop\\dents\\*.jpg'

res = glob.glob(path)

imagename = 'view14_'
count = 0
for file in res:
    img = cv2.imread(file)
    img = cv2.resize(img,(640,480))
    cv2.imwrite(file.replace(file.split('\\')[-1], imagename+str(count)+'.jpg'),img)
    count += 1
    os.remove(file)
    




