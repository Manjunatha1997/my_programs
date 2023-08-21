import cv2

img = cv2.imread("chessboard.png",0)
img1 = cv2.GaussianBlur(img,(5,5),0)

sobelx = cv2.Sobel(img,cv2.CV_64F,1,0)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1)
canny = cv2.Canny(img,100,200)
canny1 = cv2.Canny(img1,100,200)

cv2.imshow("image",img)
cv2.imshow("sobelx",sobelx)
cv2.imshow("sobely",sobely)
cv2.imshow("blur",img1)
cv2.imshow("canny",canny)
cv2.imshow("canny1",canny1)

cv2.waitKey(0)
cv2.destroyAllWindows()
