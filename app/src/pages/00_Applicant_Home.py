import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Applicant, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('Add new Job Entry', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/01_Add_New_Job.py')

if st.button('See all Jobs Entries', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/02_All_Job_Entries.py')

if st.button('See Aggregate Job Data', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/03_Aggregate_Job_Data.py')