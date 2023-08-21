from tkinter import Frame
import cv2

import numpy as np 
import glob 


# frame=cv2.imread("LINE1_MR192_55.jpg")


# x1=100
# y1=110
# x2=585
# y2=385
# width=640
# height=480

# x1=120
# y1=170
# x2=510
# y2=400
# width=640
# height=480


x1=60
y1=70
x2=595
y2=395
width=640
height=480


c=0
path="C:\\Users\\Manju\\Downloads\\annotations\\annotations\\NA\\*.jpg"

for file in glob.glob(path):
    frame = cv2.imread(file)
    # frame = cv2.resize(frame,(680,480))
    frame = cv2.resize(frame,(640,480))

    c=c+1
    for i in range(x1):
        cv2.line(frame,(i,0),(i,height),(0,0,0),1)

    for i in range(width-x2):
        cv2.line(frame,(x2 +i,0),(x2+i,height),(0,0,0),1)

    for i in range(y1):
        cv2.line(frame,(0,i),(width,i),(0,0,0),1)

    for i in range(height-y2):
        cv2.line(frame,(0,y2+i),(width,y2+i),(0,0,0),1)

    # cv2.imwrite("D:\\Suprajit\\suprajit_line2_14\\197_l2c\\MR197_L2a_%d.jpg" % c,frame)
    cv2.imwrite(file,frame)
    print(file)



# cv2.imshow("original",frame)
# cv2.waitKey(0)
