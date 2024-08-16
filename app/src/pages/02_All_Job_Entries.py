import logging
logger = logging.getLogger(__name__)
import requests
import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

# Page setup
st.set_page_config(layout = 'wide', page_icon='assets/logo.png')
SideBarLinks()
add_logo("assets/logo.png", height=400)
st.markdown("# All Job Entries")


data = {} 
try:
  data = requests.get('http://api:4000/jbr/job_records/user_job_entries/242').json()
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

st.dataframe(data, column_order=('Position', 'Company', 'Industry', 'Salary', 'Applied', 'Description', 'Level', 'Address', 'City', 'Country'))

