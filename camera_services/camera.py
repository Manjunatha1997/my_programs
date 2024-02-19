import cv2
import ai_settings as settings
from common_utils import CacheHelper


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if ret:
        print(frame.shape)
        CacheHelper().set_json({'input_frame':frame})
    else:
        cap = cv2.VideoCapture(0)

