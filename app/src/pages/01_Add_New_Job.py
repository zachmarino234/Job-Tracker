import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

# Page setup
st.set_page_config(layout = 'wide', page_icon='assets/logo.png')
SideBarLinks()

# set the header of the page
st.header('Add New Job Entry')
st.write(f"### Job Data pulled from TalentTrace Job Extension")

with st.form("Add New Job Entry"):
    appID = st.number_input("Applicant ID", value = 242)
    indID = st.number_input("Industry ID", value = 3)
    companyID = st.number_input("Company ID", value = 960)
    jobTitle = st.text_input("Job Title", value="Financial Manager", placeholder="Enter a job name...", label_visibility="visible")
    salary = st.number_input("Salary", value = 560000)
    description = st.text_area("Job Description", value = "The Head of Fixed Income Asset Management at Kin Inc. would be a senior leadership role responsible for overseeing the company’s fixed income investment strategies and portfolio management. This position would involve developing and implementing investment strategies that align with the company’s financial goals and risk tolerance, while also leading a team of portfolio managers, analysts, and traders. The role would require a deep understanding of global fixed income markets, interest rate trends, and economic indicators, as well as strong analytical skills for bond selection, credit analysis, and risk management. In addition to managing portfolios, the Head of Fixed Income Asset Management would communicate investment strategies and performance to clients and stakeholders, ensuring that the portfolios meet the financial objectives of the company while adhering to regulatory and risk management policies. This role would also involve collaborating with sales and client service teams to attract and retain clients, making it a critical position for driving the success of Kin Inc.'s fixed income portfolios.")
    posLevel = st.selectbox("Position Level", ("Entry", "Senior", "Manager", "Executive"), index=3, placeholder="Select a position level...")
    jobType = st.selectbox("Job Type", ("Remote", "Hybrid", "In-Office"), index=2, placeholder="Select a job type...")
    jobAddress = st.text_input("Address", value="1 Iron St", placeholder="Enter an address...", label_visibility="visible")
    jobCity = st.text_input("City", value="New York", placeholder="Enter a city...", label_visibility="visible")
    jobCountry = st.text_input("Country", value="United States", placeholder="Enter a country...", label_visibility="visible")
    
    added_job = st.form_submit_button("Add Job Entry")

    if added_job:
        job = {}
        job['appID'] = appID
        job['indID'] = indID
        job['companyID'] = companyID
        job['jobTitle'] = jobTitle
        job['salary'] = salary
        job['description'] = description
        job['posLevel'] = posLevel
        job['jobType'] = jobType
        job['jobAddress'] = jobAddress
        job['jobCity'] = jobCity
        job['jobCountry'] = jobCountry

        response = requests.post('http://api:4000/jbr/job_records', json = job)

        if response.status_code == 200:
            st.toast('Success!')
        else:
            st.toast('Failed - please try again')