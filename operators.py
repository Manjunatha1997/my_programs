import cv2
import numpy as np

img1 = cv2.imread("opencv/samples/data/imageTextN.png")
img2 = cv2.imread("opencv/samples/data/imageTextR.png")
img1 = cv2.resize(img1,(500,500))
img2 = cv2.resize(img2,(500,500))

bit_and = cv2.bitwise_and(img1, img2)
bit_or = cv2.bitwise_or(img1, img2)
bit_not = cv2.bitwise_not(img1)

# cv2.imshow("image1", img1)
# cv2.imshow("image2", img2)
cv2.imshow("bit and", bit_and)
cv2.imshow("bot or", bit_or)
cv2.imshow("bit not",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()