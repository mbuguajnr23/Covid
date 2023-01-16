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



### TASKS
## 1. GENERATE THREE MORE ANIMATED GRAPHS i.e. new cases, cumulative deaths, new deaths
fig_new_cases = px.choropleth(covid,
               locations="iso_alpha",
               color="New_cases", 
               hover_name="Country", 
               color_continuous_scale=px.colors.sequential.Viridis,
               animation_frame="Date_reported")
fig_new_cases.update_layout(height=600) 

# cumulative deaths
fig_cumulative_deaths = px.choropleth(covid,
               locations="iso_alpha",
               color="Cumulative_deaths", 
               hover_name="Country", 
               color_continuous_scale=px.colors.sequential.Viridis,
               animation_frame="Date_reported")
fig_cumulative_deaths.update_layout(height=600) 

#  new deaths
fig_new_deaths = px.choropleth(covid,
               locations="iso_alpha",
               color="New_deaths", 
               hover_name="Country", 
               color_continuous_scale=px.colors.sequential.Viridis,
               animation_frame="Date_reported")
fig_new_deaths.update_layout(height=600) 


## 2. Give your graphs titles and if possible add explanative text after each graph
## 3. Use widgets in the sidebar to help the user chooose between the four animations: e.g. select box, button, radio 
# Allow user to choose which animation to view
animation_options = ["Cumulative cases", "New cases", "Cumulative deaths", "New deaths"]
animation_choice = st.selectbox("Select animation", animation_options)

if animation_choice == "Cumulative cases":
    st.write("Cumulative COVID-19 Cases per country over time")
    st.write("This graph shows the cumulative number of COVID-19 cases per country over time, as reported by the World Health Organization.")
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')
elif animation_choice == "New cases":
    st.write("New COVID-19 Cases per country over time")
    st.write("This graph shows the number of new COVID-19 cases per country over time, as reported by the World Health Organization.")
    st.plotly_chart(fig_new_cases, use_container_width=True, theme='streamlit')

elif animation_choice == "Cumulative deaths":
    st.write("Cumulative COVID-19 Deaths per country over time")
    st.write("This graph shows the cumulative number of deaths caused by COVID-19 per country over time, as reported by the World Health Organization.")
    st.plotly_chart(fig_cumulative_deaths, use_container_width=True, theme='streamlit')
else:
    st.write("New COVID-19 Deaths per country over time")
    st.write("This graph shows the number of new deaths caused by COVID-19 per country over time, as reported by the World Health Organization.")
    st.plotly_chart(fig_new_deaths, use_container_width=True, theme='streamlit')

## 4. create bar graphs to show the cumulative cases per day and cumulative daeaths per day 
## 5. deploy your app to streamlit cloud
## 6. submit the link to your streamlit app on dexvirtual


