import cv2
import numpy as np
import glob

img_array = []
for filename in glob.glob('D:\\Bridgestone\\Beed bare\\Ok images\\*.bmp'):
    print(filename)
    img = cv2.imread(filename)
    print(type(img))
    height, width, layers = img.shape
    size = (width,height)
    print(size)
    img_array.append(img)


out = cv2.VideoWriter('beed_bare_good.avi',cv2.VideoWriter_fourcc(*'DIVX'), 1, size)

 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()