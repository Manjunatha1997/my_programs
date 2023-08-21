from turtle import width
from black import T
from click import style
from pyparsing import col
import streamlit as st
from streamlit_option_menu import option_menu
import cv2
from common_utils import *


## Footer
footer = """
<style>
#MainMenu {visibility: hidden;}
footer { visibility: hidden;}
</style>
"""
st.markdown(footer, unsafe_allow_html=True)



with st.sidebar:
    selected = option_menu(
        menu_title = None,
        options = ['Home', 'Operator'],
        icons = ['house','person']

    )


if selected == 'Home':
    img =  cv2.cvtColor(cv2.imread('Lincode-1592836225218.webp'),cv2.COLOR_BGR2RGB)
    img = cv2.resize(img,(1920,1080))
    
    st.image(img)

if selected == 'Operator':
    st.success('LIVE FEED')

    col1, col2 = st.columns([4,1])
    with col1:         
        FRAME_WINDOW = st.image([])

    
    with col2:
        st.info('Status')
        status = st.text(' ')
        st.info('Quick Report')
        defect_list = st.text(' ')



    while True:
        predicted_frame = CacheHelper().get_json('predicted_frame')
        detector_predictions = CacheHelper().get_json('defect_list')
        is_accepted = CacheHelper().get_json('is_accepted')
        
        predicted_frame = cv2.cvtColor(predicted_frame,cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(predicted_frame)
        defect_list.write(detector_predictions)
        if is_accepted == 'Accepted':
            status.write('<p style="color:green;font-weight:bold;">Accepted</p>',unsafe_allow_html=True)
        if is_accepted == 'Rejected':
            status.write('<p style="color:red;font-weight:bold;">Rejected</p>',unsafe_allow_html=True)

