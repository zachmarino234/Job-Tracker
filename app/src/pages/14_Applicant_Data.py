import logging
logger = logging.getLogger(__name__)
import requests
import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()


# set up the page
st.markdown("# All applicants")


#TODO: this table needs to show Job title, Company Name, Industry, date applied, description, job address, city, country, poslevel, salary
data = {} 
try:
  data = requests.get('http://api:4000/a/applicants').json()
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

st.dataframe(data)

