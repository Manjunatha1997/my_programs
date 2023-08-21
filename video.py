
import cv2
# cap = cv2.VideoCapture('http://192.168.1.111:8080')
cap = cv2.VideoCapture(0)
# print(cap,type(cap))

# ret,frame = cap.read()
# print(ret,frame)


while True:
    
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    # print(frame.shape)
    xmin,ymin,xmax,ymax = 0,0,640,480


    frame = cv2.circle(frame,(0,0),5,(0,255,0),-1)
    frame = cv2.circle(frame,(640,480),5,(0,255,0),-1)
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        
        break
    c = 0
    if cv2.waitKey(1) & 0xFF == ord('s'):
        c += 1
        img_crop = frame[ymin:ymax,xmin:xmax]
        cv2.imwrite('/home/manju/Desktop/delete/'+str(c)+'iiiiiiiiii.jpg',img_crop)
        # cv2.imshow('crop',img_crop)
        # print('saaaa')


cap.release()
cv2.destroyAllWindows()
