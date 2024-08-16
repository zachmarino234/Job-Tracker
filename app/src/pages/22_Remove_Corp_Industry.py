import logging
logger = logging.getLogger(__name__)
import requests
import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.header('Remove a Company or Industry from the Database')

delete_corp = st.button('Delete Company')

delete_ind = st.button('Delete Industry')



if delete_corp:
    with st.form("Remove Company"):
        companyID = st.number_input("Company ID", step =1, format = "%d")
        remove_company = st.form_submit_button("Remove Company")
        if remove_company:
            st.success("Company removed")
            requests.delete(f'http://api:4000/co/company/{companyID}')

if delete_ind:
    with st.form("Remove Industry"):
        indID = st.number_input("Industry ID", step =1, format = "%d")
        remove_industry = st.form_submit_button("Remove Industry")
        if remove_industry:
            st.success("Industry removed")
            requests.delete(f'http://api:4000/i/industry/{indID}')