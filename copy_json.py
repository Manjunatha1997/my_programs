
import json
import glob
import os



# file = '/home/manju/Downloads/tttttt/with_cam2_232.json'

path = '/home/manju/Downloads/tttttt/'
res = os.listdir(path)
# res = glob.glob(path)

for file in res:
	if file.endswith('.json'):
		with open(path+file) as f:
		  data = json.load(f)

