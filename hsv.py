import cv2
import numpy as np

def nothing(x):
    pass

# cap = cv2.VideoCapture(0)
cv2.namedWindow("Trackbar")
cv2.createTrackbar("LH","Trackbar",0,255,nothing)
cv2.createTrackbar("LS","Trackbar",0,255,nothing)
cv2.createTrackbar("LV","Trackbar",0,255,nothing)

cv2.createTrackbar("UH","Trackbar",255,255,nothing)
cv2.createTrackbar("US","Trackbar",255,255,nothing)
cv2.createTrackbar("UV","Trackbar",255,255,nothing)


while True:
    frame = cv2.imread("opencv/samples/data/smarties.png")
    # ret, frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


    l_h = cv2.getTrackbarPos("LH","Trackbar")
    l_s = cv2.getTrackbarPos("LS","Trackbar")
    l_v = cv2.getTrackbarPos("LV","Trackbar")

    u_h = cv2.getTrackbarPos("UH","Trackbar")
    u_s = cv2.getTrackbarPos("US","Trackbar")
    u_v = cv2.getTrackbarPos("UV","Trackbar")

    l_b = np.array([l_h,l_s,l_v])
    u_b = np.array([u_h,u_s,u_v])

    mask = cv2.inRange(hsv,l_b,u_b)
    res = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)

    key = cv2.waitKey(1)
    if key == 27:
        break
# cap.release()
cv2.destroyAllWindows()