
import os
import glob

path = "/home/manju/Downloads/Deeplab_Images/"

files = os.listdir(path)

for file in files:
	if file.endswith('.json'):
		fr = open(path+file)

		data = fr.readlines()
		fw = open(file,'w')

		for line in data:
			line = line.strip()
			if line.startswith('"label"'):
				# fw.write('"imagePath":'+'"'+file.split('.')[0]+'.jpg'+'"'+',')
				fw.write('"'+'label'+'": '+'"'+'Black_Sealent'+'"'+',')
			else:
				fw.write(line)


		fw.close()

		fr.close()

