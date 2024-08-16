import logging
logger = logging.getLogger(__name__)
import requests
import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide', page_icon='assets/logo.png')
SideBarLinks()





# set up the page
st.markdown("# Search for what you need!")

data = {} 
try:
  data = requests.get('http://api:4000/rn/recruiterNotes').json()
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

st.dataframe(data)
