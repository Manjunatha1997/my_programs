from pymongo import MongoClient
import cv2
import numpy as np
import glob
import io
from PIL import Image

client = MongoClient('mongodb://127.0.0.1:27017')

db = client['files']
collection = db['images']


res = collection.find()
print(res)

for i in res:
	print('image_count:',i['image_count'],'_id:',i['_id'])


# for i in res:
#     # print(i['_id'],i['image_count'])
    
#     img1_bytes = i['image_id']
    
#     # Decoding CV2
#     decoded = cv2.imdecode(np.frombuffer(img1_bytes, np.uint8), 1)
#     # print(decoded)
#     cv2.imshow(str(i['image_count']),decoded)
    
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()




    
    