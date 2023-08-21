import cv2
import numpy as np
import glob

files = glob.glob('C:\\Users\\Manju\\Pictures\\Camera Roll\\maini_measure\\new\\*.jpg')


for i in files:
    img = cv2.imread(i)
    # img = cv2.GaussianBlur(img,(5,5),0)
    img = cv2.GaussianBlur(img,(1,1),0)


    # edge_detect_img = cv2.Canny(img,100,150)
    edge_detect_img = cv2.Canny(img,40,150)

    cimg = edge_detect_img


    # cv2.imshow(i[25:], edge_detect_img)
    circles = cv2.HoughCircles(cimg,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)

    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

    cv2.imshow('detected circles',cimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imshow(i[50:], edge_detect_img)

    cv2.waitKey(0)