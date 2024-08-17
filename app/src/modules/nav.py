# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

import streamlit as st

#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon='🏠')

def AboutPageNav():
    st.sidebar.page_link("pages/30_About.py", label="About", icon="🧠")

#### ------------------------ Role: applicant ------------------------
def ApplicantHomeNav():
    st.sidebar.page_link("pages/00_Applicant_Home.py", label="Applicant Home", icon='👤')

def AddNewJob():
    st.sidebar.page_link("pages/01_Add_New_Job.py", label="Add New Job Entry", icon='🧑‍💻')

def SeeAllJobs():
    st.sidebar.page_link("pages/02_All_Job_Entries.py", label="See All Job Entries", icon='🖥️')

def SeeAggregateData():
    st.sidebar.page_link("pages/03_Aggregate_Job_Data.py", label="See Aggregate Job Data", icon='📊')

def DeleteAccount():
    st.sidebar.page_link("pages/04_Delete_Account.py", label = "Delete Your Account", icon = '🚫')

# -------------------------------- Sidebar for Sam -----------------------------------------------

def SamNav():
    st.sidebar.page_link("pages/10_Recruiter_Home.py", label="Sam's Dashboard", icon='🛠️')

def viewRecruiterNotes():
    st.sidebar.page_link("pages/14_Recruiter_Notes.py", label="View Your Notes", icon='🔎')

def addInterviewRecord():
    st.sidebar.page_link("pages/13_New_RecNotes.py", label="Add New Interview Records", icon='📝')

def viewApplicantData():
    st.sidebar.page_link("pages/11_Applicant_Data.py", label="Who applied recently?", icon='📥')

def viewJobTrend():
    st.sidebar.page_link("pages/12_New_Job_Trend.py", label="What's new on the market?", icon='📊')

#### ------------------------ Sidebar for Alex ------------------------
def AdminPageNav():
    st.sidebar.page_link("pages/20_Admin_Home.py", label="System Admin", icon='🖥️')
    st.sidebar.page_link("pages/03_Aggregate_Job_Data.py", label="See Aggregate Job Data", icon='📊')
    st.sidebar.page_link("pages/23_UpdateAdd_Corp_Industry.py", label="Update/Add a Company or Industry", icon='🌐')
    st.sidebar.page_link("pages/22_Remove_Corp_Industry.py", label="Remove a Company or Industry", icon='🚫')

# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in. 
    """    

    # add a logo to the sidebar always
    st.sidebar.image("assets/logo.png", width = 250)

    # If there is no logged in user, redirect to the Home (Landing) page
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page('Home.py')
        
    if show_home:
        # Show the Home page link (the landing page)
        HomeNav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        # Show persona 1's pages (Barney).
        if st.session_state['role'] == 'applicant':
            ApplicantHomeNav()
            AddNewJob()
            SeeAllJobs()
            SeeAggregateData()
            DeleteAccount()

        # Show persona 2's pages (Sam).
        if st.session_state['role'] == 'dept_head':
            SamNav()
            viewRecruiterNotes() 
            addInterviewRecord()
            viewApplicantData()
            viewJobTrend()
        
        # If the user is an administrator, give them access to the administrator pages
        if st.session_state['role'] == 'administrator':
            AdminPageNav()

    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state['role']
            del st.session_state['authenticated']
            st.switch_page('Home.py')