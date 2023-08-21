import cv2
import numpy as np
def mouse_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),10,(0,0,255),-1)
        points.append((x,y))
        print(points)
        if len(points) >= 2:
            cv2.line(img,points[-1],points[-2],(255,255,0),1)
        cv2.imshow("image",img)

img = np.zeros((512,512,3),np.uint8)
cv2.imshow("image",img)
points = []
cv2.setMouseCallback("image",mouse_event)
cv2.waitKey(0)
cv2.destroyAllWindows()