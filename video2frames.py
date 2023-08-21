import cv2
import os
import glob
from datetime import datetime

from pathy import shutil



videos_path = 'D:\\DHL\\*.mp4'


out_folder_name = "D:\\DHL_data\\"
image_name = "DHL"



def video_to_frames(cam,out_folder_name,image_name):

    time = datetime.now()

    time = str(time).split(' ')
    time = time[0]


    if not out_folder_name.endswith('/'):
        out_folder_name = out_folder_name + '/'

    try:
        if not os.path.exists(out_folder_name):
            os.mkdir(out_folder_name)
    except OSError:
        print('Error: Creating directory of',out_folder_name)

    currentframe = 0
    for i in cam:

        print(i)
            
        while (True):
            ret, frame = i.read()
            if ret:
                name =out_folder_name+image_name+'_'+time+ '_' + str(currentframe) + '.jpg'
                # print('Creating...' + name)
                cv2.imwrite(name, frame)
                currentframe += 1
            else:
                break

        i.release()
        cv2.destroyAllWindows()

caps = [cv2.VideoCapture(video) for video in glob.glob(videos_path)]


video_to_frames(caps,out_folder_name,image_name)


