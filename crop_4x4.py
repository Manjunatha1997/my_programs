import glob
import os
import cv2
from datetime import date, datetime

path = 'C:\\Users\\Manju\\Downloads\\bottom_no_solder\\crops_need\\'

out_path = 'C:\\Users\\Manju\\Downloads\\bottom_no_solder\\crops_need\\'


if not os.path.isdir(out_path):
    os.makedirs(out_path)


res = glob.glob(path+'*.PNG')


for file in res:

    fname = file.split('\\')[-1].split('.')[0]
    # print(fname)
    print(file)

    img =  cv2.imread(file)
    image_copy = img.copy() 
    imgheight=img.shape[0]
    imgwidth=img.shape[1]
    M = 270
    N = 480
    x1 = 0
    y1 = 0

    for y in range(0, imgheight, M):
        for x in range(0, imgwidth, N):
            if (imgheight - y) < M or (imgwidth - x) < N:
                break
                
            y1 = y + M
            x1 = x + N

            # check whether the patch width or height exceeds the image width or height
            if x1 >= imgwidth and y1 >= imgheight:
                x1 = imgwidth - 1
                y1 = imgheight - 1
                #Crop into patches of size MxN
                tiles = image_copy[y:y+M, x:x+N]
                #Save each patch into file directory
                cv2.imwrite(out_path+fname+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
                cv2.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)
            elif y1 >= imgheight: # when patch height exceeds the image height
                y1 = imgheight - 1
                #Crop into patches of size MxN
                tiles = image_copy[y:y+M, x:x+N]
                #Save each patch into file directory
                cv2.imwrite(out_path+fname+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
                cv2.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)
            elif x1 >= imgwidth: # when patch width exceeds the image width
                x1 = imgwidth - 1
                #Crop into patches of size MxN
                tiles = image_copy[y:y+M, x:x+N]
                #Save each patch into file directory
                cv2.imwrite(out_path+fname+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
                cv2.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)
            else:
                #Crop into patches of size MxN
                tiles = image_copy[y:y+M, x:x+N]
                #Save each patch into file directory
                cv2.imwrite(out_path+fname+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
                cv2.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)





