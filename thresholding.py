import cv2

img = cv2.imread("opencv/samples/data/gradient.png")

ret, th1 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
ret, th1 = cv2.threshold(img,100,255,cv2.THRESH_MASK)
ret, th1 = cv2.threshold(img,100,255,cv2.THRESH_TOZERO)
ret, th1 = cv2.threshold(img,100,255,cv2.THRESH_TRUNC)
ret, th1 = cv2.threshold(img,100,255,cv2.THRESH_BINARY_INV)
ret, th1 = cv2.threshold(img,100,255,cv2.THRESH_TOZERO_INV)



cv2.imshow("image", img)
cv2.imshow("th1", th1)
cv2.waitKey(0)
cv2.destroyAllWindows()
