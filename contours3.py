import cv2

img = cv2.imread('outimage.jpg')

edge = cv2.Canny(img,127,255)

# ret,contours, hierarchy = cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contours= cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# print(str(len(ret)))
print(str(len(contours)))
# print(str(len(hierarchy)))



# cv2.drawContours(img,contours,-1,(255,0,0),1)
#
# cv2.imshow('image',img)
# cv2.imshow('edge',edge)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
