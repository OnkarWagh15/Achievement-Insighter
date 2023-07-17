# importing required libraries
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import csv
import sys



def cm1i(start, end):
    
    seat = ""
    total = ""
    remarks = ""
    percentage = ""
    subjects = ["ENGLISH", "BASIC SCIENCE", "BASIC MATHEMATICS", "FUNDAMENTALS OF ICT", "ENGINEERING GRAPHICS",
                "WORKSHOP PRACTICE"]
    marks = []
    short_sub = ["ENG", "BSC", "BMS", "ICT", "EEC", "WPC"]
    headers = ['Enrollment no.', 'Seat no', 'Name']
    # for headers of CSV file
    for subject in short_sub:
        if subject == "ENG" or subject == "BSC":
            headers.append(subject + "(TH)")
            headers.append(subject + "(PR)")
        elif subject == "BMS":
            headers.append(subject + "(TH)")
        else:
            headers.append(subject + "(PR)")

    final_header = headers + ['total marks', 'percentage', 'remarks']
    # importing the CSV file
    with open("C:/Users/hp/Desktop/Result_Fetcher/MSBTE_Result_Fetcher/1st_sem/1st.csv", 'w', newline='') as f:   
        w = csv.writer(f)
        w.writerow(final_header)
    for i in range(start, end):
        if i == 138744:
            continue
        filename = "C:/Users/hp/Desktop/Result_Fetcher/MSBTE_Result_Fetcher/1st_sem/" + str(i) + ".aspx.html"
        try:
            f = open(filename, 'rb')
            file_content = f.read()
            f.close()
        except FileNotFoundError:
             return -1
        soup = BeautifulSoup(file_content, 'html.parser')
        enrollment = soup.find('strong', string="ENROLLMENT NO.").find_next('td').text
        marks.append(enrollment)
        seat = soup.find('td', string="SEAT NO.").find_next('td').text
        marks.append(seat)
        name = soup.find('strong', string="MR. / MS.").find_next('td').text
        marks.append(name)
        for subject in subjects:
            var = soup.find('td', string=subject)
            if var is not None:
                # print(var.text)
                for i in range(36):
                    if subject in ["ENGLISH", "BASIC SCIENCE"]:
                        if i == 7:
                            marks.append(var.text)
                        if i == 25:
                            marks.append(var.text)
                        var = var.find_next('td')
                    else:
                        if i == 7:
                            marks.append(var.text)
                        var = var.find_next('td')

        total = soup.find_all('table')[2].find_all('tr')[1].find_all('td')[2].text
        percentage = soup.find_all('table')[2].find_all('tr')[1].find_all('td')[1].text
        remarks = soup.find_all('table')[2].find_all('tr')[2].find_all('td')[1].text

        marks.append(total)
        if percentage=='':
            percentage=0
        marks.append(percentage)
        marks.append(remarks)

        with open("C:/Users/hp/Desktop/Result_Fetcher/MSBTE_Result_Fetcher/1st_sem/1st.csv", 'a', newline='') as f:
            w = csv.writer(f)
            w.writerow(marks)
        f.close()
        del marks[:]
    print("Done")


