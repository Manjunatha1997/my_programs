import cv2
from common_utils import CacheHelper


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        CacheHelper().set_json({'frame':frame})
        
