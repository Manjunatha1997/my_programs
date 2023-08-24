
from pymongo import MongoClient
import dataframe_image as dfi
import pandas as pd
import os



MONGO_DB = "LIVIS_sept_03"


def singleton(cls):
    """
    This is a decorator which helps to create only 
    one instance of an object in the particular process.
    This helps the preserve the memory and prevent unwanted 
    creation of objects.
    """
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton
class MongoHelper:
    try:
        client = None
        def __init__(self):
            if not self.client:
                # self.client = MongoClient(host=MONGO_SERVER_HOST, port=MONGO_SERVER_PORT)
                self.client = MongoClient(host="127.0.0.1", port=27017)

            self.db = self.client[MONGO_DB]

        def getDatabase(self):
            return self.db

        def getCollection(self, cname, create=False, codec_options=None):
            _DB = MONGO_DB
            DB = self.client[_DB]
           
            return DB[cname]
    except:
        pass            


def create_dir(path):
    if not os.path.isdir(path):
        os.makedirs(path)

mp_inspection = MongoHelper().getCollection("inspection")

year_check = "2023"
month_check = "05"
path = "/home/manju/Documents/seneca/reports_csv"




lt = []
rt = []


for inspection_data in mp_inspection.find():
    start_time = inspection_data["start_time"]
    month = start_time.split(" ")[0].split('-')[1]
    year = start_time.split(" ")[0].split('-')[0]
    if year == year_check and month == month_check:
        id = str(inspection_data["_id"])
        
        mp_r = MongoHelper().getCollection(id+'_result')
        mp_r_data = mp_r.find_one()



        try:
            drawing_details_left_table = mp_r_data["drawing_details"][0]["left_table"]
            breaker_details_left_table = mp_r_data["breaker_details"][0]["left_table"]

            drawing_details_right_table = mp_r_data["drawing_details"][0]["right_table"]
            breaker_details_right_table = mp_r_data["breaker_details"][0]["right_table"]

            
            

            drawing_details_df_left_table = pd.DataFrame(drawing_details_left_table)
            drawing_details_df_right_table = pd.DataFrame(drawing_details_right_table)

            lt.append(drawing_details_df_left_table)
            rt.append(drawing_details_df_right_table)





            breaker_details_df_left_table = pd.DataFrame(breaker_details_left_table)
            breaker_details_df_right_table = pd.DataFrame(breaker_details_right_table)



            out_csv_path = os.path.join(path,id,'csv')
            out_image_path = os.path.join(path,id,'image')

            create_dir(out_csv_path)
            create_dir(out_image_path)



            drawing_details_df_left_table.to_csv(f"{out_csv_path}/{id}_drawing_details_df_left_table.csv")
            drawing_details_df_right_table.to_csv(f"{out_csv_path}/{id}_drawing_details_df_right_table.csv")
            breaker_details_df_left_table.to_csv(f"{out_csv_path}/{id}_breaker_details_df_left_table.csv")
            breaker_details_df_right_table.to_csv(f"{out_csv_path}/{id}_breaker_details_df_right_table.csv")


            dfi.export(drawing_details_df_left_table, f"{out_image_path}/{id}_drawing_details_df_left_table.png")
            dfi.export(drawing_details_df_right_table, f"{out_image_path}/{id}_drawing_details_df_right_table.png")
            dfi.export(breaker_details_df_left_table, f"{out_image_path}/{id}_breaker_details_df_left_table.png")
            dfi.export(breaker_details_df_right_table, f"{out_image_path}/{id}_breaker_details_df_right_table.png")




        except Exception as e:
            print(e)



res_l = pd.concat(
    lt,
    axis=0,
    join="outer",
    ignore_index=False,
    keys=None,
    levels=None,
    names=None,
    verify_integrity=False,
    copy=True,
)


res_r = pd.concat(
    lt,
    axis=0,
    join="outer",
    ignore_index=False,
    keys=None,
    levels=None,
    names=None,
    verify_integrity=False,
    copy=True,
)
res_l.to_csv("/home/manju/Documents/seneca/reports/2023-05-drawing_left_table.csv")
res_r.to_csv("/home/manju/Documents/seneca/reports/2023-05-drawing_left_table.csv")











