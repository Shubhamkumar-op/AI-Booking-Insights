import streamlit as st
import requests
import pandas as pd
import os

backend_url = "https://ai-booking-insights.onrender.com" 
st.title("Hotel Booking Analytics & QA System")


st.sidebar.header("Analytics")
show_revenue_button = st.sidebar.button("Show Revenue Trends")
show_cancellation_rate_button = st.sidebar.button("Show Cancellation Rate")
show_geo_distribution_button = st.sidebar.button("Show Geo Distribution")
show_booking_lead_time_button = st.sidebar.button("Show Booking Lead Time")

data_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "bookings_data.csv")

if os.path.exists(data_file_path):
    df = pd.read_csv(data_file_path)
    st.write("Dataset Preview:")
    st.write(df.head())  

    if show_revenue_button:
        response = requests.post(f"{backend_url}/analytics/revenue_trends", files={"file": open(data_file_path, 'rb')})
        if response.status_code == 200:
            st.write(response.json().get("revenue_trends", {}))
        else:
            st.error("Failed to fetch revenue trends")

    if show_cancellation_rate_button:
        response = requests.post(f"{backend_url}/analytics/cancellation_rate", files={"file": open(data_file_path, 'rb')})
        if response.status_code == 200:
            st.write(f"Cancellation Rate: {response.json().get('cancellation_rate', 0.0)}%")
        else:
            st.error("Failed to fetch cancellation rate")

    if show_geo_distribution_button:
        response = requests.post(f"{backend_url}/analytics/geo_distribution", files={"file": open(data_file_path, 'rb')})
        if response.status_code == 200:
            st.write(response.json().get("geo_distribution", {}))
        else:
            st.error("Failed to fetch geo distribution")

    if show_booking_lead_time_button:
        response = requests.post(f"{backend_url}/analytics/booking_lead_time", files={"file": open(data_file_path, 'rb')})
        if response.status_code == 200:
            st.write(response.json().get("booking_lead_time", {}))
        else:
            st.error("Failed to fetch booking lead time")
else:
    st.error("Data file not found in the 'data' folder")

query = st.text_input("Enter your question:")
if st.button("Get Answer"):
    response = requests.post(f"{backend_url}/ask", json={"query": query})
    if response.status_code == 200:
        st.write("LLM Response:", response.json().get("llm_response", "No response"))
    else:
        st.error("Failed to get response from the model")


