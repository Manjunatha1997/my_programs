
from common_utils import MongoHelper
import pandas as pd
import csv
from custom_utils import *
import bson




mpd = MongoHelper().getCollection('domains')
domains = mpd.find_one()
domains_list = domains.get('domains')


print(domains_list)


resp_data = {
    "domain":"",
    "total_images":0,
    "total_annotatated_images":0,
    "total_un_annotated_images":0
}



# domains = []
# total_annotated_images = []
# total_un_annotated_images = []
# total_images = []
# total_bnd_box = []
# part_ids = []
# part_names = []


file_names = []
# domains_list = ['demo4']
for domain in domains_list:

    domains = []
    total_annotated_images = []
    total_un_annotated_images = []
    total_images = []
    total_bnd_box = []
    part_ids = []
    part_names = []




    print("domain >>>>>>>>>> ",domain)
    mpp = MongoHelper().getCollection(domain+'parts')
    mpp_data = [i for i in mpp.find({'isdeleted':False})]

    for i in mpp_data:

        total_imgs = 0
        total_ann_images = 0
        total_un_ann_images = 0
        total_bnd = 0
        part_id = str(i['_id'])

        part_name = i['part_number']

        mp_dataset  = MongoHelper().getCollection(f"{domain}{part_id}_dataset")
        mp_dataset_data = mp_dataset.find()

        for ann in mp_dataset_data:
            state = ann.get('state')
            annotation_detection = ann.get('annotation_detection')
            if state == 'tagged':
                total_ann_images += 1
                total_bnd += len(annotation_detection)
            else:
                total_un_ann_images += 1
                total_bnd += len(annotation_detection)
            total_imgs +=1 

        domains.append(domain)
        total_images.append(total_imgs)
        total_annotated_images.append(total_ann_images)
        total_un_annotated_images.append(total_un_ann_images)
        total_bnd_box.append(total_bnd)
        part_ids.append(part_id)
        part_names.append(part_name)

        data = {
                "Total Images": total_imgs,
                "Total Annotated Images" : total_ann_images,
                "Total UnAnnotated Images":total_un_ann_images,
                "Total Bounding Box":total_bnd,
                "Domain":domain,
                "Part ID":part_id,
                "Part Name":part_name
                }
        
        

        mp = MongoHelper().getCollection(domain+'all_annotation_details')
        mp_data = mp.find_one({'Part ID':part_id})
        if mp_data:
            mp.update_one({mp_data['Part ID']:part_id},{"$set":data})
        else:
            mp.insert_one(data)
    
    

    # print(f"total_annotated_images : {total_annotated_images}\n total_un_annotated_images {total_un_annotated_images} \n  total_bnd_box {total_bnd_box}\n  total_images {total_images} ")

    data_frame = {
            "Total Images": total_images,
            "Total Annotated Images" : total_annotated_images,
            "Total UnAnnotated Images":total_un_annotated_images,
            "Total Bounding Box":total_bnd_box,
            "Domain":domains,
            "Part ID":part_ids,
            "Part Name":part_names
            }
    ## if the images found , then craete a csv file else No.
    if data_frame["Total Images"]:
        df = pd.DataFrame(data_frame)
        df.to_csv(f"{domain}_anotation_details.csv")
        file_names.append(f"{domain}_anotation_details.csv")



sender = "manjunatha.reddy@lincode.ai" 
receiver ="divyasai.lakshmi@lincode.ai" # "shyam.gupta@lincode.ai"
filename = file_names
password =  "cokywtbgeezhqjwz" # "cokywtbgeezhqjwz" # "wedpyxysjvsvyjbe" # personal -  mr
message = send_mail_attcach(sender,password,receiver,filename)
# message = send_mail(sender,password,receiver,filename[0])

print(message)

from datetime import datetime
fw = open("logs.txt","w")
fw.write(str(datetime.now()))
fw.close()


