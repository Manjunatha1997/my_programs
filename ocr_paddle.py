


import glob
import os
import cv2
from super_resolution import *

from paddleocr import PaddleOCR,draw_ocr
ocr = PaddleOCR(use_angle_cls=True, lang='en',use_gpu=False) # need to run only once to download and load model into memory



def get_ocr_data(frame):
    #result = ocr.ocr(frame, cls=True)
    try:
        result = ocr.ocr(frame,cls=True)
        result = result[0]
        boxes = [line[0] for line in result]
        txts = [line[1][0] for line in result]
        scores = [line[1][1] for line in result]
        ocr_image = draw_ocr(frame, boxes, txts,font_path='/home/manju/Documents/mobile_apps/livis_ocr/livis-be/flaskk/simfang.ttf')
 
        print("txts in try ", txts)

        return txts, ocr_image

    except:
        return [],frame


def create_dir(out):
    import os
    if not os.path.isdir(out):
        os.makedirs(out)


path = "/home/manju/Documents/seneca/dataset/pole/srgan_test_output/"
out = "/home/manju/Documents/seneca/dataset/pole/srgan_test_output/ocr_out/"
create_dir(out)
images  = glob.glob(os.path.join(path,"*"))


# pattern = r'^\d{2,3}A$'
# import re

# def validate_input(input_str):
#     if re.match(pattern, input_str):
#         return True
#     return False


for image in images:
    try:
        imge = cv2.imread(image)
        # img = super_resolution_img(imge)

        
        # img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
        dets, inf_img = get_ocr_data(imge)
        # input("enter !!!!")



        # for test_str in dets:
        #     if validate_input(test_str):
        #         print(f"'{test_str}' matches the conditions.///////////////////////////////////")
        #     else:
        #         print(f"'{test_str}' does not match the conditions.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")


        out_image_path = os.path.join(out,os.path.basename(image))
        print(out_image_path," out_image_pathout_image_pathout_image_path \n\n ")
        
        cv2.imwrite(out_image_path,inf_img)
    except Exception as e:
        print(e,"skipping file >>",image)