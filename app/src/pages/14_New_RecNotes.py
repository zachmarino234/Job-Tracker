import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# set the header of the page
st.header('Add New Note')

with st.form("Add New Note"):
    interviewID = st.number_input("Interview ID", value = 1)
    compensation_range = st.number_input("Compensation", value = 336387.99)
    role = st.text_area("Job Title", value="Financial Manager", placeholder="Enter a job name...", label_visibility="visible")
    popularSkill = st.text_area("Popular Skill", value="Enter skills", label_visibility="visible")
    popularCertificates = st.text_area("Popular Certificate", value = "Enter certificates", label_visibility="visible")
    
    
    added_note = st.form_submit_button("Add New Note")

    if added_note:
        recruiternote = {}
        recruiternote['interviewID'] = interviewID
        recruiternote['compensation_range'] = compensation_range
        recruiternote['role'] = role
        recruiternote['popularSkill'] = popularSkill
        recruiternote['popularCertificates'] = popularCertificates
        

        requests.post('http://api:4000/rn/recruiterNotes', json = recruiternote)