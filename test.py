import torch
from PIL import Image
import numpy as np
from RealESRGAN import RealESRGAN
import glob
import os


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(device)
model = RealESRGAN(device, scale=4)
model.load_weights('weights/RealESRGAN_x4.pth', download=True)

path = "/home/manju/Documents/seneca/dataset/pole/srgan_test_input"


files = glob.glob(os.path.join(path,"*"))

for file in files:
    print(file)
    image = Image.open(file).convert('RGB')

    sr_image = model.predict(image)
    sr_image.save(f'/home/manju/Documents/seneca/dataset/pole/srgan_test_output/{os.path.basename(file)}.jpg')
    






