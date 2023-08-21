import cv2
import os
import numpy as np
# Input path, and Path must be ends with '/'
inp_path = '/home/manju/Desktop/od/'

# Creating output folder path
# Path must be ends with '/'
out_path = '/home/manju/Desktop/out/'

# Create a folder is not exists
if not os.path.isdir(out_path):
    os.mkdir(out_path)

# Reading all files with os module
files = os.listdir(inp_path)

temp = []
for file in files:
    if file.endswith('.jpg'):
        # Reading all images in the given folder
        img = cv2.imread(inp_path+file,0)

        # Applying adaptive thresholding
        thr = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
        x = cv2.resize(thr,(50,50))
        temp.append(x)
        # Write/Save it into a output folder
        cv2.imwrite(out_path+file,thr)
    else:
        print('skipping file is :',file)




# if len(temp) > 50:
#     numpy_horizontal = np.hstack(temp[:50])

#     numpy_horizontal_concat = np.concatenate(temp[:50], axis=1)

#     cv2.imshow('Numpy Horizontal Concat', numpy_horizontal_concat)
#     cv2.waitKey()
#     cv2.destroyAllWindows()

# else:
numpy_horizontal = np.hstack(temp)

numpy_horizontal_concat = np.concatenate(temp, axis=1)

cv2.imshow('Numpy Horizontal Concat', numpy_horizontal_concat)
cv2.waitKey()
cv2.destroyAllWindows()

    