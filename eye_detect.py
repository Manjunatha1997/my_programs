import cv2

face_cascade = cv2.CascadeClassifier("/home/manju/python_programs/opencv/opencv/data/haarcascades/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("/home/manju/python_programs/opencv/opencv/data/haarcascades/haarcascade_eye_tree_eyeglasses.xml")

video = cv2.VideoCapture(0)

while True:
    ret, img = video.read()
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_img,1.1,4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        eye_gray = gray_img[y:y+h, x:x+w]
        eye_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(eye_gray,1.1,4)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(eye_color, (ex, ey), (ex+ew, ey+eh), (255, 0, 0),2)

    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
