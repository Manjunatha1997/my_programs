
from common_utils import *
import cv2
from inference import *
from ai_settings import *
import bson
import requests



def custom_bnd_box_plot(image,class_name:str,xmin:int,ymin:int,xmax:int,ymax:int,color:tuple):

    cv2.rectangle(image, (xmin, ymin), (xmin - (xmin-xmax), ymin - (ymin-ymax)), color, 1)

    # cv2.rectangle(image, (xmin, ymin), (xmin - (xmin-xmax), ymin + 40), color, 1)

    cv2.line(image, (xmin,ymin), (int(xmin+20),int(ymin)), color,3)
    cv2.line(image, (xmin,ymin), (int(xmin),int(ymin+20)), color,3)


    cv2.line(image, (xmax,ymax), (int(xmax-20),int(ymax)), color,3)
    cv2.line(image, (xmax,ymax), (int(xmax),int(ymax-20)), color,3)

    cv2.line(image, (xmin,ymax), (int(xmin+20),int(ymax)), color,3)
    cv2.line(image, (xmin,ymax), (int(xmin),int(ymax-20)), color,3)

    cv2.line(image, (xmax,ymin), (int(xmax-20),int(ymin)), color,3)
    cv2.line(image, (xmax,ymin), (int(xmax),int(ymin+20)), color,3)


    ## put text
    font = cv2.FONT_HERSHEY_SIMPLEX 
    org = (xmin,ymin) 
    fontScale = 1
    thickness = 2
    image = cv2.putText(image, class_name, org, font,  
                    fontScale, color, thickness, cv2.LINE_AA) 


    return image



cap  = cv2.VideoCapture(0)

ret, frame = cap.read()


predictor = Predictor()
predictor.model_dir = './'
predictor.weights_path = 'yolov5n.pt'
predictor_model = predictor.load_model()

while True:

    ret, frame = cap.read()
    frame_copy = frame.copy()

    predicted_frame, detector_predictions,coordinates  = predictor.run_inference_hub(predictor_model,frame)
    cv2.imshow("frame",predicted_frame)

    for i in coordinates:
        for k,v in i.items():
            print(k,v)
            class_name = k
            xmin = v[0]
            ymin = v[1]
            xmax = v[2]
            ymax = v[3]

        

            custom_frame = custom_bnd_box_plot(frame_copy,class_name,xmin,ymin,xmax,ymax,(0,255,0))
            cv2.imshow("custom_frame",custom_frame)
            cv2.waitKey(1)

        


 