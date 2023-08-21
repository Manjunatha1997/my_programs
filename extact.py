from distutils.archive_util import make_archive
from xmlrpc.client import boolean
from matplotlib.pyplot import flag
import pandas as pd
import shutil
import os
import cv2


def extract_images_from_csv(csv_file,outdir,flag):

    if not os.path.isdir(outdir):
        os.makedirs(outdir)

    df = pd.read_csv(csv_file)
    c = 1
    if flag is True:
        flagged_data= df.loc[df['flagged'] == True]
        input_images = flagged_data['input_images']
        for inp_images in input_images:
            x = inp_images.split(',')
            for i in x:
                image = i[2:-1]
                if image.endswith("'"):
                    image = image[:-1]
                image = image.replace('http://127.0.0.1:3306','/home/mim/Main/dataimages')
                img = cv2.imread(image)
                cv2.imwrite(outdir+image.split('/')[-1],img)
                print(image,c)
                c += 1


    else:

        input_images = df['input_images']
        c = 1
        for inp_images in input_images:
            x = inp_images.split(',')
            for i in x:
                image = i[2:-1]
                if image.endswith("'"):
                    image = image[:-1]
                image = image.replace('http://127.0.0.1:3306','/home/mim/Main/dataimages')
                img = cv2.imread(image)

                cv2.imwrite(outdir+image.split('/')[-1],img)
                print(image,c)
                c += 1

csv_file = r'D:\python_programs\62866672320c60a2701237ab.csv'

extract_images_from_csv(csv_file,outdir='./extracted_images/',flag=True)


