

from PIL import Image
from PIL import ImageFilter
import os
  
def main():
    # path of the folder containing the raw images
    inPath ="D:\\detzo\\M5_OCR\\view1\\m5_gd_v1_frames\\"
  
    # path of the folder that will contain the modified image
    outPath ="D:\\detzo\\M5_OCR\\view1\\m5_gd_v1_frames\\"
  
    for imagePath in os.listdir(inPath):
        # imagePath contains name of the image 
        inputPath = os.path.join(inPath, imagePath)
  
        # inputPath contains the full directory name
        img = Image.open(inputPath)
  
        fullOutPath = os.path.join(outPath,imagePath)
        # fullOutPath contains the path of the output
        # image that needs to be generated
        img.rotate(180).save(fullOutPath)
  
        print(fullOutPath)
  
# Driver Function
if __name__ == '__main__':
    main()
