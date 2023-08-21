from json import load
from inference import *
from datetime import datetime
import glob
from fastai.vision.all import load_learner
import pathlib
from common_utils import CacheHelper

temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath


predictor = Predictor()
models = predictor.load_model()


res = glob.glob(r'C:\Users\Manju\Downloads\a\a\blur_label\\*.jpg')




classifier_weights = r"C:\Users\Manju\Documents\smart_ups_weights\crops_g_b_d.pkl"
classify_labels = ['good_label']

def detect_classify(pickel_file, image):
    model = load_learner(pickel_file)
    preds,_,thres = model.predict(image)
    return preds



for file in res:
    frame = cv2.imread(file)
    input_frame = frame.copy()
    t1 = datetime.now()
    
    predicted_image, detector_labels, coordinates = predictor.run_inference_hub(models,frame)
    t2 = datetime.now()
    print(f"Total inference time is !!!!! {(t2-t1).total_seconds()} seconds ")
    response = predictor.check_kanban()
    print(coordinates)

    for l in classify_labels:
        if l in detector_labels:
            try:
                for cord in coordinates:
                    for label, label_cord in cord.items():
                        if label == l:
                            xmin = label_cord[0]
                            ymin = label_cord[1]
                            xmax = label_cord[2]
                            ymax = label_cord[3]

                            crop_img = input_frame[ymin:ymax, xmin:xmax]
                            prdss = detect_classify( classifier_weights,crop_img)
                            print(file,label, prdss)


            except:
                pass

