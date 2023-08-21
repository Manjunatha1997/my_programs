import redis
import cv2


r = redis.Redis(host='localhost',port=6379,password=None)

cap = cv2.VideoCapture(0)

count = 0
while True:
    ret, frame = cap.read()
    r.set('image'+str(count),str(frame))
    cv2.imshow('image',frame)
    count += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