def cm3i(start, end):
    seat = ""
    total = ""
    remarks = ""
    percentage = ""
    subjects = ['OBJECT ORIENTED PROGRAMMING USING C++', "DATA STRUCTURE USING  ‘C’", 'COMPUTER GRAPHICS',
                'DATABASE MANAGEMENT SYSTEM', 'DIGITAL TECHNIQUES']
    marks = []
    short_sub = ['OOP', 'DSU', 'CGR', 'DBMS', 'DT']
    headers = ['Enrollment no.', 'Seat no', 'Name']
    # for headers of CSV file
    for subject in short_sub:
        headers.append(subject + "(TH)")
        headers.append(subject + "(PR)")

    final_header = headers + ['total marks', 'percentage', 'remarks']
    # importing the CSV file
    with open("C:/Users/hp/Desktop/Result_Fetcher/MSBTE_Result_Fetcher/3rd_sem/3rd.csv", 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(final_header)
    for i in range(start, end):
        if i == 138744:
            continue
        filename = "C:/Users/hp/Desktop/Result_Fetcher/MSBTE_Result_Fetcher/3rd_sem/" + str(i) + ".aspx.html"
        try:
            f = open(filename, 'rb')
            file_content = f.read()
            f.close()
        except FileNotFoundError:
            return -1
            
        soup = BeautifulSoup(file_content, 'html.parser')
        enrollment = soup.find('strong', string="ENROLLMENT NO.").find_next('td').text
        marks.append(enrollment)
        seat = soup.find('td', string="SEAT NO.").find_next('td').text
        marks.append(seat)
        name = soup.find('strong', string="MR. / MS.").find_next('td').text
        marks.append(name)
        for subject in subjects:
            var = soup.find('td', string=subject)
            if var is not None:
                # print(var.text)
                for i in range(36):
                    if subject in ['OBJECT ORIENTED PROGRAMMING USING C++', "DATA STRUCTURE USING  ‘C’",
                                   'COMPUTER GRAPHICS', 'DATABASE MANAGEMENT SYSTEM', 'DIGITAL TECHNIQUES']:
                        if i == 7:
                            marks.append(var.text)
                        if i == 25:
                            marks.append(var.text)
                        var = var.find_next('td')
                    else:
                        if i == 7:
                            marks.append(var.text)
                        var = var.find_next('td')

        total = soup.find_all('table')[2].find_all('tr')[1].find_all('td')[2].text
        percentage = soup.find_all('table')[2].find_all('tr')[1].find_all('td')[1].text
        remarks = soup.find_all('table')[2].find_all('tr')[2].find_all('td')[1].text

        marks.append(total)
        if percentage=='':
            percentage=0
        marks.append(percentage)
        marks.append(remarks)

        with open("C:/Users/hp/Desktop/Result_Fetcher/MSBTE_Result_Fetcher/3rd_sem/3rd.csv", 'a', newline='') as f:
            w = csv.writer(f)
            w.writerow(marks)
        f.close()
        del marks[:]
    print("Done")



def cm5i(start, end):
    seat = ""
    total = ""
    remarks = ""
    percentage = ""
    subjects = ["ENVIRONMENTAL STUDIES", "OPERATING SYSTEMS", "ADVANCED JAVA PROGRAMMING", "SOFTWARE TESTING",
                "ADVANCED COMPUTER NETWORK", "INDUSTRIAL TRAINING", "CAPSTONE PROJECT PLANNING"]
    marks = []
    short_sub = ["EST", "OSY", "AJP", "STE", "ACN", "ITR", "CPP"]
    headers = ['Enrollment no.', 'Seat no', 'Name']
    # for headers of CSV file
    for subject in short_sub:
        if subject == "OSY" or subject == "AJP" or subject == "STE" or subject == "ACN":
            headers.append(subject + "(TH)")
            headers.append(subject + "(PR)")
        elif subject == "EST":
            headers.append(subject + "(TH)")
        else:
            headers.append(subject + "(PR)")

    final_header = headers + ['total marks', 'percentage', 'remarks']
    # importing the CSV file
    with open("C:/Users/hp/Desktop/Result_Fetcher/MSBTE_Result_Fetcher/5th_sem/5th.csv", 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(final_header)
    for i in range(start, end):
        if i == 138744:
            continue
        filename =  "C:/Users/hp/Desktop/Result_Fetcher/MSBTE_Result_Fetcher/5th_sem/" + str(i) + ".aspx.html"
        try:
            f = open(filename, 'rb')
            file_content = f.read()
            f.close()
        except FileNotFoundError:
            return -1
        soup = BeautifulSoup(file_content, 'html.parser')
        enrollment = soup.find('strong', string="ENROLLMENT NO.").find_next('td').text
        marks.append(enrollment)
        seat = soup.find('td', string="SEAT NO.").find_next('td').text
        marks.append(seat)
        name = soup.find('strong', string="MR. / MS.").find_next('td').text
        marks.append(name)
        for subject in subjects:
            var = soup.find('td', string=subject)
            if var is not None:
                # print(var.text)
                for i in range(36):
                    if subject in ["OPERATING SYSTEMS", "ADVANCED JAVA PROGRAMMING", "SOFTWARE TESTING",
                                   "ADVANCED COMPUTER NETWORK"]:
                        if i == 7:
                            marks.append(var.text)
                        if i == 25:
                            marks.append(var.text)
                        var = var.find_next('td')
                    else:
                        if i == 7:
                            marks.append(var.text)
                        var = var.find_next('td')

        total = soup.find_all('table')[2].find_all('tr')[1].find_all('td')[2].text
        percentage = soup.find_all('table')[2].find_all('tr')[1].find_all('td')[1].text
        remarks = soup.find_all('table')[2].find_all('tr')[2].find_all('td')[1].text

        marks.append(total)
        if percentage=='':
            percentage=0
        marks.append(percentage)
        marks.append(remarks)

        with open("C:/Users/hp/Desktop/Result_Fetcher/MSBTE_Result_Fetcher/5th_sem/5th.csv", 'a', newline='') as f:
            w = csv.writer(f)
            w.writerow(marks)
        f.close()
        del marks[:]
    # st.write("Done")



sem=int(sys.argv[1])
start=int(sys.argv[2])
end=int(sys.argv[3])
if sem == 1:
   
    cm1i(start, end)
# if sem == 2:
if sem == 3:
    cm3i(start, end)
# if sem == 4:
if sem == 5:
    cm5i(start, end)
# if sem == 6:

