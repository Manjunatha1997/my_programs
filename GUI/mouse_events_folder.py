import cv2
from pascal_voc_writer import Writer
import glob


path = '/home/manju/Desktop/delete/'

for file in glob.glob(path+'*.jpg'):

    image = file

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
        #         # print(ix,iy,x,y)
        #         cv2.rectangle(img, pt1 =(ix,iy),
        #                     pt2 =(x,y),
        #                     color =(230, 242, 255),
        #                     thickness = 1)
        
        elif event == cv2.EVENT_LBUTTONUP:

            drawing = False

            cv2.rectangle(img, pt1 = (ix,iy),
                        pt2 = (x,y),
                        color =(0, 255, 0),
                        thickness = 2)
            
            print([ix,iy,x,y])
            all_cord.append([ix,iy,x,y])



    cv2.namedWindow(winname = image)
    cv2.setMouseCallback(image,
                        draw_rectangle_with_drag)

    while True:
        cv2.imshow(image, img)

        if cv2.waitKey(10) == 27:
            print('closing ...')
            exit()

        if cv2.waitKey(10) == ord('s'):
            cv2.imshow(image, img)

            print(out)
            print(all_cord)

            split_name = image.split('/')
            img_name = split_name[-1].split('.')[0]
            print(img_name,'**************')

            writer = Writer(img_name+'.jpg',640,480)
            for i in all_cord:

                writer.addObject('RedSpring',i[0],i[1],i[2],i[3])

            writer.save(path + img_name+'.xml')
            cv2.imwrite(path+img_name+'.jpg',image1)        


            break

    
    cv2.destroyAllWindows()

