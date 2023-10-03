

import os
import cv2
import time
import xml.etree.ElementTree as ET
import glob
import shutil
import bson
from datetime import datetime
import math


def create_dir(path):
    if not os.path.isdir(path):
        os.makedirs(path)





resources = ['suma','akshata','praveen','nijant','saidi','bharati','parashuram']


path = r'D:\Generic_needle_punch_OCR\dataset\2023-09-28\dot_peen_marking_ocr'

res = glob.glob(os.path.join(path,'*'))


for resource in resources:
    create_dir(os.path.join(path,resource))


split_count = math.ceil(len(res) / len(resources)) 
count = 1
r_count = 0
for file in res:
    if not os.path.isfile(file):
        continue
    img = cv2.imread(file)
    c_date = str(datetime.now().strftime('%Y-%M-%d'))
    random_file_name = c_date + '_' +str(bson.ObjectId()) + '.jpg' 


    if count == split_count:
        count = 1
        r_count += 1
        if r_count > len(resources)-1:
            r_count = 0

    else:
        count += 1

    print(f' {resources[r_count]} :: {count} :: {r_count} ')
    out_path = os.path.join(path,resources[r_count])
    out_file_name = os.path.join(out_path,random_file_name)
    if img is not None:
        cv2.imwrite(out_file_name,img)
    





