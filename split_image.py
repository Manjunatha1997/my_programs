from ctypes import c_void_p
import glob
from importlib.resources import path
import image_slicer # $ pip install image_slicer
import imageio # pip install imageio
import matplotlib.pyplot as plt # for image visualization
# %matplotlib inline

# Slice your image
# syantax = image_slicer.slice('file',number of slice)
path = 'C:\\Users\\Manju\\Downloads\\bottom_no_solder\\crops_need\\*.png'
res = glob.glob(path)

counter = 1

# for file in res:
#     print(file)

file = r"C:\Users\Manju\Documents\pcba_testing\empty\bottom_one_1 (1).png"

img_4 = image_slicer.slice(file,6)


l = []
for i in img_4:
    pic = imageio.imread('{}'.format(i.filename)) # read the image
    plt.figure(figsize = (5,5)) # define the size of image you want see
    plt.imshow(pic) # to see the image
    print('Slice Number: {}'.format(i.number))
    print('Type of the image : ' , type(pic))
    print('Shape of the image : {}'.format(pic.shape))
    print('Image Hight {}'.format(pic.shape[0]))
    print('Image Width {}'.format(pic.shape[1]))
    print('Dimension of Image {}'.format(pic.ndim))
    print('Image size {}'.format(pic.size))
    print('Maximum RGB value in this image {}'.format(pic.max()))
    print('Minimum RGB value in this image {}'.format(pic.min()))
    print('Mean RGB value in this image {}'.format(pic.mean())) 
    print('\n\n\n\n')
    l.append(pic)

