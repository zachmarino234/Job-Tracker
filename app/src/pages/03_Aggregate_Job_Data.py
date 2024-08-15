import logging
logger = logging.getLogger(__name__)
import requests
import streamlit as st
from streamlit_extras.app_logo import add_logo
import pandas as pd
import pydeck as pdk
from urllib.error import URLError
from modules.nav import SideBarLinks

SideBarLinks()

# add the logo
add_logo("assets/logo.png", height=400)

# set up the page
st.markdown("# Aggregate Job Data")
st.sidebar.header("Mapping Demo")
st.write(
    """This Mapping Demo is from the Streamlit Documentation. It shows how to use
[`st.pydeck_chart`](https://docs.streamlit.io/library/api-reference/charts/st.pydeck_chart)
to display geospatial data."""
)

# TODO: Top 5's for different attributes 

# TODO: Average salary

# TODO: 

import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.header("Popular Countries")
map_data = pd.DataFrame(
   #TODO: Map with popular countries (attribute from jobrecords)
)

st.pydeck_chart(
    pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=0,
            longitude=0,
            zoom=1,
            pitch=40,
        ),
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=map_data,
                get_position="[lon, lat]",
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            )
        ],
    )
)

st.header("Average Salary per Industry")
chart_data = pd.DataFrame(
    # TODO: Average salary per industry
    requests.get('http://api:4000/jbr/jobRecords').json()
)
avg_salaries = chart_data.groupby('indID')['salary'].mean().reset_index()
avg_salaries.rename(columns={'indID': 'industry'}, inplace = True)

st.bar_chart(avg_salaries, x='industry', y='salary')
