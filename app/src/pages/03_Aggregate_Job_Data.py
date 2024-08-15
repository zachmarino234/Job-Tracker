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

SideBarLinks()

# add the logo
add_logo("assets/logo.png", height=400)

st.header("Most Popular Countries")
country_data = pd.DataFrame(
   #TODO: Map with popular countries
   requests.get('http://api:4000/agg/country_count').json()
)

st.dataframe(country_data, use_container_width=True, column_order=('Country', 'Count'))

chart_data = pd.DataFrame(
    # TODO: Average salary per industry
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

st.header("Most Popular Employers")
employer_data = pd.DataFrame(
   requests.get('http://api:4000/agg/popular_employers').json()
)

st.dataframe(employer_data, use_container_width=True)