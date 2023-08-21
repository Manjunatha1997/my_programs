import cv2
import numpy as np
import glob
import os
# files = glob.glob("/home/manju/Desktop/task/*.jpg")
files = glob.glob("/home/manju/Desktop/pavithra/IGBT/manju/OP3621_HS7000/crop1/*.jpg")

lst = []

for file in files:
    try :
        img_original = cv2.imread(file)
        img = cv2.cvtColor(img_original,cv2.COLOR_BGR2GRAY)

        template = cv2.imread("/home/manju/Desktop/pavithra/IGBT/manju/OP3621_HS7000/temp.jpg", 0)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
        thr = 0.28
        loc = np.where(res >= thr)[::-1]
        loc = zip(*loc)
        for i in loc:
            # cv2.rectangle(img,i,(i[0]+w,i[1]+h),(0,0,255),2)

            # print(file,i[0],i[1],(i[0]+w),(i[1]+h))
            lst.append([file,i[0],i[1],(i[0]+w),(i[1]+h)])
    except:
        print("removing file is :::",file)

for f in lst:
    xml_file = f[0][:-4]+".xml"
    fw = open(xml_file,"w")

    fw.write("<annotation>\n"
	"<folder>test</folder>\n"
	"<filename>"+xml_file+"</filename>\n"
	"<path>"+xml_file+"</path>\n"
	"<source>\n"
		"<database>Unknown</database>\n"
	"</source>\n"
	"<size>\n"
		"<width>"+str(w)+"</width>\n"
		"<height>"+str(h)+"</height>\n"
		"<depth>3</depth>\n"
	"</size>\n"
	"<segmented>0</segmented>\n"
	"<object>\n"
		"<name>K75T60</name>\n"
		"<pose>Unspecified</pose>\n"
		"<truncated>0</truncated>\n"
		"<difficult>0</difficult>\n"
		"<bndbox>\n"
			"<xmin>"+str(f[1])+"</xmin>\n"
			"<ymin>"+str(f[2])+"</ymin>\n"
			"<xmax>"+str(f[3])+"</xmax>\n"
			"<ymax>"+str(f[4])+"</ymax>\n"
		"</bndbox>\n"
	"</object>\n"
"</annotation>"
             )

    fw.close()


