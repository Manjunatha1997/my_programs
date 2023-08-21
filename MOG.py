
import cv2
import numpy as np


cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
	ret, frame = cap.read()

	fgmask = fgbg.apply(frame)

	cv2.imshow('frame',frame)
	cv2.imshow('mask',fgmask)

	k = cv2.waitKey(30) & 0xFF
	if k == 27 or k == ord('q'):
		break





cap.release()
cv2.destroyAllWindows()





