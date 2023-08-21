import pandas as pd
import os
import cv2


def extract_images_from_csv(csv_file,indir,outdir,flag):

    if not os.path.isdir(outdir):
        os.makedirs(outdir)

    df = pd.read_csv(csv_file)
    c = 1
    if flag is True:
        flagged_data= df.loc[df['flagged'] == True]
        input_images = flagged_data['input_images']
        remarks = flagged_data['remark']
        print(remarks,'remarks....')
        for k, inp_images in enumerate(input_images):
            x = inp_images.split(',')
            try:

                # remark = remarks[k]
                # print(remark,' remark...',k)
                # input()
                for i in x:
                    image = i[2:-1]
                    if image.endswith("'"):
                        image = image[:-1]
                    image = image.replace('http://127.0.0.1:3306',indir)
                    # img = cv2.imread(image)
                    # cv2.imwrite(outdir+image.split('/')[-1],img)
                    print(image,c)
                    c += 1
            except:
                continue


    else:

        input_images = df['input_images']
        c = 1
        for inp_images in input_images:
            x = inp_images.split(',')
            for i in x:
                image = i[2:-1]
                if image.endswith("'"):
                    image = image[:-1]
                # image = image.replace('http://127.0.0.1:3306',indir)
                # img = cv2.imread(image)

                # cv2.imwrite(outdir+image.split('/')[-1],img)
                print(image,c)
                c += 1

    print(f'files copied to ==> {outdir}')



csv_file = r"C:\Users\Manju\Downloads\temp.csv"
extract_images_from_csv(csv_file,indir='/home/mim/Main/dataimages',outdir='./extracted_images/',flag=True)
