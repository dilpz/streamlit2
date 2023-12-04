import streamlit as st
import pandas as pd
import os

# Function to save data to CSV
def save_to_csv(data, filename="rsvp.csv"):
    if not os.path.isfile(filename):
        # Create a new CSV file and add data
        df = pd.DataFrame(data, columns=["Name", "Attending", "Number of Guests"])
        df.to_csv(filename, index=False)
    else:
        # Append data to existing CSV file
        df = pd.DataFrame(data, columns=["Name", "Attending", "Number of Guests"])
        df.to_csv(filename, mode='a', index=False, header=False)

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
    save_to_csv(data)
    st.success("Thank you for your response!")

# Displaying the CSV file content (optional)
if st.checkbox("Show RSVP data"):
    if os.path.isfile("rsvp.csv"):
        df = pd.read_csv("rsvp.csv")
        st.write(df)
    else:
        st.write("No data available yet.")
