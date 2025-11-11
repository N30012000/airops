import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.express as px

st.set_page_config(page_title="AirOps Pro", page_icon="🛫", layout="wide")

# Sidebar
with st.sidebar:
    st.markdown("# 🛫 AirOps Pro")
    st.markdown("**Aviation Operations Platform**")
    
    airlines = {
        "PIA": "Pakistan International Airlines",
        "AIRBLUE": "AirBlue",
        "SEREAIR": "SereneAir"
    }
    
    selected_airline = st.selectbox("Select Airline:", list(airlines.keys()))
    airline_name = airlines[selected_airline]
    
    page = st.radio("Navigation:", 
        ["Dashboard", "Flights", "Maintenance", "Revenue", "Reports", "AI Insights", "Data Entry"])

# Dashboard Page
if page == "Dashboard":
    st.header(f"🛫 {airline_name}")
    st.subheader("Operational Dashboard")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("On-Time Percent", "87.3", "+2.1")
    with col2:
        st.metric("Fleet Util", "78.9", "+3.2")
    with col3:
        st.metric("Delays 30d", "156", "-12")
    with col4:
        st.metric("Revenue M", "12.4", "+0.45")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        dates = pd.date_range(end=datetime.now(), periods=30)
        otp_data = pd.DataFrame({
            "Date": dates,
            "On-Time": np.clip(np.random.normal(87, 3, 30), 75, 95)
        })
        
        fig = px.area(otp_data, x="Date", y="On-Time", 
                     title="On-Time Performance 30 Days",
                     color_discrete_sequence=["#1E3A5F"])
        fig.update_layout(height=400, template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fleet_data = pd.DataFrame({
            "Aircraft": ["Boeing 777", "Airbus A320", "ATR 72", "Boeing 737"],
            "Utilization": [82, 79, 75, 81]
        })
        
        fig = px.bar(fleet_data, x="Aircraft", y="Utilization",
                    title="Fleet Utilization by Type",
                    color_discrete_sequence=["#1E3A5F"])
        fig.update_layout(height=400, template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    st.subheader("Recent Alerts")
    
    alerts = [
        ("Critical", "Aircraft N-4567 requires maintenance", "2 hours ago"),
        ("Warning", "Flight delayed by 1h 15min due to weather", "1 hour ago"),
        ("Notice", "Crew scheduling optimization recommended", "30 min ago"),
        ("Info", "On-time performance exceeded target", "10 min ago"),
    ]
    
    for severity, message, time in alerts:
        col1, col2, col3 = st.columns([0.5, 3, 1])
        with col1:
            st.write(severity)
        with col2:
            st.write(message)
        with col3:
            st.caption(time)

# Flights Page
elif page == "Flights":
    st.header("Aircraft Flight Operations")
    
    tab1, tab2, tab3 = st.tabs(["Live Flights", "Routes", "Delays"])
    
    with tab1:
        flights_data = pd.DataFrame({
            "Flight": ["PK-001", "PK-002", "PK-003", "PK-004", "PK-005"],
            "Route": ["KHI-ISB", "KHI-LHE", "ISB-KHI", "LHE-KHI", "KHI-DXB"],
            "Aircraft": ["A320", "B777", "A320", "B737", "A320"],
            "Scheduled": ["06:00", "07:30", "08:15", "09:00", "10:30"],
            "Status": ["Departed", "On Time", "Delayed", "Cancelled", "Scheduled"],
        })
        st.dataframe(flights_data, use_container_width=True, hide_index=True)
    
    with tab2:
        routes_data = pd.DataFrame({
            "Route": ["KHI-ISB", "KHI-LHE", "ISB-KHI", "LHE-KHI", "KHI-DXB"],
            "Flights": [89, 76, 85, 72, 48],
            "OnTime": [88.8, 85.5, 87.2, 86.1, 91.7],
            "Avg Delay": [12, 18, 14, 16, 8],
        })
        st.dataframe(routes_data, use_container_width=True, hide_index=True)
    
    with tab3:
        delay_data = pd.DataFrame({
            "Cause": ["Weather", "Mechanical", "Crew", "ATC",
