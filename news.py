import streamlit as st
import pandas as pd

# Load the data
data = pd.read_csv("news.csv")

# Create a list of unique countries for the dropdown menu
countries = data["Country"].unique()

# Create a date range slider
min_date = pd.to_datetime(data["Date"]).min().date()
max_date = pd.to_datetime(data["Date"]).max().date()
start_date = st.date_input("Start date", min_date)
end_date = st.date_input("End date", max_date)

# Filter the data by country and date range
selected_country = st.selectbox("Select a country", countries)
filtered_data = data[(data["Country"] == selected_country) & (pd.to_datetime(data["Date"]).dt.date >= start_date) & (pd.to_datetime(data["Date"]).dt.date <= end_date)]

# Display the filtered data
st.table(filtered_data[["Country", "News", "Date"]])
