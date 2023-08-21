import cv2

img = cv2.imread("opencv/samples/data/messi5.jpg")
img2 = cv2.imread("opencv/samples/data/opencv-logo-white.png")
img = cv2.resize(img,(500,500))
img2 = cv2.resize(img2,(500,500))


res = cv2.add(img,img2)
res = cv2.addWeighted(img,.5,img2,.9,0)

cv2.imshow("image",res)
cv2.waitKey(0)
cv2.destroyAllWindows()