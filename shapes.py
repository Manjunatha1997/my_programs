import cv2

img = cv2.imread("lena.png",1)
img = cv2.line(img,(0,0),(100,100),(255,0,0),5)
img = cv2.arrowedLine(img,(0,50),(200,200),(235,229,52),4)
img = cv2.rectangle(img,(100,100),(200,300),(18,18,135),3)
img = cv2.circle(img,(200,500),50,(123,433,233),-1)

cv2.imshow("Image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
