import cv2


img = cv2.imread('/home/manju/Downloads/whats.jpg')
gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# edge = cv2.Canny(gray_image,127,255)
ret,edge = cv2.threshold(gray_image,200,255,0)

_,con,_ = cv2.findContours(edge,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)



print(len(con),type(con))

temp = []
for c in con:
    print(cv2.contourArea(c))
    temp.append(cv2.contourArea(c))
    print(c,'every contour')

print('smallest contour is:',min(temp))
print('biggest contour is:',max(temp))
print('length of  contour is:',len(temp))
print(len(con))


cv2.drawContours(img,con,-1,(0,0,255),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
