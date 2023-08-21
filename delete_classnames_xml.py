
import xml.etree.ElementTree as ET
from pascal_voc_writer import Writer

tree = ET.parse('/home/manju/Downloads/batch_23_5.xml')
root = tree.getroot()
for object in root.findall('object'):
	name = object.find('name').text
	
	if name == 'Shot_Shot_Presence':
		root.remove(object)	

tree.write('/home/manju/Downloads/output.xml')



# def delete_classname(xml_file, class_name):
#     tree = ET.parse(xml_file)
#     root = tree.getroot()
#     for object in root.findall('object'):
#         name = object.find('name').text
        
#         if name == class_name:
#             print(xml_file, class_name)
#             # root.remove(object)	

#     # tree.write(xml_file)




# main_path = 'D:\\indoData\\annotations23\\annotations\\'


# res = os.walk(main_path)

# for i in res:
#     root = i[0]
#     folders = i[1]
#     files = i[2]

#     for file in files:
#         if file.endswith('.xml'):

#             # print(file)
#             xml_file = root + '\\' + file
#             # print(xml_file)
#             delete_classname(xml_file, 'operation_missing')

