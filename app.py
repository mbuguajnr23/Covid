import streamlit as st
import pycountry
import pandas as pd
import plotly.express as px
st.set_page_config(layout="wide", initial_sidebar_state="expanded" )
covid = pd.read_csv("data/covid_cases.csv")

def get_iso3(iso2):
    #Function takes in iso_alpha2 country codes and returns the iso_alpha 3 codes"""
    try:
        return pycountry.countries.get(alpha_2=iso2).alpha_3
    except:
        #In case we have errors that row of data will be left out.
        #Try except is a good way to handle possible errors that might occur while running a function"""
        pass

covid['iso_alpha'] = covid.Country_code.apply(lambda x: get_iso3(x))
fig= px.choropleth(covid,
               locations="iso_alpha",
               color="Cumulative_cases", 
               hover_name="Country", # column to add to hover information
               color_continuous_scale=px.colors.sequential.Viridis,
               animation_frame="Date_reported")# animation based on the dates
fig.update_layout(height=600) #Enlarge the figure
st.plotly_chart(fig, use_container_width=True, theme='streamlit')


### TASKS
## 1. GENERATE THREE MORE ANIMATED GRAPHS i.e. new cases, cumulative deaths, new deaths
## 2. Give your graphs titles and if possible add explanative text after each graph
## 3. Use widgets in the sidebar to help the user chooose between the four animations: e.g. select box, button, radio 
## 4. create bar graphs to show the cumulative cases per day and cumulative daeaths per day 
## 5. deploy your app to streamlit cloud
## 6. submit the link to your streamlit app on dexvirtual


