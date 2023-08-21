import cv2,time


img = cv2.imread('shapes.jpg')
img2 = img

height, width, channels = img.shape
# Number of pieces Horizontally
CROP_W_SIZE  = 3
# Number of pieces Vertically to each Horizontal
CROP_H_SIZE = 2

for ih in range(CROP_H_SIZE ):
    for iw in range(CROP_W_SIZE ):

        x = int(width/CROP_W_SIZE * iw)
        y = int(height/CROP_H_SIZE * ih)
        h = int(height / CROP_H_SIZE)
        w = int(width / CROP_W_SIZE )
        print(x,y,h,w)


        img = img[y:y+h, x:x+w]



        NAME = str(time.time())
        import os
        if not os.path.isdir('CROP'):
            os.mkdir('CROP')
        cv2.imwrite("CROP/" + str(time.time()) +  ".png",img)
        # cv2.imshow('image',)
        img = img2