import logging
logger = logging.getLogger(__name__)
import requests
import streamlit as st
from streamlit_extras.app_logo import add_logo
import pandas as pd
import pydeck as pdk
import altair as alt
from urllib.error import URLError
from modules.nav import SideBarLinks

# Page setup
st.set_page_config(layout = 'wide', page_icon='assets/logo.png')
SideBarLinks()
add_logo("assets/logo.png", height=400)

# Displays KPI's if user is administrator role
if st.session_state['role'] == 'administrator':
    st.header("At a Glance")

    # Get the data from the routes
    user_data = pd.DataFrame (
        requests.get('http://api:4000/agg/user_count').json()
    ).iloc[0]

    job_data = pd.DataFrame (
        requests.get('http://api:4000/agg/job_entries').json()
    ).iloc[0]

    company_data = pd.DataFrame (
        requests.get('http://api:4000/agg/companies').json()
    ).iloc[0]

    # Create columns to display them horizontally
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Users", value=user_data)
    col2.metric(label="Job Entries", value=job_data)
    col3.metric(label="Companies", value=company_data)
    
    st.caption("Note: Each metric is 1000 because our mock data generated 1000 rows for each table")

# Most popular countries
st.header("Most Popular Countries")
country_data = pd.DataFrame(
   requests.get('http://api:4000/agg/country_count').json()
)

st.dataframe(country_data, use_container_width=True, column_order=('Country', 'Count'))

# Average salary for each industry
chart_data = pd.DataFrame(
    requests.get('http://api:4000/agg/industry_salary').json()
)

chart = alt.Chart(chart_data).mark_bar().encode(
    x=alt.X('name:N', title='Industry'),  # 'name:N' specifies that x-axis is categorical
    y=alt.Y('Average_Salary:Q', title='Average Salary'),  # 'Average_Salary:Q' specifies that y-axis is quantitative
    color='name:N',  # Optional: Color bars by industry name for better distinction
).properties(
    title='Average Salary per Industry'
)

# Display the chart in Streamlit
st.header("Average Salary per Industry")
st.altair_chart(chart, use_container_width=True)

# Most popular employers
st.header("Most Popular Employers")
employer_data = pd.DataFrame(
   requests.get('http://api:4000/agg/popular_employers').json()
)

st.dataframe(employer_data, use_container_width=True)

# Most popular industries (our mock data has each industry associated with 100 records
# so the results will be the same aka not a bug)
st.header("Most Popular Industries")
industry_data = pd.DataFrame(
   requests.get('http://api:4000/agg/mostpopularinds').json()
)

st.dataframe(industry_data, use_container_width=True, column_order=('Industry', 'Count'))
st.caption("Note: Each Industry has 100 records because our mock data generated 100 rows for each industry")