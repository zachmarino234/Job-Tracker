import logging
logger = logging.getLogger(__name__)
import requests
import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.header('Delete Your Account')

delete = st.button('Delete Account')

if 'show_confirm' not in st.session_state:
    st.session_state.show_confirm = False

if delete:
    st.session_state.show_confirm = True

if st.session_state.show_confirm:
    with st.expander("Are you sure you want to delete your account?", expanded=True):
        st.write("This action cannot be undone.")
        
        # Button to confirm account deletion
        if st.button('Yes, delete my account'):
            # Placeholder for the account deletion logic
            st.success("Your account has been deleted.")
            st.session_state.show_confirm = False
        
        # Button to cancel the deletion and close the pop-up
        if st.button('Cancel'):
            st.session_state.show_confirm = False

    #appID = 242 #Applicant ID number for the user

    #requests.delete(f'http://api:4000/a/applicants/{appID}')
