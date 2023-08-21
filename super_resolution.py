import requests
import io
import cv2
import numpy as np




def super_resolution_img(numpy_image):
    cv2.imwrite("temp.jpg",numpy_image)

    r = requests.post(
        "https://api.deepai.org/api/torch-srgan",
        files={
            'image': open('temp.jpg', 'rb'),
        },
        headers={'api-key': '1ac365a6-36db-4f18-8ebf-133599c00c9a'}
    )
    print(r.json())
    image_url = r.json()["output_url"]

    response = requests.get(image_url)
    bytes_im = io.BytesIO(response.content)
    #img = cv2.cvtColor(np.array(Image.open(bytes_im)), cv2.COLOR_RGB2BGR)
    nparr = np.asarray(bytearray(bytes_im.read()), dtype=np.uint8)   #np.frombuffer(bytes_im, np.uint8)
    img = cv2.imdecode(nparr, cv2.COLOR_RGB2BGR)
    return img


# image = cv2.imread("shapes.jpg") 
# super_res_image = super_resolution_img(image)
# cv2.imwrite("shapes_super.jpg",super_res_image)






