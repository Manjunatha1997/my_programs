
import json
import cv2
import pickle
import redis

with open('config.json') as f:
    data = json.load(f)
vids = {}

for i in data:
    vids[i['camera_index']] = cv2.VideoCapture(i['camera_id'])

while True:
    all_frames = {}
    for i,j in vids.items():
        j.set(cv2.CAP_PROP_FRAME_WIDTH,640)
        j.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
        ret, frame = j.read()
        all_frames[i] = frame
     
    for k,v in all_frames.items():
        print(k)
