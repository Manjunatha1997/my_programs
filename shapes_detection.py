import cv2

img = cv2.imread('shapes.jpg')

cv2.rectangle(img,(0,100),(100,200),(0,255,255))

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thr = cv2.threshold(gray,240,255,cv2.THRESH_BINARY)

_,contours,_ = cv2.findContours(thr,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    cv2.drawContours(img,[approx],0,(0,0,255),2)
    x = approx.ravel()[0]
    y = approx.ravel()[1]


    if len(approx) == 3:
        # cv2.putText(img,'Triangle',(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,100,120),2)
        # print(x,y)
        pass
    elif len(approx) == 4:
        cv2.putText(img,'Rectangle',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(12,23,32),2)
        print(x,y)


    else:
        pass



cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()
