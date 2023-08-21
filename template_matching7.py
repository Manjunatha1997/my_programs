import cv2
import numpy as np
import glob
import os
files = glob.glob("/home/manju/Desktop/lincode/test270/*.jpg")

lst = []
skip_files = []
for file in files:
	img_original = cv2.imread(file)
	height, width, depth = img_original.shape
	img = cv2.cvtColor(img_original,cv2.COLOR_BGR2GRAY)

	template = cv2.imread("/home/manju/Desktop/lincode/template.jpg", 0)
	w, h = template.shape[::-1]
	res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)

	try:
		thr = 0.85
		loc = np.where(res >= thr)[::-1]
		loc = tuple((loc[0][0],loc[1][0]))
		# cv2.rectangle(img_original,loc,(loc[0]+w,loc[1]+h),(255,0,0),2)
		lst.append([file,loc[0],loc[1],(loc[0]+w),(loc[1]+h)])
		# cv2.imshow("image",img_original)
		# cv2.waitKey(0)
		# cv2.destroyAllWindows()
	except:
		try:
			thr = 0.8
			loc = np.where(res >= thr)[::-1]
			loc = tuple((loc[0][0],loc[1][0]))
			# cv2.rectangle(img_original,loc,(loc[0]+w,loc[1]+h),(255,0,0),2)
			lst.append([file,loc[0],loc[1],(loc[0]+w),(loc[1]+h)])
		except:
			# print("skipping file",file)
			skip_files.append(file)

print("length of working files::",len(lst))
print("length of skipping files::",len(skip_files))
print("total files are",len(lst)+len(skip_files))

# for f in lst:
#     xml_file = f[0][:-4]+".xml"
#     fw = open(xml_file,"w")
#
#     fw.write("<annotation>\n"
# 	"<folder>test</folder>\n"
# 	"<filename>"+xml_file+"</filename>\n"
# 	"<path>"+xml_file+"</path>\n"
# 	"<source>\n"
# 		"<database>Unknown</database>\n"
# 	"</source>\n"
# 	"<size>\n"
# 		"<width>"+str(width)+"</width>\n"
# 		"<height>"+str(height)+"</height>\n"
# 		"<depth>"+str(depth)+"</depth>\n"
# 	"</size>\n"
# 	"<segmented>0</segmented>\n"
# 	"<object>\n"
# 		"<name>K75T60</name>\n"
# 		"<pose>Unspecified</pose>\n"
# 		"<truncated>0</truncated>\n"
# 		"<difficult>0</difficult>\n"
# 		"<bndbox>\n"
# 			"<xmin>"+str(f[1])+"</xmin>\n"
# 			"<ymin>"+str(f[2])+"</ymin>\n"
# 			"<xmax>"+str(f[3])+"</xmax>\n"
# 			"<ymax>"+str(f[4])+"</ymax>\n"
# 		"</bndbox>\n"
# 	"</object>\n"
# "</annotation>"
#              )
#
#     fw.close()
#

