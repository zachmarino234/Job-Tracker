import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks
import datetime
import json
# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# set the header of the page
st.header('Add New Note')




with st.form("Add New Note"):
    job_ID = st.number_input("Job ID", placeholder="Enter ID", label_visibility="visible")
    app_ID = st.number_input("App ID", placeholder="Enter ID", label_visibility="visible")
    recruiter_ID = st.number_input("recruiterID", placeholder="Enter ID", label_visibility="visible")

    
    
    added_note = st.form_submit_button("Add New Note")

    if added_note:

        recruiternote = {}
        recruiternote['jobID'] = job_ID
        recruiternote['appID'] = app_ID
        recruiternote['recruiterID'] = recruiter_ID
        
        

        response = requests.post('http://api:4000/rn/recruiterNotes', json = recruiternote)

        if response.status_code == 200:
            st.toast('Success')
        else:
            st.toast('Failed - Please try again')

