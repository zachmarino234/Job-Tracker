import logging
logger = logging.getLogger(__name__)
import requests
import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

# Page setup
st.set_page_config(layout = 'wide', page_icon='assets/logo.png')
SideBarLinks()

st.header('Remove a Company or Industry from the Database')


with st.form("Remove Company"):
    companyID = st.number_input("Company ID", step=1, format="%d")
    remove_company = st.form_submit_button("Remove Company")
        
    if remove_company:
        st.success("Attempting to remove company...")
        try:
            response = requests.delete(f'http://api:4000/co/company/{companyID}')
            st.write(f"Response status code: {response.status_code}")  # For debugging
                
            if response.status_code == 200:
                st.toast('Success!')
                st.success("Company removed successfully.")
            else:
                st.toast('Failed - please try again')
                st.error(f"Failed to remove company. Error: {response.status_code}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

with st.form("Remove Industry"):
    indID = st.number_input("Industry ID", step =1, format = "%d")
    remove_industry = st.form_submit_button("Remove Industry")
    if remove_industry:
        st.success("Industry removed")
        requests.delete(f'http://api:4000/i/industry/{indID}')