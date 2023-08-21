
import cv2
import multiprocessing

config_list = [
	{"camera_id":0,"camera_index":"1cam"},
	{"camera_id":"C:/Users/Manju/Videos/a/demo.mp4","camera_index":"video"}
]

def cam_preview(preview_name,cam_id):
    
    cap = cv2.VideoCapture(cam_id)
    while True:
        ret, frame = cap.read()
        print(cam_id,preview_name,ret)
        if ret:
            cv2.imshow(preview_name,frame)
            if cv2.waitKey(1) and 0xFF == ord('q'):
                break
        else:
            cv2.VideoCapture(cam_id)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    thread_pool = {}
    

    for distro in config_list:
        thread_pool[distro['camera_id']] = multiprocessing.Process(target=cam_preview,args=(distro['camera_index'], distro['camera_id']))

    for tt in thread_pool:
        thread_pool[tt].start()
    for tt in thread_pool:
        thread_pool[tt].join()





