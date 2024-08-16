import streamlit as st
from streamlit_extras.app_logo import add_logo
import requests
import pandas as pd
import pydeck as pdk
import altair as alt
from urllib.error import URLError
from modules.nav import SideBarLinks

# Page setup
st.set_page_config(layout = 'wide', page_icon='assets/logo.png')
SideBarLinks()

st.markdown("# What's new in the job market?")


st.header("Most Lucrative Positions")
lucrative_positions = pd.DataFrame(
   requests.get('http://api:4000/agg/lucrativeposition').json()
)

st.dataframe(lucrative_positions, use_container_width=True) 

             
