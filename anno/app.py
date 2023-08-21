from hashlib import new
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
				 ('find_all_class_names','find_no_class_names', 'find_un_annotated_images','rename_class_names')
				 )

if action == 'find_all_class_names':
	x = st.button('Submit')
	if x == True:
		resp = find_all_classes(path)
		print(resp)
		df = st.json(resp)
			
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


## Remove footer of streamlit
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
			
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 