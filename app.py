import csv
from email import header
from email.policy import default
from turtle import width
import streamlit as st
from streamlit_option_menu import option_menu
import cv2
import pandas as pd
from common_utils import *
from datetime import datetime
import os
import os
from datetime import date
import pandas as pd
from csv import writer
import csv
import bson
from st_clickable_images import clickable_images
import requests
import ast





PART_LIST = ['','Part1','Part2']


def create_csv(inference_images,inspection_time,status,reason,selected_model):
	today_date = date.today()
	today_date = str(today_date)
	today_date_csv_file = 'reports/'+today_date+'.csv'

	if not os.path.exists(today_date_csv_file):
		with open(today_date_csv_file, 'w') as f:
			f.write('inference_images,inspection_time,status,reason,part_name\n')

	with open(today_date_csv_file, 'a', newline='') as f_object:  
		# Pass the CSV  file object to the writer() function
		writer_object = writer(f_object)
		# Result - a writer object
		# Pass the data in the list as an argument into the writerow() function
		writer_object.writerow([inference_images,inspection_time,status,reason,selected_model])  
		# Close the file object
		f_object.close()

# def add_data(inference_images,inspection_time,status,reason,selected_model):
# 	today_date = date.today()
# 	today_date = str(today_date)
# 	# today_date_csv_file = today_date+'.csv'
# 	today_date_csv_file = 'reports/'+today_date+'.csv'


# 	with open(today_date_csv_file, 'a', newline='') as f_object:  
# 		# Pass the CSV  file object to the writer() function
# 		writer_object = writer(f_object)
# 		# Result - a writer object
# 		# Pass the data in the list as an argument into the writerow() function
# 		writer_object.writerow([inference_images,inspection_time,status,reason,selected_model])  
# 		# Close the file object
# 		f_object.close()


## Footer
footer = """
<style>
#MainMenu {visibility: hidden;margin-top:20px;}
footer { visibility: hidden;}
</style>
"""
st.markdown(footer, unsafe_allow_html=True)

st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

## sidebar
with st.sidebar:
	selected = option_menu(
		menu_title = None,
		options = ['Home', 'Operator','Detailed Report'],
		icons = ['house','person','book'],

	)
	# st.write('<p style="color:red;font-weight:bold; font-size:20px; position:absolute; bottom:-460px">PoweredBy Lincode</p>',unsafe_allow_html=True)

## Home
if selected == 'Home':
	img =  cv2.cvtColor(cv2.imread('Lincode-1592836225218.webp'),cv2.COLOR_BGR2RGB)
	img = cv2.resize(img,(1920,1080))
	st.image(img)





