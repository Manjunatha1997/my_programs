import glob
import cv2

path = r'C:\Users\Manju\Desktop\aaa\\'

res = glob.glob(path+'*.jpg')

for file in res:
	print(file)
	img = cv2.imread(file)
	img = cv2.resize(img,(640,480))
	cv2.imwrite(path+file.split('\\')[-1],img)


