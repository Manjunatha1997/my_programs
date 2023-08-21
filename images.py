import cv2

img = cv2.imread("opencv/samples/data/lena.jpg")

cv2.imshow("image", img)

if cv2.waitKey(0) == 27:
    print("not saved")
else:
    if cv2.waitKey(0) == ord('s'):
        cv2.imwrite("lena.png", img)
        cv2.destroyAllWindows()
