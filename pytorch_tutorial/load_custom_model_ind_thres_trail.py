import torch
import os
import glob
import cv2
import numpy as np


defects = [] #['bus','chair','tv','bottle','person']
ind_thresh = {} #{'bus':0.1,'person':0.1,'chair':0.1}
label_captitalize = False
rename_labels = {}


def load_model():
	model = torch.hub.load('D:\\yolov5_auto','custom',path='yolov5s.pt',source = 'local')
	model.conf = 0.45
	model.iou = 0.45
	return model

model = load_model()

def run_inference_hub(image):
	
	results = model(image)

	labels = results.pandas().xyxy[0]
	labels = list(labels['name'])

	
	result_dict = results.pandas().xyxy[0].to_dict()

	
	labels_ = []
	coordinates = []
	for i in range(len(labels)):
		xmin = list(result_dict.get('xmin').values())[i]
		ymin = list(result_dict.get('ymin').values())[i]
		xmax = list(result_dict.get('xmax').values())[i]
		ymax = list(result_dict.get('ymax').values())[i]
		c = list(result_dict.get('class').values())[i]
		name = list(result_dict.get('name').values())[i]
		confidence = list(result_dict.get('confidence').values())[i]

		
		

		## bounding box and text 

		if name in defects:
			color = (0,0,255) # Red color bounding box 
		else:
			color = (0,128,0) # Green color bounding box 

		if name in ind_thresh:
			try:
				if ind_thresh.get(name) <= confidence:

					p1, p2 = (int(xmin), int(ymin)), (int(xmax), int(ymax))
					cv2.rectangle(image, p1, p2, color, thickness=2, lineType=cv2.LINE_AA)
					if name:
						namer = rename_labels.get(name)
						if namer is None:
							name = name
						else:
							name = namer			
						tf = max(2 - 1, 1)  # font thickness
						w, h = cv2.getTextSize(name, 0, fontScale=2 / 3, thickness=tf)[0]  # text width, height
						outside = p1[1] - h - 3 >= 0  # label fits outside box
						p2 = p1[0] + w, p1[1] - h - 3 if outside else p1[1] + h + 3
						cv2.rectangle(image, p1, p2, color, -1, cv2.LINE_AA)  # filled
						coordinates.append({name:[int(xmin),int(ymin),int(xmax),int(ymax)]})
						if label_captitalize:
							name = name.capitalize()
							cv2.putText(image, name, (p1[0], p1[1] - 2 if outside else p1[1] + h + 2), 0, 2 / 3, (255,255,255),
									thickness=tf, lineType=cv2.LINE_AA)
						else:						
							cv2.putText(image, name, (p1[0], p1[1] - 2 if outside else p1[1] + h + 2), 0, 2 / 3, (255,255,255),
									thickness=tf, lineType=cv2.LINE_AA)
							

						labels_.append(name)
			except:
				pass
		else:
			p1, p2 = (int(xmin), int(ymin)), (int(xmax), int(ymax))
			cv2.rectangle(image, p1, p2, color, thickness=2, lineType=cv2.LINE_AA)
			if name:			
				namer = rename_labels.get(name)
				if namer is None:
					name = name
				else:
					name = namer
				
				tf = max(2 - 1, 1)  # font thickness
				w, h = cv2.getTextSize(name, 0, fontScale=2 / 3, thickness=tf)[0]  # text width, height
				outside = p1[1] - h - 3 >= 0  # label fits outside box
				p2 = p1[0] + w, p1[1] - h - 3 if outside else p1[1] + h + 3
				cv2.rectangle(image, p1, p2, color, -1, cv2.LINE_AA)  # filled
				coordinates.append({name:[int(xmin),int(ymin),int(xmax),int(ymax)]})

				if label_captitalize:
					name = name.capitalize()
					cv2.putText(image, name, (p1[0], p1[1] - 2 if outside else p1[1] + h + 2), 0, 2 / 3, (255,255,255),
							thickness=tf, lineType=cv2.LINE_AA)
				else:						
					cv2.putText(image, name, (p1[0], p1[1] - 2 if outside else p1[1] + h + 2), 0, 2 / 3, (255,255,255),
							thickness=tf, lineType=cv2.LINE_AA)
				labels_.append(name)


	for img in results.imgs:
		return img, labels_, coordinates

# cv2.imshow('predected_image',predicted_image)
# cv2.waitKey(0)

cap = cv2.VideoCapture(0)
while True:
	ret, frame = cap.read()
	predicted_image, detcetor_labels, coordinates = run_inference_hub(frame)
	print(detcetor_labels,coordinates)
	input('enterrrrrrrrrr')
	# cv2.imshow('frame',predicted_image)

	if cv2.waitKey(1) and 0xFF == ord('q'):
		break



