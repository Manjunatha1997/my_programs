import os
from pydoc import isdata
import sys
import cv2
import glob
import json
import numpy as np 
import os.path as osp
from PIL import Image

## Reading annotation files and creating masks
images = r"D:\Anomaly-Detection-Localization-master\Anomaly-Detection-Localization-master\mvtec\metal\ground_truth\burr\\"
labels = r"D:\Anomaly-Detection-Localization-master\Anomaly-Detection-Localization-master\mvtec\metal\ground_truth\burr\\"

width, height = 640, 480
defects = ['burr']

out_dir = r'D:\Anomaly-Detection-Localization-master\Anomaly-Detection-Localization-master\mvtec\metal\ground_truth\burr_out_dir\\'

if not os.path.isdir(out_dir):
    os.makedirs(out_dir)
palette = [[0, 0, 0],[255,255,255]]


list_with_single_polys = []
x_train = []
y_train = []

#def read_images(images):
filename = [img for img in glob.glob(images + '*.jpg')]
for img in filename:
    print(filename)
    rgb_img = cv2.imread(img)
    rgb_crop = rgb_img
    x_train.append(rgb_crop)

# y_train = np.zeros((len(x_train),1200,1600,1))
y_train = np.zeros((len(x_train),height,width,1))

for i,file in enumerate(filename):
    mask1 = np.zeros(rgb_img.shape[:2], dtype = np.uint8)
    file = file.replace('.jpg','.json')
    with open(file) as f:
        json_data = json.load(f)
        for val in json_data['shapes']:
            list_with_single_polys = val['points']
            roi = list_with_single_polys
            pts = np.array(roi, dtype = np.int32)
            pts = pts.reshape((-1, 1, 2))
            mask1 = np.dstack((mask1,mask1))
            if val['label'] in defects:
                cv2.fillPoly(mask1, [pts], 255)
                print(type(mask1))
                jpg_mask = file.split('\\')[-1].split('.')[0]
                mask1 = np.array(mask1).astype(np.uint8)
                mask1 = Image.fromarray(mask1).convert('P')
                mask1.putpalette(np.array(palette, dtype=np.uint8))
                jpg_mask = jpg_mask+'.png'
                
                #mask1.save(osp.join(out_dir+jpg_mask,mask1))
                mask1.save(osp.join(out_dir+jpg_mask, file.replace('.json', '.png')))
                
                
                #print(jpg_mask)
                #cv2.imwrite(out_dir+jpg_mask,mask1)
                #plt.imsave(out_dir+jpg_mask,mask1,cmap='RdYlGn')

                #cv2.imwrite('mask'+file,mask1)
            # if val['label'] == 'Mastic_Sealant':
            # 	cv2.fillPoly(mask1, [pts], 255)
            # 	y_train[i,:,:,0] = mask1
    # cv2.imwrite(file)        