## Operator
if selected == 'Operator':
	st.success('LIVE FEED')
	col1, col2,col3 = st.columns([4,1,1])
	
	with col1:
		part_name_placeholder = st.empty()
		part_name = part_name_placeholder.selectbox(

	"Select Part Name",

	PART_LIST)
	with col2:
		if part_name:

			run = st.checkbox('RUN')
	with col3:
		if part_name:
			if run:
				btn = st.button('Inspect')
				if btn:
					CacheHelper().set_json({"inspect":True})
					
				part_name_placeholder.empty()
				part_name_placeholder.text(f"Part Name : {part_name}")
				

	FRAME_WINDOW = st.image([])

	
	status_placeholder = st.sidebar.info('Status : ---')
	# st.sidebar.info('Status')
	# status = st.sidebar.text(' -- ')

	st.sidebar.info('Inspection Count')

	REPORTS = st.sidebar.dataframe(None,use_container_width=True,hide_index=True)


	df = pd.read_csv('inspection_count.csv')


	st.sidebar.info('Quick Report')
	defect_list = st.sidebar.text(' ')

	

	while part_name and run:
		predicted_frame = CacheHelper().get_json('predicted_frame')
		predicted_frame = cv2.resize(predicted_frame,(1920,1080))
		# predicted_frame = cv2.flip(predicted_frame,1)

		frame = predicted_frame.copy()

	

		
		predicted_frame = cv2.cvtColor(predicted_frame,cv2.COLOR_BGR2RGB)
		FRAME_WINDOW.image(predicted_frame)
		is_inspected = CacheHelper().get_json("is_inspected")
	
		if is_inspected:
			CacheHelper().set_json({"is_inspected":False})
			
			worker_response = CacheHelper().get_json("worker_response")
			if not worker_response:
				worker_response = {}
			defects = worker_response.get("defect_list","")
			is_accepted = worker_response.get("status",None)
			time_stamp = worker_response.get("time_stamp",None)
			predicted_images = worker_response.get("predicted_frames",None)
			defect_list.write(defects)


			if is_accepted == 'Accepted':
				df['accepted'][0] += 1
				# status.write('<p style="color:green;font-weight:bold;"> Accepted</p>',unsafe_allow_html=True)
				status_placeholder.success("Status : Accepted")
			if is_accepted == 'Rejected':
				df['rejected'][0] += 1
				# status.write('<p style="color:red;font-weight:bold;"> Rejected</p>',unsafe_allow_html=True)
				status_placeholder.warning("Status : Rejected")

			df['total'][0] += 1
			
			
			df.to_csv('inspection_count.csv',header=True, index=False)
			REPORTS.dataframe(df,use_container_width=True,hide_index=True)
			################################## Detailed report #################
			create_csv(predicted_images,time_stamp,is_accepted,defects,part_name)
				
		btn = False

	else:
		df['accepted'][0] = 0
		df['rejected'][0] = 0
		df['total'][0] = 0
		df.to_csv('inspection_count.csv',header=True, index=False)
		REPORTS.dataframe(df,use_container_width=True,hide_index=True)



def display_images(image_urls):
	for url in image_urls:
		st.image(url, caption='Image', use_column_width=True)

## Detailed Report

if selected == 'Detailed Report':
	col1, col2, col3 = st.columns(3)
	with col1:
		date_selected = st.date_input ( 'Select Date' , value="today" , min_value=None , max_value=None , key=None)
	with col2:
		select_status = st.selectbox("Select Status",["","Accepted","Rejected"])
	with col3:
		select_part_name = st.selectbox("Select Part Name",PART_LIST)

	try:
		if date_selected:

			# sub_col1, sub_col2 = st.columns([4,1])
			# with sub_col1:
			st.text('')
			detailed_report = st.dataframe(None,use_container_width=True)
			
			today_date_csv_file = 'reports/'+str(date_selected)+'.csv'
			data = pd.read_csv(today_date_csv_file)
			
			if select_status and select_part_name:
				data = data[(data['status'] == select_status) & (data['part_name'] == select_part_name)]
			elif select_status:
				data = data[data['status'] == select_status]
			elif select_part_name:
				data = data[data['part_name'] == select_part_name]
		
			# Reorder the columns
			data = data[['part_name', 'status', 'reason', 'inspection_time', 'inference_images']]

			detailed_report.dataframe(data,use_container_width=True)

			# with sub_col2:
			# 	values = data.index.values
				# m = st.markdown("""
				# 		<style>
				# 		div.stButton > button:first-child {
				# 			# background-color: rgb(204, 49, 49);
				# 			height:20px;
				# 			# margin-down:20px;
				# 		}
				# 		</style>""", unsafe_allow_html=True)

				# st.button('Images',use_container_width=True)

				# for index, row in data.iterrows():
				# 	# data[index] = st.button(f"Display Image {row['inference_images']}")
				# 	if st.button(f"image {values[index]}",use_container_width=True):
				# 		# Display the inference_image corresponding to the row
				# 		image_data = ast.literal_eval(row['inference_images'])
				# 		with sub_col1:
				# 			for i in range(len(image_data)):
				# 				st.image(image_data[i], caption=f"Image {image_data[i]}")


			col1, col2, col3 = st.columns(3)
			with col1:
				st.success('Total Accepted : '+str(len(data[data['status']=='Accepted'])))
			with col2:
				st.warning('Total Rejected : '+str(len(data[data['status']=='Rejected'])))
			with col3:
				st.info('Total Count : '+str(len(data)))

			
			


	except Exception as e:
		st.write('Data Not Found : ',e)
	

