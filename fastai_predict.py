
from glob import glob
from os import remove
from cv2 import threshold
from fastai.vision.all import load_learner
import pathlib

from torch import threshold_
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath
import cv2


model = load_learner(r"C:\Users\Manju\Downloads\burr35.pkl")

conf = 0.8


def pred(file,conf):
    res = []
    pred,_,thres = model.predict(file)
    t=[pred if thres[i] > conf else " " for i in range(len(thres)) ]
    if len(t)!=0:
        res.append(t)
    x = res[0]

    if len(x) > 1:
        x.remove(" ")

    return x[0]


for i in glob(r'C:\Users\Manju\Downloads\indomim_anno\view_20Copy\good\\*.png'):
    img = cv2.imread(i)

    xmin, ymin, xmax, ymax = 224, 138, 374, 281 
    img_crop = img[ymin:ymax,xmin:xmax]
    preds = pred(img_crop,0.85)
 
    cv2.rectangle(img,(xmin,ymin),(xmax,ymax),(0,0,255),2)

        
    # font
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    
    # fontScale
    fontScale = 1
    
    # Blue color in BGR
    color = (255, 0, 0)
    
    # Line thickness of 2 px
    thickness = 2
    img = cv2.putText(img, preds, (xmin,ymin), font, 
                fontScale, color, thickness, cv2.LINE_AA)
    cv2.imshow('image',img)
    cv2.waitKey(0)

    



