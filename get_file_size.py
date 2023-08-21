import os
path = '/home/manju/Desktop/magna_flux/mf/'
def get_file_size(path):
	res = os.listdir(path)
	for file in res:
		file = path+file
		size = os.path.getsize(file)
		print(file,', size:',size ,'bytes')
get_file_size(path)