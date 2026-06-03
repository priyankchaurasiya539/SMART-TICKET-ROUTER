import streamlit as st
import requests

st.title("Smart Ticket Router UI")
user_input = st.text_area("Enter your support description here ")

if st.button("Route Ticket"):
    url = "http://127.0.0.1:8000/predict"
    data = {
        "ticket_text" : user_input
    }
    response = requests.post(url , json=data)
    result = response.json() 
    dept = result["department"]
    priority = result["priority"]
    st.success(f"Rooted to department : {dept}")
    st.success(f"Assigned Priority : {priority}")