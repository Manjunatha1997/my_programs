from hashlib import new
from logging import PlaceHolder
import streamlit as st
import os
import pandas as pd
import numpy as np
from utils import check_path_dir
from xml_wrapper_module import *
from PIL import Image






image = Image.open("lincode.png")

st.set_page_config(
  page_title="LIVIS",page_icon=image
)

# st.set_page_config(page_title='My First App', page_icon=':smiley', 
#                    layout="wide", initial_sidebar_state='expanded')

# Title
st.title("Annotation Validation")

path = st.text_input('Enter your input folder path !',placeholder="Enter your input folder path ")
check_path = st.button('Check Path')
if check_path == True:
	resp_path = check_path_dir(path)
	if resp_path == False:
		st.warning("Please check your path ")
	if resp_path == True:
		st.success(" Select action and go !!! ")



action = st.radio("Select Action: ",
				 ('find_all_class_names',
				 'find_no_class_names', 
				 'find_un_annotated_images',
				 'rename_class_names',
				 'delete_class_names',
				 'split_folder',
				 )
				 )

if action == 'find_all_class_names':
	x = st.button('Submit')
	if x == True:
		resp = find_all_classes(path)
		print(resp)
		df = st.json(resp)
		data_frame = pd.DataFrame([resp])
		# data_frame = pd.DataFrame(resp.items(), columns=list(resp.keys()))


		st.bar_chart(data_frame)


			
if action == 'find_un_annotated_images':
	remove = st.radio("Remove ",('No', 'Yes') )
	
	if remove == 'No':
		move = st.radio("move ",('No', 'Yes') )

	if remove == 'Yes':
		sub = st.button('Submit')
		if sub == True:
			resp = find_extra_images(path,remove=True)
			st.json(resp)

	if remove == 'No' and move == 'No':
		sub = st.button('submit')
		if sub == True:
			resp = find_extra_images(path)
			st.json(resp)
	if remove == 'No' and move == 'Yes':
		mv_path = st.text_input('Enter your destination folder path !')
		sub = st.button('submit')
		if sub == True:
			resp = find_extra_images(path,move=mv_path)
			st.json(resp)

if action == 'find_no_class_names':
	remove = st.checkbox('Remove')
	resp = find_no_class_names(path)
	st.text(resp)
	
	if remove:
		resp = find_no_class_names(path,remove=True)
		st.text(resp)

if action == 'rename_class_names':
	old_class_name = st.text_input('Enter class name',placeholder="Enter class name")
	new_class_name = st.text_input('Enter new class name',placeholder="Enter new class name")

	btn = st.button('Submit')
	if btn == True:
		resp = rename_class_name(path,old_class_name,new_class_name)
		st.json(resp)

if action == 'split_folder':
	# file_type = st.radio('selectfile type',('jpg','png'))
	mb_split = st.radio('Define MB or folders',('folders','MB'))

	if mb_split == 'MB':
		set_mb = st.number_input('set MB',min_value=1)
		btn = st.button('Submit')

	if mb_split == 'folders':
		set_folders = st.number_input('Set no.of folders',min_value=1)
		all_mails = []
		for i in range(set_folders):
			j = str(i)
			key = j+'email'
			mail = st.text_input('Enter Email',placeholder='Enter Email',key=j)
			all_mails.append(mail)



		btn = st.button('Submit')
		if btn:
			st.text(all_mails)


if action == 'delete_class_names':
	all_classes = find_all_classes(path)
	all_classes = list(all_classes.keys())
	select_delete_classs = st.multiselect("Select classes you want to delete.",all_classes)
	btn = st.button('Submit')
	if btn == True:
		st.text(select_delete_classs)
		resp = delete_class_names(path,select_delete_classs)
		st.json(resp)




## Remove footer of streamlit
hide_streamlit_style = """
			<style>
			#MainMenu {visibility: hidden;}
			footer {visibility: hidden;}
			
			</style>
			"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 