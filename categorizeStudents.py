from streamlit import session_state as session
import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import sys
import os
import base64

st.set_page_config(page_title='Analysis', layout="wide")
col1, col2, col3 = st.columns(3)


with col2:
    st.header(':blue[Categorize Students]' )
    st.subheader('------------------------------------')
    
df=pd.read_csv(sys.argv[1])

RangeOfMarks = st.slider(
    "Select a Range of Percentage:",
    value=(0,100))
st.write("You've Selected Range:", RangeOfMarks)

if 0 <= RangeOfMarks[1] < 40:
    st.header("Displaying Records of Students applicable for Re-examination")
elif 40 <= RangeOfMarks[1] < 65:
    st.header("Displaying Records of Students that require attention")
elif 65 <= RangeOfMarks[1] < 86:
    st.header("Displaying Records of Students that have scored well")
else:
    st.header("Displaying Records of Students that have scored the highest")

condition = (df['percentage'] >= RangeOfMarks[0] ) & (df['percentage'] <= RangeOfMarks[1])
filtered_data = df[condition]
st.dataframe(filtered_data)

col1, col2, col3 = st.columns(3)
with col2:
    for i in range(0,6):
        st.write(" ")
    st.subheader("We have categorized data for you !")
    st.write("Download list of students? ")
    option = st.selectbox(
    ' \nSelect Category of Students',
    ('1] 75-100 : First Class With Distinction', '2] 60-75 : First Class', '3] 45-60 : Second Class', '4] 40-45 : Pass', '5] 0-40 : ATKT/Fail'))
    st.write('You selected:\n', option)
    
    if option[0] == '1':
        condition = ((df['percentage'] >= 75) & (df['percentage'] < 100))
        filtered_df = df[condition]
    elif option[0] == '2':
        condition = ((df['percentage'] >= 60) & (df['percentage'] < 75))
        filtered_df = df[condition]
    elif option[0] == '3':
        condition = ((df['percentage'] >= 45) & (df['percentage'] < 60))
        filtered_df = df[condition]
    elif option[0] == '4':
        condition = ((df['percentage'] >= 40) & (df['percentage'] < 45))
        filtered_df = df[condition]
    else:
        condition = ((df['percentage'] >= 0) & (df['percentage'] < 40))
        filtered_df = df[condition]

    filtered_df.to_csv('category.csv', index=False)
    csv_data = open('category.csv', 'rb').read()
    st.download_button(
        label="Download",
        data=csv_data,
        file_name='Category.csv',
        mime='text/csv'
    )