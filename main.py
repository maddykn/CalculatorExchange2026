#source "/Users/madeline.novak/Library/CloudStorage/GoogleDrive-madeline.novak@cis.dk/My Drive/2. Newly Organized Folder/Math Department (Meeting Notes and Other Docs)/Calculator Exchange/CalculatorExchangeApplication/.venv/bin/activate"

import gspread
from google.oauth2.service_account import Credentials
import streamlit as st

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=SCOPES
)

client = gspread.authorize(creds)

sheet = client.open("Calculators for Sale (May 2026) (Responses)").sheet1

records = (sheet.get_all_records()) #list(dict)
#individual item records[index][key] fx: records[0]["Your Name"]
#print(records)

for d in records:
    age = d["Age"]
    cable = d["Charging Cable"] 
    if age == "Purchased new in Grade 11 or 12 (1-2 years old)":
        price = 700
    elif age == "Purchased new in Grade 9 or 10 (3-4 years old)":
        price = 500
    else:
        price = 300
    
    if cable == "Yes":
        price = price + 60
    
    d["Price"] = price
    print(d)

st.title("Calculator Exchange")
st.write("Please reach out to students who are looking to sell their calculators")
st.write("Note, we don't recommend buying calculators previously purchased used unless you know for certain your student will not be here after Grade 10")

col1, col2, col3, col4, col5 = st.columns([0.20, 0.30, 0.25, 0.10, 0.15])

with col1:
    st.markdown(
        "<p style='font-size:12px; font-weight:bold;'>Name of Student</p>",
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        "<p style='font-size:12px; font-weight:bold;'>Contact</p>",
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        "<p style='font-size:12px; font-weight:bold;'>Condition</p>",
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        "<p style='font-size:12px; font-weight:bold;'>Price</p>",
        unsafe_allow_html=True
    )

with col5:
    st.markdown(
        "<p style='font-size:12px; font-weight:bold;'>Status</p>",
        unsafe_allow_html=True
    )

for d in records:
    if d['Status'] == "Available":
        with col1:
            st.markdown(
                f"<p style='font-size:14px;'>{d['Name']}</p>",
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                f"<p style='font-size:14px;'>{d['Contact']}</p>",
                unsafe_allow_html=True
            )

        with col3:
            st.markdown(
                f"<p style='font-size:14px;'>{d['Age'][d['Age'].find('('):]}</p>",
                unsafe_allow_html=True
            )

        with col4:
            st.markdown(
                f"<p style='font-size:14px;'>{d['Price']}</p>",
                unsafe_allow_html=True
            )
    
        with col5:
            st.markdown(
                f"<p style='font-size:14px;'>{d['Status']}</p>",
                unsafe_allow_html=True
         )



