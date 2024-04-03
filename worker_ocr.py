import sys
import os
from common_utils import *
import cv2
from inference import *
import bson
import requests
from paddleocr import PaddleOCR,draw_ocr


ocr = PaddleOCR(use_angle_cls=True, lang='en') # need to run only once to download and load model into memory

def get_ocr_inference(ocr_model,image):
    try:
        result = ocr.ocr(image, cls=True)
        # draw result
        from PIL import Image
        result = result[0]
        print(f'result :: {result}')
        boxes = [line[0] for line in result]
        txts = [line[1][0] for line in result]
        scores = [line[1][1] for line in result]
        im_show = draw_ocr(image, boxes, txts, scores, font_path='simfang.ttf')
        im_show = Image.fromarray(im_show)
        return txts, im_show

    except Exception as e:
        print('in get_ocr_inference func',e)
        return [],image


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
    if input_frame is None:
        continue
    input_frame_copy = input_frame.copy()
    
    detections, predicted_frame = get_ocr_inference(ocr,input_frame)
    redis_obj.set_json({"predicted_frame":predicted_frame})

    if inspect == True:

        defects = predictor.defects
        features = predictor.features
        features_count = predictor.features_count
        status, defect_list,feature_list,feature_dict = check_kanban(detections, defects,features,features_count)

        object_id = str(bson.ObjectId())
        
        cv2.imwrite(os.path.join(datadrive_path,object_id+'_if.jpg'),input_frame_copy)
        cv2.imwrite(os.path.join(datadrive_path,object_id+'_pf.jpg'),predicted_frame)
        input_frame_url = "http://localhost:3306/"+object_id+"_if.jpg"
        predicted_frame_url = "http://localhost:3306/"+object_id+"_pf.jpg"

        worker_response = {
            "input_frames":[input_frame_url],
            "predicted_frames":[predicted_frame_url],
            "status":status,
            "defect_list":defect_list,
            "time_stamp":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        }

        print(f" \n\n  worker response :: {worker_response} \n\n ")

        redis_obj.set_json({"worker_response":worker_response})
        redis_obj.set_json({"inspect":False})
        redis_obj.set_json({"is_inspected":True})

