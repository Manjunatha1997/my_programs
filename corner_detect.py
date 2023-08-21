import cv2
import numpy as np
img = cv2.imread("chessboard.png")
img = cv2.resize(img,(600,600))
cv2.imshow("image",img)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)     

dest = cv2.cornerHarris(gray,2,5,0.04)
dest = cv2.dilate(dest,None)

img[dest > 0.01 * dest.max()] = [0,0,255]
cv2.imshow("result",img)


if  cv2.waitKey(0):
    cv2.destroyAllWindows()


