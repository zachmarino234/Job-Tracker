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

## ------------------------ Examples for Role of usaid_worker ------------------------
def ApiTestNav():
    st.sidebar.page_link("pages/12_API_Test.py", label="Test the API", icon='🛜')

def PredictionNav():
    st.sidebar.page_link("pages/11_Prediction.py", label="Regression Prediction", icon='📈')

def ClassificationNav():
    st.sidebar.page_link("pages/13_Classification.py", label="Classification Demo", icon='🌺')

#### ------------------------ System Admin Role ------------------------
def AdminPageNav():
    st.sidebar.page_link("pages/20_Admin_Home.py", label="System Admin", icon='🖥️')
    st.sidebar.page_link("pages/21_ML_Model_Mgmt.py", label='ML Model Management', icon='🏢')
    st.sidebar.page_link("pages/12_API_Test.py", label="Test the API", icon='🛜')


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

        # Show World Bank Link and Map Demo Link if the user is a political strategy advisor role.
        if st.session_state['role'] == 'applicant':
            ApplicantHomeNav()
            AddNewJob()
            SeeAllJobs()
            SeeAggregateData()

        # If the user role is usaid worker, show the Api Testing page
        if st.session_state['role'] == 'usaid_worker':
            PredictionNav()
            ApiTestNav() 
            ClassificationNav()
        
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


# -------------------------------- Sidebar for Sam -----------------------------------------------

def SamNav():
    st.sidebar.page_link("pages/14_Sam.py", label="Sam's Dashboard", icon='🛠️')

def PredictNav():
    st.sidebar.page_link("pages/04_Predictions.py", label="Predict Value Based on Regression Model", icon='📈')

def ViewAPI():
    st.sidebar.page_link("pages/12_API_Test.py", label="View the Simple API Demo", icon='🏛️')

def ViewClassDemo():
    st.sidebar.page_link("pages/02_Map_Demo.py", label="View Classification Demo", icon='⚖️️')
