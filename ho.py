import cv2
import numpy as np

# Read image.
img = cv2.imread('image.jpg', cv2.IMREAD_COLOR)

# Convert to grayscale.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur using 3 * 3 kernel.
gray_blurred = cv2.blur(gray, (3, 3))

# gray_blurred = cv2.GaussianBlur(gray_blurred,(5,5),0)



# ret,th1 = cv2.threshold(gray_blurred,125,255,cv2.THRESH_BINARY)

thr = cv2.adaptiveThreshold(gray_blurred,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
# thr = cv2.adaptiveThreshold(gray_blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)


# Apply Hough transform on the blurred image.
detected_circles = cv2.HoughCircles(thr,
				cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
			param2 = 30, minRadius = 1, maxRadius = 40)

# Draw circles that are detected.
if detected_circles is not None:

	# Convert the circle parameters a, b and r to integers.
	detected_circles = np.uint16(np.around(detected_circles))
	# print("detected_circles---",detected_circles)

	total = 0

	for pt in detected_circles[0, :]:
		a, b, r = pt[0], pt[1], pt[2]
		
		total = total + 1

		img = cv2.circle(img, (a, b), r, (0, 255, 0), 2)

	print("total number of circles---",total)
	cv2.imshow("Detected Circle", img)
	cv2.imwrite('out1.jpg',img)
	cv2.waitKey(0)






