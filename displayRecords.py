import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import sys




st.set_page_config(page_title='Analysis', layout="wide")
st.header(':blue[MSBTE] | :blue[Semester Results]' )
st.subheader('Format: Marks-Total-Percentange-Class')
st.subheader('------------------------')
df=pd.read_csv(sys.argv[1])
totalStudents=df.shape[0]
st.write('Total Number of Records:',totalStudents)

def color_value(val, threshold):
    global countOfFail
    global countOfPerformers
    countOfFail=countOfPerformers=0
    if val < threshold: 
        color='red'
        countOfFail +=1
    elif val > 86: 
        color='green'
        countOfPerformers +=1    
    else: color=''
    return f'background-color: {color}'
st.dataframe(df.style.applymap(color_value, subset=['percentage'], threshold=40, ))


def header(url):
    st.markdown(f'<p style="background-color:#0066cc;color:#33ff33;font-size:24px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)

col1, col2= st.columns(2,gap="large")
with col1:
    df_score=pd.read_csv(sys.argv[1])
    pieChart= px.pie(df_score,
                    title='Variance in Score',
                    values='total marks',
                    names='percentage')
    st.plotly_chart(pieChart)
with col2:
    st.text(" ") 
    st.text(" ") 
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ") 
    st.text(" ") 
    if st.button('Percentange Range and Class Awarded:', key=None, help=None, on_click=None,args=None, kwargs=None,use_container_width=True) is True:
        st.write('Percentage Range: 85-100 : First Class With Distinction')
        st.write('Percentage Range: 70-85 : First Class')
        st.write('Percentage Range: 40-75 : First Class Con')
        st.write('Percentage Range: 1-40 : ATKT/Fail')



st.text("Want to download the result sheet? \nClick of below download button: File will be downloaded in csv format \t \t ")
@st.cache_data
def convert_df(df):
    return df.to_csv().encode('utf-8')

csv = convert_df(df)

st.download_button(
    label="Download",
    data=csv,
    file_name='Semester_Result.csv',
    mime='text/csv',
)
