import torch
import os
import glob
import cv2
import numpy as np


class Predictor():
	def __init__(self):
		self.model_dir = 'D:\\yolov5_auto'
		self.weights_path = 'yolov5s.pt'
		self.common_confidence = 0.1
		self.common_iou = 0.45
		self.defects = [] #['bus','chair','tv','bottle','person']
		self.ind_thresh = {} #{'bus':0.1,'person':0.1,'chair':0.1}
		self.label_captitalize = False
		self.rename_labels = {} # {'person':'manju'}
		self.avoid_labels_cords = [{'xmin':0,'ymin':135,'xmax':300,'ymax':480}]



	def load_model(self):
		model = torch.hub.load(self.model_dir,'custom',path=self.weights_path,source = 'local')
		model.conf = self.common_confidence
		model.iou = self.common_iou
		return model


	def run_inference_hub(self,model, image):

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
	
			
			skip = None
			if self.avoid_labels_cords:
				for crd in self.avoid_labels_cords:
					if round(xmin) >= crd['xmin'] and round(ymin) >= crd['ymin'] and round(xmax) <= crd['xmax'] and round(ymax) <= crd['ymax']:
						print(round(xmin),round(ymin),round(xmax),round(ymax))
						skip = True
			if skip :
				continue


			# input()

			## bounding box and text 

			if name in self.defects:
				color = (0,0,255) # Red color bounding box 
			else:
				color = (0,128,0) # Green color bounding box 

			if name in self.ind_thresh:
				try:
					if self.ind_thresh.get(name) <= confidence:

						p1, p2 = (int(xmin), int(ymin)), (int(xmax), int(ymax))
						cv2.rectangle(image, p1, p2, color, thickness=2, lineType=cv2.LINE_AA)
						if name:
							namer = self.rename_labels.get(name)
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
							if self.label_captitalize:
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
					namer = self.rename_labels.get(name)
					if namer is None:
						name = name
					else:
						name = namer
					
					tf = max(2 - 1, 1)  # font thickness
					# tf = self.line_thickness
					w, h = cv2.getTextSize(name, 0, fontScale=2 / 3, thickness=tf)[0]  # text width, height
					outside = p1[1] - h - 3 >= 0  # label fits outside box
					p2 = p1[0] + w, p1[1] - h - 3 if outside else p1[1] + h + 3
					cv2.rectangle(image, p1, p2, color, -1, cv2.LINE_AA)  # filled
					coordinates.append({name:[int(xmin),int(ymin),int(xmax),int(ymax)]})

					if self.label_captitalize:
						name = name.capitalize()
						cv2.putText(image, name, (p1[0], p1[1] - 2 if outside else p1[1] + h + 2), 0, 2 / 3, (255,255,255),
								thickness=tf, lineType=cv2.LINE_AA)
					else:						
						
						cv2.putText(image, name, (p1[0], p1[1] - 2 if outside else p1[1] + h + 2), 0, 2 / 3, (255,255,255),
								thickness=tf, lineType=cv2.LINE_AA)
					labels_.append(name)


		for img in results.imgs:
			return img, labels_, coordinates


cap = cv2.VideoCapture(0)
predictor = Predictor()
model = predictor.load_model()

while True:
	ret, frame = cap.read()
	frame_c = frame.copy()
	# frame = cv2.imread('test_image.jpg')
	predicted_image, detcetor_labels, coordinates = predictor.run_inference_hub(model,frame)
	# print(detcetor_labels,coordinates)
	cv2.imshow('frame',predicted_image)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		cv2.imwrite('test_image.jpg',frame_c)
		break
