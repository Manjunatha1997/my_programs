import os
import shutil

inp_path = "/home/manju/Desktop/pavithra/IGBT/manju/OP3621_HS7000/crop5/"

xml_file = "/home/manju/Desktop/pavithra/IGBT/manju/OP3621_HS7000/K75T60_fa4_1.xml"

res  = os.listdir(inp_path)

for file in res:
	f = file.split('.')[0]+'.xml'	
	shutil.copyfile(xml_file,inp_path+f)
	