import streamlit as st
import pandas as pd
from openpyxl import Workbook
import os

# Function to save data to Excel
def save_to_excel(data, filename="rsvp_data.xlsx"):
    if not os.path.isfile(filename):
        # Create a new workbook and add data
        workbook = Workbook()
        sheet = workbook.active
        sheet.append(["Name", "Attending", "Number of Guests"])
        for item in data:
            sheet.append(item)
        workbook.save(filename)
    else:
        # Append data to existing workbook
        with pd.ExcelWriter(filename, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
            df = pd.DataFrame(data, columns=["Name", "Attending",
            "Number of Guests"])
            df.to_excel(writer, sheet_name="RSVP", index=False)

# Streamlit UI
st.title("Wedding RSVP")
st.subheader("Please fill in your details:")

# User input fields
name = st.text_input("Name")
attending = st.selectbox("Will you be attending?", ["Yes", "No"])
num_guests = st.number_input("Number of guests", min_value=0)

# Button to submit response
if st.button("Submit"):
    data = [[name, attending, num_guests]]
    save_to_excel(data)
    st.success("Thank you for your response!")

# Displaying the Excel file content (optional)
if st.checkbox("Show RSVP data"):
    if os.path.isfile("rsvp_data.xlsx"):
        df = pd.read_excel("rsvp_data.xlsx")
        st.write(df)
    else:
        st.write("No data available yet.")
