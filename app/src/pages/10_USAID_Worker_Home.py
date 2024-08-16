import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Recruiter, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('See Applicants Data', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/14_Applicant_Data')

if st.button('View Your Notes', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/14_Recruiter_Notes')

if st.button("Add new notes",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/14_New_RecNotes')

if st.button("What's new on the market",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/14_New_Job_Trend')