import cv2
from pascal_voc_writer import Writer
from tkinter import simpledialog

import glob


image = 'image.jpg'

img = cv2.imread(image)
img = cv2.resize(img,(640,480))
image1 = img.copy()

# variables
ix = -1
iy = -1

drawing = False

out = '/home/manju/Desktop/tool/'

all_cord = []


def draw_rectangle_with_drag(event, x, y, flags, param):
    
    global ix, iy, drawing, img

    if event == cv2.EVENT_LBUTTONDOWN:

        drawing = True
        ix = x
        iy = y          
            
    # elif event == cv2.EVENT_MOUSEMOVE:
    #     if drawing == True:

    #         cv2.rectangle(img, pt1 =(ix,iy),
    #                     pt2 =(x,y),
    #                     color =(236, 218, 218),
    #                     thickness = 3)
    

        drawing = False

        cv2.rectangle(img, pt1 = (ix,iy),
                    pt2 = (x,y),
                    color =(0, 255, 0),
                    thickness = 3)
        
        print([ix,iy,x,y])
        all_cord.append([ix,iy,x,y])



cv2.namedWindow(winname = "Title of Popup Window")
cv2.setMouseCallback("Title of Popup Window",
                    draw_rectangle_with_drag)

while True:
    cv2.imshow("Title of Popup Window", img)
    
    if cv2.waitKey(10) == 27:

        print(out)
        print(all_cord)

        split_name = image.split('.')
        img_name = split_name[0]

        writer = Writer(img_name+'.jpg',640,480)
        for i in all_cord:

            writer.addObject("USER_INP",i[0],i[1],i[2],i[3])

        writer.save(out + img_name+'.xml')
        cv2.imwrite(out+image,image1)        


        break

cv2.destroyAllWindows()

