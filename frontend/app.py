import streamlit as st
import requests

backend_url = "https://ai-booking-insights.onrender.com"

st.title("Hotel Booking Analytics & QA System")

st.sidebar.header("Analytics")
if st.sidebar.button("Show Revenue Trends"):
    response = requests.post(f"{backend_url}/analytics")
    st.write(response.json().get("revenue_trends", {}))

query = st.text_input("Enter your question:")
if st.button("Get Answer"):
    response = requests.post(f"{backend_url}/ask", json={"query": query})
    st.write("LLM Response:", response.json().get("llm_response", "No response"))
