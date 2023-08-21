import numpy as np
import glob
import cv2
import numpy as np
from fastai.vision.all import *
import platform
import pathlib

os_type = platform.system()
if os_type == 'Windows':
    pathlib.PosixPath = pathlib.WindowsPath





model = load_learner(r'd:\indomim_tirupati\classyfy_det\burr35_cross.pkl')



for file in glob.glob(r'C:\Users\Manju\Downloads\indomim_anno\view_7-Copy\bad_out\test\*.png'):
    img = cv2.imread(file)

    pred,_,thr=model.predict(img)  
    print(pred)
