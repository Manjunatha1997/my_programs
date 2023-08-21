import cv2
import math

img = cv2.imread('/home/manju/Pictures/scr.png')


print(img.shape)


x1, y1 = 10,20
x2 ,y2 = 80, 40


cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),3)
cv2.line(img,(x1,y2),(x2,y2),(0,255,0),2)

p1 = (x1,y1)
p2 = (x2,y2)

# crop = img[200:200+1366,200:200+768]
crop  = img[y1:y2,x1:x2]
print('crop shape=============>',crop.shape)
# cv2.imshow('crop',crop)

distance = math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))

print(distance)

cv2.putText(img, 'diagonal distance: '+str(distance), p2, cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (255, 0, 0), 1, cv2.LINE_AA)


cv2.imshow('image',img)
cv2.waitKey(0)

