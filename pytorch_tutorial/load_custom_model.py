import torch
import os
import glob
import cv2
import numpy as np


defects = ['person']


def run_inference_hub(hub_weights_path,image,conf=0.7):
	model = torch.hub.load('D:\\yolov5_auto','custom',path=hub_weights_path,source = 'local')
	model.conf = conf
	model.iou = 0.45


	results = model(image)

	labels = results.pandas().xyxy[0]
	labels = list(labels['name'])

	
	result_dict = results.pandas().xyxy[0].to_dict()


	
	for i in range(len(labels)):
		xmin = list(result_dict.get('xmin').values())[i]
		ymin = list(result_dict.get('ymin').values())[i]
		xmax = list(result_dict.get('xmax').values())[i]
		ymax = list(result_dict.get('ymax').values())[i]
		c = list(result_dict.get('class').values())[i]
		name = list(result_dict.get('name').values())[i]

		## bounding box and text 

		if name in defects:
			color = (0,0,255) # bounding box color
		else:
			color = (0,255,0) # bounding box color

		p1, p2 = (int(xmin), int(ymin)), (int(xmax), int(ymax))
		cv2.rectangle(image, p1, p2, color, thickness=2, lineType=cv2.LINE_AA)
		if name:
			
			tf = max(2 - 1, 1)  # font thickness
			w, h = cv2.getTextSize(name, 0, fontScale=2 / 3, thickness=tf)[0]  # text width, height
			outside = p1[1] - h - 3 >= 0  # label fits outside box
			p2 = p1[0] + w, p1[1] - h - 3 if outside else p1[1] + h + 3
			cv2.rectangle(image, p1, p2, color, -1, cv2.LINE_AA)  # filled
			cv2.putText(image, name, (p1[0], p1[1] - 2 if outside else p1[1] + h + 2), 0, 2 / 3, (255,255,255),
						thickness=tf, lineType=cv2.LINE_AA)


	for img in results.imgs:
		return img, labels

predicted_image, detcetor_labels = run_inference_hub('yolov5s.pt',cv2.imread(r'D:\yolov5_auto\data\images\bus - Copy - Copy.jpg'))

cv2.imshow('predected_image',predicted_image)
cv2.waitKey(0)
