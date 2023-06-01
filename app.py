import streamlit as st
import os
import pandas as pd
from PIL import Image
from streamlit_modal import Modal
from xml_wrapper_module_updated import *



image = Image.open("lincode.png")

st.set_page_config(
  page_title="LIVIS",page_icon=image,layout="wide"
)


# st.set_page_config(page_title='My First App', page_icon=':smiley', 
#                    layout="wide", initial_sidebar_state='expanded')

# Title
# st.title("Annotation Validation")

st.markdown("<h1 style='text-align: center;font-weight:bold; color: #4885A2;'>Annotation Validation</h1>", unsafe_allow_html=True)



path = st.text_input('Enter your input folder path !',placeholder="Enter your input folder path ")

# check_path = st.button('Check Path')
# if check_path == True:
# 	resp_path = check_path_dir(path)
# 	if resp_path == False:
# 		st.warning("Please check your path ")
# 	if resp_path == True:
# 		st.success(" Select action and go !!! ")




action = st.selectbox("Select Action",('find_all_class_names',
				 'find_empty_xml', 
				 'find_un_annotated_images',
				 'rename_class_names',
				 'delete_class_names',
				 'split_folder',
				 'change_image_xml',
				 ))

if action == 'find_all_class_names':
	if not path:
		st.warning("Please provide path")
	resp = find_all_classes_recursive(path)

	total_data = {}
	if resp:
		for item in resp:
			for key, value in item.items():
				if key in total_data:
					total_data[key] += value
				else:
					total_data[key] = value
	if total_data:
		## updatind folder path 
		total_data['folder_path'] = path
		# st.json(total_data)
		resp.append(total_data)
	
	if resp:
		df = pd.json_normalize(resp)

		## model for total data 
		modal = Modal(key="model",title="Total Data")
		col1, col2 = st.columns(2)
		with col1:
			open_modal = st.button("View Total Data")
		with col2:
			csv_button = st.download_button(label="Download CSV",data=df.to_csv(index=False),file_name="annotation_count.csv",mime='text/csv')

		if open_modal:
			modal.open()

		if modal.is_open():
			with modal.container():
				st.json(total_data)


		# csv_button = st.download_button(label="Download CSV",data=df.to_csv(index=False),file_name="annotation_count.csv",mime='text/csv')
		st.table(resp)
		# col1, col2 = st.columns(2)
		# with col1:
		# 	df = st.json(resp)
		# with col2:
		# 	df = pd.json_normalize(resp)

		# 	csv_button = st.download_button(label="Download CSV",data=df.to_csv(index=False),file_name="annotation_count.csv",mime='text/csv')
		# 	st.table(resp)

			# st.bar_chart(data_frame)
	else:
		st.text("No classes found  ")

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

if action == 'find_empty_xml':
	resp = find_no_class_names(path)
	if resp:
		st.text(resp)
		remove = st.checkbox('Remove')
		if remove:
			resp = find_no_class_names(path,remove=True)
			st.text(resp)
	else:
		st.text("No files found")

if action == 'rename_class_names':
	x = find_all_classes(path)
	old_class_name = st.selectbox("Select class name ",list(x.keys()))
	new_class_name = st.text_input('Enter new class name',placeholder="Enter new class name")

	btn = st.button('Submit')
	if btn == True:
		resp = rename_class_name(path,old_class_name,new_class_name)
		st.json(resp)

if action == 'split_folder':
	file_type = st.radio('selectfile type',('jpg','png'))
	mb_size = st.number_input("Set MB",min_value=1,max_value=150)
	btn = st.button('Submit')
	if btn == True:
		resp = split_folder(path,mb_size,image_type = file_type)
		st.json(resp)

	# mb_split = st.radio('Define MB or folders',('folders','MB'))

	# if mb_split == 'MB':
	# 	set_mb = st.number_input('set MB',min_value=1)
	# 	btn = st.button('Submit')

	# if mb_split == 'folders':
	# 	set_folders = st.number_input('Set no.of folders',min_value=1)
	# 	all_mails = []
	# 	for i in range(set_folders):
	# 		j = str(i)
	# 		key = j+'email'
	# 		mail = st.text_input('Enter Email',placeholder='Enter Email',key=j)
	# 		all_mails.append(mail)



	# 	btn = st.button('Submit')
	# 	if btn:
	# 		st.text(all_mails)

if action == 'delete_class_names':
	all_classes = find_all_classes(path)
	if all_classes:
		all_classes = list(all_classes.keys())
		select_delete_classs = st.multiselect("Select classes you want to delete.",all_classes)
		btn = st.button('Submit')
		if btn == True:
			resp = delete_class_names(path,select_delete_classs)
			st.json(resp)
	else:
		st.text("No classes found !!!")

if action == 'change_image_xml':
	if not path:
		st.warning("Please provide path")

	new_image_name = st.text_input("Enter new image name",placeholder="Type new image name here ")
	btn = st.button('Submit')
	if btn:
		os.system(f"python change_image_xml.py {path} {new_image_name}")
		st.success("Success")



## Remove footer of streamlit
hide_streamlit_style = """
			<style>
			#MainMenu {visibility: hidden;}
			footer {visibility: hidden;}
			
			</style>
			"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 