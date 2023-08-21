import glob
import os 
import xml.etree.ElementTree as ET
import cv2
import shutil

path = '/home/manju/rough_extra/'

jpg = []
xml = []
all = []
for j in os.listdir(path):
    if j.endswith('.jpg'):
        jpg.append(j)

c = 1
for x in os.listdir(path):
    if x.endswith('.xml'):
        if x.split('.')[0]+'.jpg' in jpg:
            # print(path+x)
            # print(path+x.split('.')[0]+'.jpg')
            os.rename(path+x,path+'bb'+str(c)+'.xml')
            os.rename(path+x.split('.')[0]+'.jpg',path+'bb'+str(c)+'.jpg')
            # shutil.copyfile((path+x),os.rename((path+x),'bb'+str(c)+'.xml'))
            # all += path+x
            # all += (path+x.split('.')[0]+'.jpg')
            # shutil.copyfile(path+x.split('.')[0]+'.jpg',os.rename(path+x.split('.')[0]+'.jpg','bb'+str(c)+'.jpg'))
        c += 1


count = 0


# files = glob.glob(os.path.join(path,'*.xml'))
# for file in files:
# #     print((file.split('/')[-1]).split('.')[0])
#     tree = ET.parse(file)
        

# #     tree.find('//path').text = tree.find('//path').text.replace('_2_','_3_')
# #     count = 0
#     for elt in tree.iter():
#         if((elt.tag == 'name')):  #& (elt.text == 'change')):
#             # print(file)
#             elt.text = 'something...'
#             # count += 1
#         if((elt.tag == 'filename')): # & (elt.text == 'squarea')):
#             # print(file)
#             # elt.text = 'a'+file.split(')')[0].split('(')[1]+'.jpg'

#             elt.text = file.split('.')[0].split('/')[-1]+'.jpg'
#         if ((elt.tag == 'path')):
#             # elt.text = 'path/'+'a'+file.split(')')[0].split('(')[1]+'.jpg'
#             elt.text = file.split('.')[0]+'.jpg'
#     count += 1

# #     tree.find('//filename').text = (file.split('/')[-1]).split('.')[0] + '.jpg' 
#     tree.write(file)

# print(count)
