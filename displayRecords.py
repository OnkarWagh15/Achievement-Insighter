from streamlit import session_state as session
import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import subprocess
import sys
import os

st.set_page_config(page_title='Analysis', layout="wide")

#Read csv file
df=pd.read_csv(sys.argv[1]) 

#Links to Categorize students page
def run_another_file(file):
    subprocess.Popen(["streamlit", "run", "categorizeStudents.py", "--", file])


col1, col2, col3 = st.columns(3)
with col1:
    st.header(':blue[MSBTE] | :blue[Semester Results]' )
    st.subheader('------------------------')
with col3:
    if st.button("Categorize and Analyse Students"):
        file=sys.argv[1]
        run_another_file(file)
        

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
    for i in range (1,5):
        st.text(" ") 
    if st.button('Percentange Range and Class Awarded:', key=None, help=None, on_click=None,args=None, kwargs=None,use_container_width=True) is True:
        st.write('Percentage Range: 75-100 : First Class With Distinction')
        st.write('Percentage Range: 60-75 : First Class')
        st.write('Percentage Range: 45-60 : Second Class')
        st.write('Percentage Range: 40-45 : Pass')
        st.write('Percentage Range: 0-40 : ATKT/Fail')


col3, col4= st.columns(2,gap="large")
with col3:
    st.text("Want to download the result sheet? \nClick of below download button: File will be downloaded in csv format \t \t ")
    @st.cache_data
    def convert_df(df):
        return df.to_csv().encode('utf-8')
    csv = convert_df(df)
    st.download_button(
        label="Download",
        data=csv,
        file_name='Semester_Result.csv',
        mime='text/csv',)

with col4:
    st.text("Want to download the Marksheet of a particular student? \n\t \t ")
    filename = st.text_input("Enter the filename (including the extension (seatno.aspx.html)): ")
    if sys.argv[1][0] == '1':
        folder_path = "C:/Users/hp/Desktop/Result_Fetcher/MSBTE_Result_Fetcher/1st_sem/"
    elif sys.argv[1][0] == '2':
        folder_path = "C:/Users/hp/Desktop/Result_Fetcher/MSBTE_Result_Fetcher/2nd_sem/"
    elif sys.argv[1][0] == '3':
        folder_path = "C:/Users/hp/Desktop/Result_Fetcher/MSBTE_Result_Fetcher/3rd_sem/"
    elif sys.argv[1][0] == '4':
        folder_path = "C:/Users/hp/Desktop/Result_Fetcher/MSBTE_Result_Fetcher/4th_sem/"
    elif sys.argv[1][0] == '5':
        folder_path = "C:/Users/hp/Desktop/Result_Fetcher/MSBTE_Result_Fetcher/5th_sem/"
    else:
        folder_path = "C:/Users/hp/Desktop/Result_Fetcher/MSBTE_Result_Fetcher/6th_sem/"
    file_path = os.path.join(folder_path, filename)
    if st.button("Check Availability ?"):
        try:
            with open(file_path, "rb") as file:
                file_content = file.read()
            st.write("The Marksheet is Availble, Click on download to Download Marksheet")
            st.download_button(label="Download", data=file_content, file_name=filename)
        except FileNotFoundError:
            st.error("File not found.")





