import sys
import os
sys.path.insert(0,os.getcwd())

from common_utils import *
import cv2
from inference import *
import bson
import requests




predictor = Predictor()
predictor.model_dir = './'
predictor.weights_path = "yolov5n.pt"
predictor.defects = []
predictor.features = []
predictor.features_count = []

predictor_model = predictor.load_model()


def check_kanban(detector_predictions,defects,features,features_count):
    defect_list = []
    feature_list = []
    feature_dict = {}
    for defect in defects:
        if defect in detector_predictions:
            defect_list.append(defect)

    for feature in features:
        if not feature in detector_predictions:
            feature_list.append(feature)
    
    if defect_list or feature_list:
        status = "Rejected"
    else:
        status = "Accepted"

    return status, defect_list,feature_list,feature_dict



redis_obj = CacheHelper()

while True:
    inspect = redis_obj.get_json("inspect")
    input_frame = redis_obj.get_json("input_frame")
    input_frame_copy = input_frame.copy()
    
    predicted_frame, detections, coordinates = predictor.run_inference_hub(predictor_model,input_frame)

    redis_obj.set_json({"predicted_frame":predicted_frame})

    if inspect == True:

        defects = predictor.defects
        features = predictor.features
        features_count = predictor.features_count
        status, defect_list,feature_list,feature_dict = check_kanban(detections, defects,features,features_count)

        object_id = str(bson.ObjectId())
        print(os.path.join(datadrive_path,object_id+'_if.jpg'))
        
        cv2.imwrite(os.path.join(datadrive_path,object_id+'_if.jpg'),input_frame_copy)
        cv2.imwrite(os.path.join(datadrive_path,object_id+'_pf.jpg'),predicted_frame)
        input_frame_url = "http://"+my_ip_address+":3306/"+object_id+"_if.jpg"
        predicted_frame_url = "http://"+my_ip_address+":3306/"+object_id+"_pf.jpg"


        data = {'input_frame_list':[input_frame_url],'predicted_frame_list':[predicted_frame_url],'status':status,'defect_list':defects,'feature_list':features,'features':feature_list,'defects':defect_list,'feature_dict':feature_dict}
        print(data,":: data")
        url=  "http://localhost:5000/main/save_results/"
        resp = requests.post(url=url,json=data)
        print(resp,"resp")
        redis_obj.set_json({"inspect":False})




