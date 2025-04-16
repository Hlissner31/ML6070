import streamlit as st
import pandas as pd
import numpy as np
import plotly_express as px

#x = st.slider('x')
#st.write(x, 'Squared is', x*x)

#try text inputs
#url = st.text_input('Enter your favorite URL')
#st.write('My favorite URL is >>',url)

#read and display data
#df = pd.read_csv("football_data.csv")
#if st.checkbox('Show dataframe'):
#    st.write(df)

#option = st.selectbox('Which club is your favorite?', df['Club'].unique())
#st.write('You selected >>', option)

'''
# Club and Nationality Viewing Application
### This is a demo
'''

df = st.cache_data(pd.read_csv)("football_data.csv")

clubs = st.sidebar.multiselect('Show the Players for the club', df['Club'].unique())

countries = st.sidebar.multiselect('Show Player from countries', df['Nationality'].unique())

new_df = df[(df['Club'].isin(clubs)) & (df['Nationality'].isin(countries))]

st.write(new_df)

fig = px.scatter(new_df, x='Overall', y = 'Age', color='Name')

'''
### Here is the result displayed in a chart
'''
st.plotly_chart(fig)