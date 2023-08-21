from grpc import Status
import pymongo
from regex import B
client = pymongo.MongoClient('mongodb://127.0.0.1:27017')

db = client['BHATTAM']

col = db['inspection']

inspectionid_collection = col
objs = [i for i in inspectionid_collection.find().sort([( '$natural', -1)])]

# print(objs)

left_frame_status = 'Accepted'
right_frame_status = 'Accepted'

p = []


for ins in objs:
    ins_id = str(ins['_id'])
    # print(ins_id)

    log_col = db[ins_id+'_log']

    print(log_col)

    if left_frame_status and right_frame_status:
        log_col_data = [i for i in log_col.find({'left_frame_status':left_frame_status,'right_frame_status':right_frame_status})]
    
    elif left_frame_status or right_frame_status:
        if left_frame_status:
            Status = left_frame_status
        if right_frame_status:
            status = right_frame_status
        log_col_data = [i for i in log_col.find({'left_frame_status':status,'right_frame_status':status})]

        

    p.extend(log_col_data)


print(len(p))


    




    


