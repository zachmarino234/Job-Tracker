import logging
logger = logging.getLogger(__name__)
import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# set the header of the page
st.header('Add New Job Entry')
st.write(f"### Job Data pulled from TalentTrace Job Extension")

# TODO: constraints on the inputs 
st.text_input("Job Title", value="Financial Manager", placeholder="Enter a job name...", label_visibility="visible")

st.text_input("Salary", value="120000", placeholder="Enter a salary...", label_visibility="visible")

st.text_input("Company", value="State Street", placeholder="Enter a company name...", label_visibility="visible")

st.selectbox("Position Level", ("Entry", "Senior", "Manager", "Executive"), index=2, placeholder="Select a position level...")

st.text_input("Job Type", value="idk", placeholder="Enter a job type...", label_visibility="visible")

st.text_input("Address", value="1 Iron St", placeholder="Enter an address...", label_visibility="visible")

st.text_input("City", value="Boston", placeholder="Enter a city...", label_visibility="visible")

st.text_input("Country", value="United States", placeholder="Enter a country...", label_visibility="visible")

# TODO: Button adds the above data to the database
st.button("Add Job Entry")

