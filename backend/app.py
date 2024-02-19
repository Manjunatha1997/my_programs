
from flask import Flask, render_template, Response, request, jsonify
import cv2
from common_utils import CacheHelper, MongoHelper
from datetime import datetime
import pymongo

app = Flask(__name__)


@app.route('/main/', methods=['GET','POST'])
def main():
    return render_template("main.html")


@app.route('/main/inspect/',methods=['POST'])
def inspect():
    CacheHelper().set_json({'inspect':True})
    resp = {"inspect":True}
    return resp, 200


@app.route('/main/save_results/',methods=['POST'])
def save_results():
    if request.method == "POST":


        payload = request.json

        input_frame_list = payload.get('input_frame_list',None)
        predicted_frame_list = payload.get('predicted_frame_list',None)
        status = payload.get('status',None)
        defect_list = payload.get('defect_list',None)


        time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        data = {
            "input_frame_list":input_frame_list,
            "predicted_frame_list":predicted_frame_list,
            "status":status,
            "defect_list":defect_list,
            "time_stamp":time_stamp

        }

        print(data,":: data ")
        mp = MongoHelper().getCollection("inspection_log")
        mp.insert_one(data)
        
    return payload, 200

@app.route('/main/')
@app.route('/main/get_metrics/')
def get_metrics():
    def eventStream():
        while True:
            mp = MongoHelper().getCollection('inspection_log')

            mp_data =  mp.find()
            total_accepted = 0
            total_rejected = 0

            for i in mp_data:
                status = i.get('status',None)
                if status == "Accepted":
                    total_accepted += 1
                elif status == "Rejected":
                    total_rejected += 1
                
            
            latest_doc = mp.find_one(sort=[("_id", pymongo.DESCENDING)])  
            latest_doc['total_inspections'] = total_accepted + total_rejected
            latest_doc['total_accepted'] = total_accepted
            latest_doc['total_rejected'] = total_rejected
            del latest_doc['_id']



            # print(latest_doc,"latest doc")      
            # wait for source data to be available, then push it
            json_data = jsonify(latest_doc)
            # yield 'data: {}\n\n'.format(latest_doc)
            yield latest_doc
   

    return Response(eventStream(), mimetype='application/json')


@app.route('/reports/', methods=['GET','POST'])
def reports():
    return render_template("reports.html")








@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')




def gen_frames():  
    
    while True:
        predicted_frame = CacheHelper().get_json("predicted_frame")
    
        ret, buffer = cv2.imencode('.jpg', predicted_frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result




if __name__ == "__main__":
    app.run()
