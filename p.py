# pip install paddlepaddle-gpu
# pip install paddleocr


from paddleocr import PaddleOCR,draw_ocr 
import os
import matplotlib.pyplot as plt
# %matplotlib inline
import cv2
ocr = PaddleOCR(use_angle_cls=True)

# result = ocr.ocr(img_path)
# print("======================")
out_path = 'L:\\workspace\\nikil\\output\\'
font = 'L:\\workspace\\nikil\\simfang.ttf'

img_path = 'L:\\workspace\\nikil\\bb.jpg'
print("redddddddddddddddddddd1",img_path)
print("allllllllllllllllll********============", img_path, out_path, font)

result = ocr.ocr(img_path)
# print("99999999999999999999999999999999999999999999999999999999",result)
for i in result:
    print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[",i[1][0])
    # for j in i:
    #     print("---------------------",type(j))
    #     print("*********************",j[0])



# def save_ocr(img_path, out_path, result, font):
#     # print("-----------------------------------------------------------------------")

#     save_path = os.path.join(out_path, img_path.split('\\')[-1] + 'output')

#     image = cv2.imread(img_path)
#     print("redddddddddddddddddddd2",img_path)
#     boxes = [line[0] for line in result]
#     txts = [line[1][0] for line in result]
#     scores = [line[1][1] for line in result]

#     im_show = draw_ocr(image, boxes, txts, scores, font_path=font)
#     # print("redddddddddddddddddddd3",img_path)
#     # cv2.imwrite(save_path, im_show)
#     cv2.imwrite("drwdrw2.jpg", im_show)

#     img = cv2.cvtColor(im_show, cv2.COLOR_BGR2RGB)
#     plt.imshow(img)


# save_ocr(img_path, out_path, result, font)
