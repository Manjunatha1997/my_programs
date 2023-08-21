import cv2

face_cascade = cv2.CascadeClassifier("opencv/data/haarcascades/haarcascade_frontalface_default.xml")
img = cv2.imread("faces.jpeg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,1.2,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w, x+h),(0,0,255),2)

img = cv2.resize(img,(600,600))
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()