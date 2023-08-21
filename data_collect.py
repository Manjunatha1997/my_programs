import cv2
import json
import os
from datetime import datetime

with open('config.json') as f:
	data = json.load(f)

vids = {i["camera_index"]:cv2.VideoCapture(i["Camera_id"]) for i in data}

print(vids)

data_dir = 'dataset'



counter = 1
num_frames = 5
while counter <= num_frames:
	for index,cap in vids.items():
		all_frames = {}
		ret, frame = cap.read()
		all_frames[index] = frame

		for i,j in all_frames.items():
			path = data_dir+'/'+i

			if os.path.isdir(path):
				cv2.imwrite(path+'/'+i+str(datetime.now())+'.jpg',j)
			else:
				os.makedirs(path)
				cv2.imwrite(path+'/'+i+str(datetime.now())+'.jpg',j)

	print(counter,' frame saved .....')
	counter += 1


