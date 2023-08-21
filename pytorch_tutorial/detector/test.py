from inference import *
from datetime import datetime
import requests
import bson
from common_utils import CacheHelper
predictor = Predictor()
model = predictor.load_model()


cap = cv2.VideoCapture(0)
while True:
	ret, frame = cap.read()
	## frame 1 ##
	input_frame = frame.copy()
	t1 = datetime.now()
	predictor.defects = ['person']
	predictor.features = []
	predicted_image, detector_labels, coordinates = predictor.run_inference_hub(model,frame)
	t2 = datetime.now()
	print(f"Total inference time is !!!!! {(t2-t1).total_seconds()} seconds ")
	response = predictor.check_kanban()

	CacheHelper().set_json({'input_frame':input_frame})
	CacheHelper().set_json({'inference_frame':predicted_image})
	
	# print(response)
	data = {'inspection_id':'1','camera_view':'1','camera_index':'1','part_name':'part_name','input_frame':'input_frame','inference_frame':'inference_frame','features':response.get('features'),'defects':response.get('defects'),'defect_list':predictor.defects,'feature_list':predictor.features,'status':response.get('status')}
	requests.post(url='http://localhost:8000/livis/operators/save_results_per_view/',json=data)

	# inspection_status = requests.post(url='http://localhost:8000/livis/operators/save_results/',json={'inspection_id':'1'})
	# print(inspection_status)


	## frame 2 ##
	input_frame = frame.copy()
	frame2 = input_frame
	frame2 = cv2.flip(frame2,1)
	input_frame2 = frame2.copy()

	t1 = datetime.now()
	predictor.defects = []
	predictor.features = ['cell phone']
	predicted_image, detector_labels, coordinates = predictor.run_inference_hub(model,frame2)

	t2 = datetime.now()
	print(f"Total inference time is !!!!! {(t2-t1).total_seconds()} seconds ")
	response = predictor.check_kanban()

	CacheHelper().set_json({'input_frame':input_frame})
	CacheHelper().set_json({'inference_frame':predicted_image})
	
	# print(response)
	data = {'inspection_id':'1','camera_view':'2','camera_index':'2','part_name':'part_name','input_frame':'input_frame','inference_frame':'inference_frame','features':response.get('features'),'defects':response.get('defects'),'defect_list':predictor.defects,'feature_list':predictor.features,'status':response.get('status')}
	requests.post(url='http://localhost:8000/livis/operators/save_results_per_view/',json=data)

	r = requests.post(url='http://localhost:8000/livis/operators/save_results/',json={'inspection_id':'1'})
	r.raise_for_status()
	data = r.json()

	print(data)



	print('**********************************************************************************')
	input('Enter for next inspection')

	# cv2.imshow('frame',predicted_image)


	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


