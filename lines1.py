import cv2
import numpy as np

img = cv2.imread('black_image.jpg')
# img = np.ones([800,600,3],dtype=np.uint8)
# img.fill(255)


# img = cv2.imread('/home/manju/Desktop/magnaflux/Crack/Crack_0.jpg')
# img = cv2.resize(img,(100,100))
# gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

height, width, channel = img.shape


# print(height,width)

# vertical lines
# cv2.line(img,(10,0),(10,500),(0,0,255),1)
# cv2.line(img,(20,0),(20,500),(0,0,255),1)

# horizontal lines
# cv2.line(img,(0,10),(width,10),(0,0,255),1)


size = 50

def ver():
    x1, y1, x2, y2 = 0, 0, 0, 0
    x1 = 0
    while x1 < width:

        cv2.line(img, (x1, 0), (x2, height), (0, 0, 255), 1)
        x1 += size
        x2 += size


def hor():
    x1, y1, x2, y2 = 0, 0, 0, 0
    y1 = 0
    while y1 < height:
        # if img[] == [0,0,0]
        cv2.line(img, (x1, y1), (width, y2), (0, 0, 255), 1)
        y1 += size
        y2 += size


def circle():
    cv2.circle(img, (300, 300), 100, (255, 255, 255), -1)

    # cv2.line(img, (210, 255), (210, 345), (0, 0, 255), 1)
    # cv2.line(img, (220, 240), (220, 360), (0, 0, 255), 1)
    # cv2.line(img, (230, 230), (230, 370), (0, 0, 255), 1)
    # cv2.line(img, (240, 220), (240, 380), (0, 0, 255), 1)
    # cv2.line(img, (250, 210), (250, 385), (0, 0, 255), 1)
    # cv2.line(img, (260, 210), (260, 390), (0, 0, 255), 1)
    # cv2.line(img, (270, 205), (270, 400), (0, 0, 255), 1)


hor()
circle()
ver()


hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_white = np.array([0,0,0], dtype=np.uint8)
upper_white = np.array([0,0,255], dtype=np.uint8)

# Threshold the HSV image to get only white colors
mask = cv2.inRange(hsv, lower_white, upper_white)
# Bitwise-AND mask and original image
res = cv2.bitwise_and(img,img, mask= mask)




# cv2.imshow('frame',img)
# cv2.imshow('mask',mask)
cv2.imshow('res',res)



cv2.imshow('image', img)
# cv2.imshow('gray image',gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
