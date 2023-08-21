import pandas as pd
import shutil
import os

def copy_file(source_file, dest_file):
    if not os.path.isdir(dest_file):
        os.makedirs(dest_file)
    shutil.copyfile(source_file, dest_file)






data=pd.read_csv('D:\\indo_reports\\Daywise\\feb_all\\2022-03-15 113908.618674.csv')
inference_images = data['inference_images']



for inf_images in inference_images:
    x = inf_images.split(',')

    for i in x:
        image = i[2:-1]
        if image.endswith("'"):
            image = image[:-1]
        image = image.replace('http://127.0.0.1:3306','/home/mim/Main/dataimages')
        copy_file(image,'/home/mim/Main/dataimages/extract')
        print(image)


