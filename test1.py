import glob
import re



files = glob.glob("/home/manju/Desktop/pavithra/251120/manju/*.xml")

# rint(files,len(files))

for file in files:
	fr = open(file)
	data = fr.readlines()

	for line in data:
		line = line.strip()
		exp = "(<\w+>)(\w+)(</\w+>)"

		x = re.search(exp,line)
		if x:
			result = x.group(1),x.group(3)
			f = result[0][0]
			l = result[0][-1]
			f1 = result[1][:2]
			l1 = result[1][-1]
		
			if f1+l1 != "</>":
				print(files)
			