import cv2
import numpy as np

cv2.namedWindow("image")
def nothing(x):
    pass
cv2.createTrackbar("CP","image",0,100,nothing)
cv2.createTrackbar("switch","image",0,1,nothing)

while True:
    img = cv2.imread("lena.png")
    # img = cv2.imshow("image",img)
    pos = cv2.getTrackbarPos("CP","image")

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    s = cv2.getTrackbarPos("switch","image")
    if s == 0:
        cv2.putText(img, str(pos), (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
    else:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    cv2.imshow("image",img)


cv2.destroyAllWindows()
