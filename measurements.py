import cv2
import imutils
from imutils import perspective as persp
import scipy.spatial.distance as dist
import matplotlib.pyplot as plt
import numpy as np
import os



img = cv2.imread('shapes.jpg')
image = img.copy()
rgb_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, thresh_img = cv2.threshold(gray_img,220,255,cv2.THRESH_BINARY)


# Empty black image 

black_img = np.zeros(img.shape)



# find the contours 

conts,_ = cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# def midPoint(ptA,ptB):
# 	return (int((ptA[0]+ptB[0])/2),int((ptA[1]+ptB[1])/2)

for c in conts[1:]:
	box = cv2.minAreaRect(c)
	box = cv2.boxPoints(box)
	box = np.array(box,dtype='int')

	cv2.drawContours(black_img,[c],-1,(0,10,0),2)
	cv2.drawContours(black_img,[box],-1,(255,255,255),1)

	# cv2.drawContours(img,[c],-1,(0,,0),2)
	cv2.drawContours(img,[box],-1,(0,0,255),1)

	for (x,y) in box:
		cv2.circle(black_img,(x,y),2,(0,0,255),2)
		(tl,tr,br,bl) = box


		(tlX,trX) = ((tl[0]+tr[0])/2,(tl[1]+tr[1])/2)
		(brX,blX) = ((br[0]+bl[0])/2,(br[1]+bl[1])/2)

		# Draw the mid points
		cv2.circle(black_img,(int(tlX),int(trX)),1,(255,0,0),3)
		cv2.circle(black_img,(int(brX),int(blX)),1,(255,0,0),3)
		cv2.line(black_img,(int(tlX),int(trX)),(int(brX),int(blX)),(0,0,255),1)

		# Draw the mid points
		cv2.circle(img,(int(tlX),int(trX)),1,(255,255,0),3)
		cv2.circle(img,(int(brX),int(blX)),1,(255,255,0),3)
		cv2.line(img,(int(tlX),int(trX)),(int(brX),int(blX)),(0,0,200),1)

		# claculate the distance based on the mid points.
		dA = dist.euclidean((tlX,trX),(brX,blX))
		# print the size in PX on each contour rectangle
		cv2.putText(black_img,str(dA)+' px',(int(tlX)-10,int(trX)-10),cv2.FONT_HERSHEY_SIMPLEX,0.4,(255,255,255),1)
		cv2.putText(img,str(dA)+' px',(int(tlX)-10,int(trX)-10),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,0,0),1)


		
		(tlX,trX) = ((tl[0]+bl[0])/2,(tl[1]+bl[1])/2)
		(brX,blX) = ((tr[0]+br[0])/2,(tr[1]+br[1])/2)

		# Draw the mid points
		cv2.circle(black_img,(int(tlX),int(trX)),1,(255,0,0),3)
		cv2.circle(black_img,(int(brX),int(blX)),1,(255,0,0),3)
		cv2.line(black_img,(int(tlX),int(trX)),(int(brX),int(blX)),(100,100,100),1)
		# Draw the mid points
		cv2.circle(img,(int(tlX),int(trX)),1,(255,255,0),3)
		cv2.circle(img,(int(brX),int(blX)),1,(255,255,0),3)
		cv2.line(img,(int(tlX),int(trX)),(int(brX),int(blX)),(0,0,255),1)

		# claculate the distance based on the mid points.
		dB = dist.euclidean((tlX,trX),(brX,blX))

		# print the size in PX on each contour rectangle
		cv2.putText(black_img,str(dB)+' px',(int(tlX)+10,int(trX)+10),cv2.FONT_HERSHEY_SIMPLEX,0.4,(255,255,255),1)
		cv2.putText(img,str(dB)+' px',(int(tlX)+10,int(trX)+10),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,0,0),1)




cv2.imshow('Original Image',image)
cv2.imshow('Output image ',img)
# cv2.imshow('gray_img', gray_img)
# cv2.imshow('thresh', thresh_img)
cv2.imshow('Output Image ',black_img)
# cv2.imwrite('shapes_output.jpg',img)
# cv2.imwrite('shapes_output1.jpg',black_img)
cv2.waitKey(0)

