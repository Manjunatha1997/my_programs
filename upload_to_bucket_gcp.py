


from abc import ABC, abstractmethod
from google.cloud import storage
import os
import bson
import cv2


def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

class DataMover(ABC):  ## can be used for moving data

    def __init__(self):
        self.client = None


    

@singleton
class GCPHelper():
    def __init__(self):
        # super().__init__()
        # if not self.client:
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'first-campaign-346416-e263efdbed96.json'
        self.client = storage.Client()
        self.bucket_name = ""

    def set_bucket_name(self, name):
        self.bucket_name = name
        return self.bucket_name

    def list_blobs(self):
        bucket_con = []
        """Lists all the blobs in the bucket."""
        # Note: Client.list_blobs requires at least package version 1.17.0.
        blobs = self.client.list_blobs(self.bucket_name)
        for blob in blobs:
            # print(blob.name)
            bucket_con.append(blob.name)
        return bucket_con

    def upload_to_bucket(self, blob_name, file_path):
        '''
        Upload file to a bucket
        : blob_name  (str) - object name
        : file_path (str)
        : bucket_name (str)
        '''
        print(file_path,"file path")

        unique_image_name = str(bson.ObjectId()) + '.jpg'
        # print(blob_name,"blob name")
        bucket = self.client.get_bucket(self.bucket_name)
        blob = bucket.blob(f"{blob_name}/{unique_image_name}")
        _, encoded_img = cv2.imencode(".jpg", file_path)

        blob.upload_from_string(encoded_img.tobytes(), content_type="image/jpeg")
        img_url = f"https://storage.googleapis.com/{bucket}/{blob_name}/{unique_image_name}"
        return img_url



img = cv2.imread('D:\my_programs\vertical.jpg')
print(img)
# gcp_mover  = GCPHelper() 
# bucket_name = gcp_mover.set_bucket_name('test_28001')

# url =gcp_mover.upload_to_bucket('mobile_apps_datadrive',img)
# print(url)





