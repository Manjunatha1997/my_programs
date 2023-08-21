import cv2
import numpy as np

def mouse_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        text = str(x)+', '+str(y)
        cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,122,111),2)
        cv2.imshow("image",img)

img = np.zeros((512,512,3),np.uint8)
cv2.imshow("image",img)
cv2.setMouseCallback("image",mouse_event)
cv2.waitKey(0)
cv2.destroyAllWindows()