
from glob import glob
from os import remove
from cv2 import threshold
from fastai.vision.all import load_learner
import pathlib

from torch import threshold_
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath
import cv2


model = load_learner("C:\\Users\\Manju\\Downloads\\cross_hole.pkl")

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


for i in glob(r'C:\Users\Manju\Downloads\indomim_anno\view_7-Copy\bad_out\\*.png'):
    preds = pred(i,0.85)
    print(preds)



