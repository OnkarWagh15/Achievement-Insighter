import streamlit as st
import subprocess
from PIL import Image


image = Image.open('background.jpg')

st.image(image, caption='Achievement Insighter')

def run_another_file(option,start,end):
    subprocess.run(["python", "Scrapper.py",option,start,end])
    if option== '1':
        file="1st_sem/1st.csv"
    elif option== '2':
        file="2nd_sem/2nd.csv"
    elif option== '3':
        file="3rd_sem/3rd.csv"
    elif option== '4':
        file="4th_sem/4th.csv"
    elif option== '5':
        file="5th_sem/5th.csv"
    else:
        file="6th_sem/6th.csv"
    subprocess.Popen(["streamlit", "run", "displayRecords.py", "--", file])



def main():
    st.subheader("Hello! I can help you with Result Analysis")
    st.write("Please enter the details below ")
    option = st.selectbox(
    ' \nSelect Semester',
    ('1', '2', '3', '4', '5','6'))
    start = st.text_input("Enter start Seat number ")
    end = st.text_input("Enter  end Seat number ")
    
    
    if st.button("Proceed"):
        run_another_file(option,start,end)
        
if __name__ == "__main__":
    main()