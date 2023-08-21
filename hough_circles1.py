import cv2
import numpy as np
import glob
# Read image.

files = glob.glob('C:\\Users\\Manju\\Pictures\\Camera Roll\\maini_measure\\new\\WIN_20220324_11_46_39_Pro.jpg')

for imgage in files:

    img = cv2.imread(imgage, cv2.IMREAD_COLOR)
    img = cv2.resize(img,(640,360)) #rmin=50 rmax=70


    # Convert to grayscale.
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Blur using 3 * 3 kernel.
    gray_blurred = cv2.blur(gray, (3, 3))

    # Apply Hough transform on the blurred image.
    detected_circles = cv2.HoughCircles(gray_blurred,
                    cv2.HOUGH_GRADIENT, 1, 20, param1 = 20,
                param2 = 30, minRadius = 50, maxRadius = 70)

    # Draw circles that are detected.
    if detected_circles is not None:

        # Convert the circle parameters a, b and r to integers.
        detected_circles = np.uint16(np.around(detected_circles))
        # print("detected_circles---",detected_circles)

        total = 1
        rad = []
        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]
            rad.append(r)
        # if r == 11 or r == 10 or r == 19 or r == 20 or r == 18 or r == 17 or r == 22 or r == 12 or r == 13 or r == 23 or r == 24 or r == 21 or r == 9 or r == 15 or r == 30 or r == 14 or r == 16:
        #     total = total + 1

            # Draw the circumference of the circle.
            cv2.circle(img, (a, b), r, (0, 255, 0), 2)

            # Draw a small circle (of radius 1) to show the center.
            # cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
        
    print("total number of circles---",total)
    cv2.imshow("Detected Circle", img)
    cv2.waitKey(0)
    print(rad,len(rad))


