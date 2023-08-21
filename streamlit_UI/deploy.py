import csv
from email import header
from email.policy import default
from turtle import width
from black import T
from click import style
from pyparsing import col
import streamlit as st
import time
from multiprocessing import Process
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



def create_csv():
	today_date = date.today()
	today_date = str(today_date)
	today_date_csv_file = 'reports/'+today_date+'.csv'

	if not os.path.exists(today_date_csv_file):
		with open(today_date_csv_file, 'w') as f:
			f.write('inference_images,inspection_time,status,reason,selected_model\n')



def add_data(inference_images,inspection_time,status,reason,selected_model):
	today_date = date.today()
	today_date = str(today_date)
	# today_date_csv_file = today_date+'.csv'
	today_date_csv_file = 'reports/'+today_date+'.csv'


	with open(today_date_csv_file, 'a', newline='') as f_object:  
		# Pass the CSV  file object to the writer() function
		writer_object = writer(f_object)
		# Result - a writer object
		# Pass the data in the list as an argument into the writerow() function
		writer_object.writerow([inference_images,inspection_time,status,reason,selected_model])  
		# Close the file object
		f_object.close()


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
	st.write('<p style="color:red;font-weight:bold; font-size:20px; position:absolute; bottom:-460px">PoweredBy Lincode</p>',unsafe_allow_html=True)

## Home
if selected == 'Home':
	img =  cv2.cvtColor(cv2.imread('Lincode-1592836225218.webp'),cv2.COLOR_BGR2RGB)
	img = cv2.resize(img,(1920,1080))
	st.image(img)





## Operator
if selected == 'Operator':
	st.success('LIVE FEED')
	col1, col2,col3 = st.columns([4,1,1])
	with col2:
		run = st.checkbox('Run')
	with col1:
		model = st.radio(

    "Select Model",

    ('MR192','MR197','MR235','MR244','MR270'))
	with col3:
		btn = st.button('Inspect')
	


	FRAME_WINDOW = st.image([])

	
	st.sidebar.info('Status')
	status = st.sidebar.text(' ')

	st.sidebar.info('Inspection Count')

	REPORTS = st.sidebar.dataframe(None)


	df = pd.read_csv('inspection_count.csv')


	st.sidebar.info('Quick Report')
	defect_list = st.sidebar.text(' ')



	while run:
		predicted_frame = CacheHelper().get_json('frame')
		predicted_frame = cv2.resize(predicted_frame,(1920,1080))

		frame = predicted_frame.copy()
		detector_predictions = CacheHelper().get_json('defect_list')
		is_accepted = CacheHelper().get_json('is_accepted')
		detector_predictions = ['Model1']
		selected_model = model
		if model in detector_predictions:
			is_accepted = 'Accepted'
		else:
			is_accepted = 'Rejected'

		inspection_time = str(datetime.now())
		
		predicted_frame = cv2.cvtColor(predicted_frame,cv2.COLOR_BGR2RGB)
		FRAME_WINDOW.image(predicted_frame)
		defect_list.write(detector_predictions)
		
		if btn:
			if is_accepted == 'Accepted':
				df['accepted'][0] += 1
				status.write('<p style="color:green;font-weight:bold;">Accepted</p>',unsafe_allow_html=True)
			if is_accepted == 'Rejected':
				df['rejected'][0] += 1
				status.write('<p style="color:red;font-weight:bold;">Rejected</p>',unsafe_allow_html=True)
			df['total'][0] += 1
			
			
			df.to_csv('inspection_count.csv',header=True, index=False)
			REPORTS.dataframe(df)
			################################## Detailed report #################
			create_csv()
			file_name = str(bson.ObjectId())
			fname = './datadrive/'+file_name+'.jpg'
			cv2.imwrite(fname,frame)
			fname_s = fname.replace('./datadrive/','localhost:3306/')

			add_data([fname_s],inspection_time,is_accepted,detector_predictions,selected_model)
		btn = False

	else:
		df['accepted'][0] = 0
		df['rejected'][0] = 0
		df['total'][0] = 0
		df.to_csv('inspection_count.csv',header=True, index=False)
		REPORTS.dataframe(df)






## Detailed Report
if selected == 'Detailed Report':
	date_selected = st.date_input ( 'Select Date' , value=None , min_value=None , max_value=None , key=None)
	try:
		if date_selected:
			detailed_report = st.dataframe(None)
			
			today_date_csv_file = 'reports/'+str(date_selected)+'.csv'
			data = pd.read_csv(today_date_csv_file)
			detailed_report.dataframe(data)
			st.success('Total Accepted '+str(len(data[data['status']=='Accepted'])))
			st.warning('Total Rejected '+str(len(data[data['status']=='Rejected'])))
			st.info('Total Count '+str(len(data)))

	except:
		st.write('Data Not Found')
	

