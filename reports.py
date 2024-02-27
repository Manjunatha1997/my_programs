import pdfkit
import base64
from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import UndefinedError
import pandas as pd
import ast
import requests
import bson
import os


environment = Environment(loader=FileSystemLoader("static/templates/"))
template = environment.get_template("reports.html")


empty_data = {
    "part_name": "-",
    "inspected_at": "-",
    "status": "-",
    "region": "-",
    "images": "-"
}

options = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'orientation': 'Landscape'
}


def convert_img_2b64(img_path):
    with open(img_path, "rb") as img_file:
        img_b64 = base64.b64encode(img_file.read()).decode()
    return f"data:image/jpeg;base64,{img_b64}"

def url_to_base64(image_url):
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            base64_string = base64.b64encode(response.content).decode('utf-8')
            return base64_string
        else:
            print("Failed to fetch the image. Status code:", response.status_code)
            return None
    except Exception as e:
        print("An error occurred:", str(e))
        return None


def dataframe_to_pdf_data(data):
    resp_out = {}
    json_data = data.to_dict()
    for i, j in json_data.items():
        if i == "reason":
            for key, value in j.items():
                j[key] = ast.literal_eval(value)

        if i == "inference_images":
            for key, value in j.items():
                # j[key] = ast.literal_eval(value)

                vals = ast.literal_eval(value)
                base_64_images = []
                for i in vals:
                    # base_image = url_to_base64(i)
                    base_image = convert_img_2b64(i.replace('http://localhost:3306','datadrive'))
                    base_64_images.append(base_image)

                j[key] = base_64_images

            
        resp_out[i] = j
 
    return json_data,len(data)




# <!-- {% for image in {{data.inference_images[i] }} %}

#                 <tr>
#                     <td colspan="4">
#                         <img src="{{ image }}" alt=" Inference Images" height="500" width="500"> </img>
#                     </td>

#                 </tr>
#             {% endfor %}      -->






def download_report(data_frame):
    try:
        
        resp, length = dataframe_to_pdf_data(data_frame)
        a = resp['inference_images'][0][0]
        print(a)



        x = template.render(
            data=resp,
            length=length,
        )
        # part_name = part_name.replace('/','_')
        # file_name = f"saved_images/{part_name}_{test_hour}_{test_case}_{serial_number}_individual_report.pdf"
        file_name = os.path.join('datadrive','reports.pdf')

        print(file_name,"file name")


        for i in range(length):
            print(data['part_name'][i])


        path_wkthmltopdf = b"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        pdfkit.from_string(x, file_name, options=options,configuration=config)
        return file_name
    except:# UndefinedError:
        print("I am in exception individual reports :: ")
        file_name = "datadrive/reports.pdf"
        path_wkthmltopdf = b"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        pdfkit.from_string("", file_name, options=options,configuration=config)
        return file_name

data = pd.read_csv("reports/2024-02-25.csv")

# x = download_report(data)
# print(x)


