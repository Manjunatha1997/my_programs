import csv
from email import header
from email.policy import default
from turtle import width
from black import T
from click import style
from matplotlib import rc_file
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
from datetime import date
import pandas as pd
from csv import writer
import csv
import bson
import plotly.express as px
import plotly.graph_objects as go
import glob


cwd = r'D:\python_programs\streamlit_UI'
print(cwd)

def create_csv():
	today_date = date.today()
	today_date = str(today_date)
	today_date_csv_file = cwd+'/reports/'+today_date+'.csv'

	if not os.path.exists(today_date_csv_file):
		with open(today_date_csv_file, 'w') as f:
			f.write('inference_images,inspection_time,status,reason,selected_model\n')



def add_data(inference_images,inspection_time,status,reason,selected_model):
	today_date = date.today()
	today_date = str(today_date)
	# today_date_csv_file = today_date+'.csv'
	today_date_csv_file = cwd+'/reports/'+today_date+'.csv'


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
		options = ['Home', 'Operator','Detailed Report','Data Visualization'],
		icons = ['house','person','book','graph-up-arrow'],

	)
	st.write('<p style="color:red;font-weight:bold; font-size:20px; position:absolute; bottom:-400px">PoweredBy Lincode</p>',unsafe_allow_html=True)

## Home
if selected == 'Home':
	img =  cv2.cvtColor(cv2.imread(cwd+'/Lincode-1592836225218.webp'),cv2.COLOR_BGR2RGB)
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


	df = pd.read_csv(cwd+'/inspection_count.csv')


	st.sidebar.info('Quick Report')
	defect_list = st.sidebar.text(' ')



	while run:
		predicted_frame = CacheHelper().get_json('frame')
		predicted_frame = cv2.resize(predicted_frame,(1920,1080))

		frame = predicted_frame.copy()
		detector_predictions = CacheHelper().get_json('defect_list')
		# is_accepted = CacheHelper().get_json('is_accepted')
		# detector_predictions = ['Model1']
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
			
			
			df.to_csv(cwd+'/inspection_count.csv',header=True, index=False)
			REPORTS.dataframe(df)
			################################## Detailed report #################
			create_csv()
			file_name = str(bson.ObjectId())
			fname = cwd+'/datadrive/'+file_name+'.jpg'
			cv2.imwrite(fname,frame)
			fname_s = fname.replace(cwd+'/datadrive/','localhost:3306/')

			add_data([fname_s],inspection_time,is_accepted,detector_predictions,selected_model)
		btn = False

	else:
		df['accepted'][0] = 0
		df['rejected'][0] = 0
		df['total'][0] = 0
		df.to_csv(cwd+'/inspection_count.csv',header=True, index=False)
		REPORTS.dataframe(df)






## Detailed Report
if selected == 'Detailed Report':
	date_selected = st.date_input ( 'Select Date' , value=None , min_value=None , max_value=None , key=None)

	try:
		if date_selected:
			detailed_report = st.dataframe(None)
			
			today_date_csv_file = cwd+'/reports/'+str(date_selected)+'.csv'
			data = pd.read_csv(today_date_csv_file)
			detailed_report.dataframe(data)
			st.success('Total Accepted '+str(len(data[data['status']=='Accepted'])))
			st.warning('Total Rejected '+str(len(data[data['status']=='Rejected'])))
			st.info('Total Count '+str(len(data)))

			## Download Button for csv
			@st.cache
			def convert_df(df):
				return df.to_csv().encode('utf-8')


			csv = convert_df(data)
			st.download_button(
			"Press to Download",
			csv,
			str(datetime.now())+".csv",
			"text/csv",
			key='download-csv'
			)
		
		
	except:
		st.write('Data Not Found')
	

## Data visuailzation
if selected == 'Data Visualization':
	## one day data visualization
	date_selected = st.date_input ( 'Select Date' , value=None , min_value=None , max_value=None , key=None)


	try:
		today_date_csv_file = cwd+'/reports/'+str(date_selected)+'.csv'
		data = pd.read_csv(today_date_csv_file)

		col1, col2 = st.columns(2)
		with col1:
			## Pie Chart
			fig = go.Figure(
			go.Pie(
			labels = ['Accepted','Rejected'],
			values =[(len(data[data['status']=='Accepted'])),(len(data[data['status']=='Rejected']))],
			hoverinfo = "label+percent",
			textinfo = "value",
			# color=["red", "goldenrod"], 
			# color_discrete_map="identity"
			# color_discrete_sequence = px.colors.sequential.RdBu
			
			

			))
			colors = ['green', 'red']
			fig.update_traces(marker = dict(colors = colors, line=dict(color='#000000', width=2)))
			st.header("Today Analysis")
			st.plotly_chart(fig,use_container_width=True)


		with col2:
			## Pie Chart
			fig = go.Figure(
			go.Pie(
			labels = ['MR192','MR197','MR235','MR244','MR270'],
			values =[(len(data[data['selected_model']=='MR192'])),(len(data[data['selected_model']=='MR197'])),(len(data[data['selected_model']=='MR235'])),(len(data[data['selected_model']=='MR244'])),(len(data[data['selected_model']=='MR270']))],
			hoverinfo = "label+percent",
			textinfo = "value"
			))
			st.header("Today Analysis")
			st.plotly_chart(fig,use_container_width=True)


		

	except:
		st.write('Today Data Not Found ')

	## Total data visualization
	try:

		f_accepted = 0
		f_rejected = 0
		f_total = 0
		MR192_count = 0
		MR197_count = 0
		MR235_count = 0
		MR244_count = 0
		MR270_count = 0
		

		
		for file in glob.glob(cwd+'/reports/*.csv'):

			data = pd.read_csv(file)
			f_accepted += len(data[data['status']=='Accepted'])
			f_rejected += len(data[data['status']=='Rejected'])
			MR192_count += (len(data[data['selected_model']=='MR192']))
			MR197_count += (len(data[data['selected_model']=='MR197']))
			MR235_count += (len(data[data['selected_model']=='MR235']))
			MR244_count += (len(data[data['selected_model']=='MR244']))
			MR270_count += (len(data[data['selected_model']=='MR270']))

			f_total += (len(data))

		col1, col2 = st.columns(2)
		with col1:
			## Pie Chart
			fig = go.Figure(
			go.Pie(
			labels = ['Accepted','Rejected'],
			values =[f_accepted,f_rejected],
			hoverinfo = "label+percent",
			textinfo = "value"
			))
			
			colors = ['green', 'red']
			fig.update_traces(marker = dict(colors = colors, line=dict(color='#000000', width=2)))

			st.header("Total Analysis")
			st.plotly_chart(fig,use_container_width=True)
		
		with col2:
			## Pie Chart
			fig = go.Figure(
			go.Pie(
			labels = ['MR192','MR197','MR235','MR244','MR270'],
			values =[MR192_count,MR197_count,MR235_count,MR244_count,MR270_count],
			hoverinfo = "label+percent",
			textinfo = "value"
			))
			st.header("Total Analysis")
			st.plotly_chart(fig,use_container_width=True)
	except:
		st.write('Data Not Found')


