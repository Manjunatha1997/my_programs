import cv2

img = cv2.imread('black_image.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

print(img)

for i in img:
    print(i,len(i))
    input()