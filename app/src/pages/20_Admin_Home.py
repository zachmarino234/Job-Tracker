import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

# Page setup
st.set_page_config(layout = 'wide', page_icon='assets/logo.png')
SideBarLinks()

st.title('System Admin Home Page')

if st.button('Update ML Models', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/21_ML_Model_Mgmt.py')

if st.button('Update/Add a Company or Industry', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/23_UpdateAdd_Corp_Industry.py')

if st.button('Remove a Company or Industry', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/22_Remove_Corp_Industry.py')

