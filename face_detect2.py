import cv2

face_cascade = cv2.CascadeClassifier("//home/manju/python_programs/opencv/opencv/data/haarcascades/haarcascade_frontalface_default.xml")
video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.2,4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 155), 2)
    cv2.imshow("Video",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()