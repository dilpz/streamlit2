import streamlit as st
import pandas as pd
import os

# Function to save data to Excel
def save_to_excel(data, filename="rsvp_data.xlsx"):
    if not os.path.isfile(filename):
        # Create a new Excel file and add data
        df = pd.DataFrame(data, columns=["Name", "Attending", "Number of Guests"])
        df.to_excel(filename, index=False)
    else:
        # Append data to existing Excel file
        df = pd.DataFrame(data, columns=["Name", "Attending", "Number of Guests"])
        with pd.ExcelWriter(filename, mode='a', engine='openpyxl') as writer:
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
