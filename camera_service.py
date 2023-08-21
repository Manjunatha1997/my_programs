import cv2
import multiprocessing
import sys
sys.path.append(r'D:\python_programs\pytorch_tutorial\detector')
from common_utils import CacheHelper





class CameraConfig:
	def __init__(self):
		'''
			Here the below mentioned  all camera_id, camera_name and camera_index should be unique, that should not conflict for another camera config.

		'''
		## Web camera
		self.web_cam = False
		self.web_cam_config = [{'camera_id':0,'camera_name':'top web','camera_index':'1'}]

		## Baumer camera
		self.baumer_cam = False
		self.baumer_cam_config = [{'camera_id':'camera ip here', 'camera_name': 'left baumer','camera_index':'1'}]

		## Lucid camera
		self.lucid_cam = False
		self.lucid_cam_config = [{'camera_id':'camera ip here', 'camera_name': 'right','camera_index':'1'}]

		## Basler camera
		self.basler_cam = False
		self.basler_cam_config = [{'camera_id':'camera ip here', 'camera_name': 'front','camera_index':'1'}]

		## Mobile IP camera
		self.mobile_cam_ip = True
		self.mobile_cam_ip_config = [{'camera_id':'192.168.32.93', 'camera_name': 'front','camera_index':'5'},
		{'camera_id':'192.168.32.56', 'camera_name': 'front','camera_index':'6'},
		{'camera_id':'192.168.32.159', 'camera_name': 'front','camera_index':'7'},
		{'camera_id':'192.168.32.148', 'camera_name': 'front','camera_index':'8'},
		]
		
	def run_web_cam(self,id,name,index):
		'''
		Id can be passed through the cv2.VideoCapture(id)
		Here the name is name of that camera, index is index number ( string ).
		This index shuold be unique. 
		Index is used for disply the window name.
		Index is used as a key for sending frames to redis.

		'''
		while True:
			try:
				cap = cv2.VideoCapture(id)
				while True:
					ret, frame = cap.read()
					CacheHelper().set_json({index:ret})
				
					if ret:
						cv2.imshow(index,frame)
						if cv2.waitKey(1) and 0xFF == ord('q'):
							break
					else:
						cap = cv2.VideoCapture(id)
				cap.release()
			
				
			except Exception as e:
				print(e)	

	def run_baumer_cam(self):
		pass

	def run_lucid_cam(self):
		pass

	def run_basler_cam(self):
		pass
	
	def run_mobile_cam_ip(self,id,name,index):
		'''
		Id can be passed through the cv2.VideoCapture(id)
		Here the name is name of that camera, index is index number ( string ).
		This index shuold be unique. 
		Index is used for disply the window name.
		Index is used as a key for sending frames to redis.

		'''
		while True:
			try:
				cap = cv2.VideoCapture(f'rtsp://{str(id)}:8080/h264_ulaw.sdp')
			
				while True:
					ret, frame = cap.read()		
					CacheHelper().set_json({index:frame})

					frame = cv2.resize(frame,(640,480))	
					if ret:
						cv2.imshow(index,frame)

						if cv2.waitKey(1) and 0xFF == ord('q'):
							break
				cap.release()

			except cv2.error as e:
				print(e)

	
	def __main__(self,consolidated_config):
		consolidated_config = consolidated_config
		print(consolidated_config)
		thread_pool = {}

		for cam_dict in consolidated_config:
			for cam_type, individual_dict in cam_dict.items():
				if cam_type == 'web_cam':
					for pool in individual_dict:  
						thread_pool[pool['camera_id']] = multiprocessing.Process(target=self.run_web_cam, args=(pool['camera_id'],pool['camera_name'],pool['camera_index']))
				if cam_type == 'mobile_cam_ip':
					for pool in individual_dict:  
						thread_pool[pool['camera_id']] = multiprocessing.Process(target=self.run_mobile_cam_ip, args=(pool['camera_id'],pool['camera_name'],pool['camera_index']))
			
		try:
			for tt in thread_pool:
				thread_pool[tt].start()
			for tt in thread_pool:
				thread_pool[tt].join()
		except:
			for tt in thread_pool:
				thread_pool[tt].start()
			for tt in thread_pool:
				thread_pool[tt].join()
if __name__ == '__main__':
	cc = CameraConfig()
	consolidated_config = []

	if cc.web_cam is True:
		consolidated_config.append({'web_cam':cc.web_cam_config})
	if cc.baumer_cam is True:
		cc.__main__(cc.basler_cam_config)
	if cc.lucid_cam is True:
		cc.__main__(cc.lucid_cam_config)
	if cc.basler_cam is True:
		cc.__main__(cc.basler_cam_config)
	if cc.mobile_cam_ip is True:
		consolidated_config.append({'mobile_cam_ip':cc.mobile_cam_ip_config})
	
	if bool(consolidated_config):
		cc.__main__(consolidated_config)
		

