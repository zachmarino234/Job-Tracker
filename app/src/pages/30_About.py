import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# About this App")

st.markdown (
    """
    As college students who are actively seeking internships, 
    we find it extremely difficult to keep up with the fast-paced 
    and convoluted recruiting process. Applications for companies 
    release at different times, on different websites, with different 
    interview schedules. This sheer amount of information often makes 
    a spreadsheet overwhelming and inefficient when it comes to 
    strategizing our interview process. As well, we have no frame of 
    reference when it comes to what types of jobs are popular, what 
    companies are seeing an uptick of applications, etc. With that in 
    mind, we created TalentTrace, a Job Tracker and database where 
    users can not only track their job applications, but the entries 
    they add are aggregated into trends that everyone can see and use.

    Logo created in Adobe Illustrator by Zach :)
    """
        )

if st.sidebar.button("Go Back"):
    st.switch_page('Home.py')