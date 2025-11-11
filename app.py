import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go

# Page config
st.set_page_config(
    page_title="AirOps Pro",
    page_icon="🛫",
    layout="wide"
)

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
    
    page = st.radio(
        "Navigation:",
        ["Dashboard", "Flights", "Maintenance", "Revenue", "Reports", "AI Insights", "Data Entry"]
    )

# Main content based on page
if page == "Dashboard":
    st.header(f"🛫 {airline_name}")
    st.subheader("Operational Dashboard")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("On-Time %", "87.3%", "+2.1%")
    with col2:
        st.metric("Fleet Util.", "78.9%", "+3.2%")
    with col3:
        st.metric("Delays (30d)", "156", "-12")
    with col4:
        st.metric("Revenue ($M)", "$12.4", "+$0.45")
    
    st.markdown("---")
    
    # Chart 1: On-Time Performance
    col1, col2 = st.columns(2)
    
    with col1:
        dates = pd.date_range(end=datetime.now(), periods=30)
        otp_data = pd.DataFrame({
            "Date": dates,
            "On-Time %": np.clip(np.random.normal(87, 3, 30), 75, 95)
        })
        
        fig = px.area(
            otp_data,
            x="Date",
            y="On-Time %",
            title="📊 On-Time Performance Trend (30 Days)",
            color_discrete_sequence=["#1E3A5F"]
        )
        fig.update_layout(hovermode="x unified", height=400, template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fleet_data = pd.DataFrame({
            "Aircraft": ["Boeing 777", "Airbus A320", "ATR 72", "Boeing 737"],
            "Utilization %": [82, 79, 75, 81]
        })
        
        fig = px.bar(
            fleet_data,
            x="Aircraft",
            y="Utilization %",
            title="✈️ Fleet Utilization by Type",
            color_discrete_sequence=["#1E3A5F"]
        )
        fig.update_layout(height=400, template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Alerts
    st.subheader("🚨 Recent Alerts")
    alerts = [
        ("🔴 Critical", "Aircraft N-4567 requires maintenance", "2 hours ago"),
        ("🟠 Warning", "Flight delayed by 1h 15min due to weather", "1 hour ago"),
        ("🟡 Notice", "Crew scheduling optimization recommended", "30 min ago"),
        ("🟢 Info", "On-time performance exceeded target", "10 min ago"),
    ]
    
    for severity, message, time in alerts:
        col1, col2, col3 = st.columns([0.5, 3, 1])
        with col1:
            st.write(severity)
        with col2:
            st.write(message)
        with col3:
            st.caption(time)

elif page == "Flights":
    st.header("✈️ Flight Operations")
    
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
            "Flights (30d)": [89, 76, 85, 72, 48],
            "On-Time %": [88.8, 85.5, 87.2, 86.1, 91.7],
            "Avg Delay (min)": [12, 18, 14, 16, 8],
        })
        st.dataframe(routes_data, use_container_width=True, hide_index=True)
    
    with tab3:
        delay_data = pd.DataFrame({
            "Cause": ["Weather", "Mechanical", "Crew", "ATC", "Other"],
            "Count": [45, 28, 15, 12, 8]
        })
        fig = px.pie(delay_data, values="Count", names="Cause", title="⚠️ Delays by Cause")
        st.plotly_chart(fig, use_container_width=True)

elif page == "Maintenance":
    st.header("🔧 Maintenance Management")
    
    tab1, tab2, tab3 = st.tabs(["Scheduled", "Alerts", "Predictive"])
    
    with tab1:
        maint_data = pd.DataFrame({
            "Aircraft": ["N-1001", "N-1002", "N-1003", "N-1004"],
            "Type": ["C-Check", "A-Check", "Heavy Maint.", "B-Check"],
            "Next Due": ["2024-02-15", "2024-01-28", "2024-03-10", "2024-02-05"],
            "Duration (h)": [48, 12, 200, 24],
        })
        st.dataframe(maint_data, use_container_width=True, hide_index=True)
    
    with tab2:
        st.error("🔴 N-4567: Engine vibration exceeds threshold - Immediate action required")
        st.warning("🟠 N-2345: Hydraulic system pressure irregular - Schedule within 48h")
        st.info("🟡 N-3456: Cabin pressure fluctuation - Review during next check")
    
    with tab3:
        pred_data = pd.DataFrame({
            "Aircraft": ["N-1001", "N-1002", "N-1003", "N-1004"],
            "Component": ["Engine 1", "Landing Gear", "Hydraulic", "APU"],
            "Health Score": [78, 92, 65, 88],
            "Est. Life (h)": [450, 1200, 180, 2000],
        })
        st.dataframe(pred_data, use_container_width=True, hide_index=True)

elif page == "Revenue":
    st.header("💰 Revenue Management")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Monthly Revenue", "$12.4M", "+$450K")
    with col2:
        st.metric("RASK", "$0.082", "-$0.002")
    with col3:
        st.metric("Load Factor", "82.1%", "+2.3%")
    with col4:
        st.metric("Yield/Pax", "$145", "+$8")
    
    st.markdown("---")
    
    revenue_data = pd.DataFrame({
        "Route": ["KHI-ISB", "KHI-LHE", "ISB-KHI", "LHE-KHI", "KHI-DXB"],
        "Current Price": ["$120", "$95", "$115", "$90", "$280"],
        "Recommended": ["$125", "$100", "$118", "$95", "$290"],
        "Revenue Impact": ["+$2.1K", "+$1.8K", "+$2.5K", "+$1.2K", "+$3.5K"]
    })
    st.dataframe(revenue_data, use_container_width=True, hide_index=True)

elif page == "Reports":
    st.header("📋 Report Generation")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("📊 Weekly Report"):
            st.success("✅ Report generated! Ready to download.")
    with col2:
        if st.button("📈 Monthly Report"):
            st.success("✅ Report generated! Ready to download.")
    with col3:
        if st.button("📑 Annual Report"):
            st.success("✅ Report generated! Ready to download.")
    
    st.markdown("---")
    st.subheader("Report Sections")
    sections = [
        "Executive Summary",
        "Flight Performance",
        "Maintenance Overview",
        "Revenue Analysis",
        "Cost Optimization",
        "Key Issues & Recommendations"
    ]
    for i, section in enumerate(sections, 1):
        st.write(f"{i}. {section}")

elif page == "AI Insights":
    st.header("🤖 AI-Powered Insights")
    
    tab1, tab2, tab3 = st.tabs(["Summary", "Predictions", "Optimization"])
    
    with tab1:
        st.subheader("Executive Summary")
        st.info("""
        **MONTHLY REPORT SUMMARY**
        
        • On-Time Performance: 87.3% (↑ 2.1% vs last month)
        • Fleet Utilization: 78.9% (Optimal range)
        • Maintenance Efficiency: 94.2% (No critical issues)
        • Cost Per Seat: $0.082 (↓ 1.2% improvement)
        • Revenue Per Flight Hour: $2,847 (↑ $145)
        
        **KEY INSIGHTS:**
        ✓ Route optimization improved efficiency by 3.4%
        ⚠ Weather delays increased by 12%
        → Recommend crew scheduling adjustment
        """)
    
    with tab2:
        st.subheader("🔮 Delay Prediction")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Predicted Delay Rate", "12.5%", "confidence: 87%")
        with col2:
            st.metric("High Risk Routes", "2", "KHI-LHE, ISB-DXB")
        with col3:
            st.metric("Top Risk Factor", "Weather", "45% prob")
        
        st.write("**Recommended Actions:**")
        st.write("✓ Increase buffer time for afternoon flights")
        st.write("✓ Pre-position crew for peak hours")
        st.write("✓ Schedule maintenance during low-demand periods")
    
    with tab3:
        st.subheader("💡 Cost Optimization")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Current Monthly Cost", "$4.2M")
        with col2:
            st.metric("Potential Savings", "$280K", "+6.7%")
        
        savings = pd.DataFrame({
            "Area": ["Fuel Efficiency", "Crew Scheduling", "Maintenance", "Operations"],
            "Savings": ["$120K/month", "$85K/month", "$45K/month", "$30K/month"],
            "Action": [
                "Optimize cruise altitudes",
                "Eliminate deadhead flights",
                "Predictive maintenance",
                "Reduce ground time"
            ]
        })
        st.dataframe(savings, use_container_width=True, hide_index=True)

elif page == "Data Entry":
    st.header("📝 Data Entry")
    
    tab1, tab2 = st.tabs(["Flight Data", "Maintenance"])
    
    with tab1:
        st.subheader("Record Flight Actual")
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Flight Number", "PK-001")
            st.time_input("Actual Departure")
            st.selectbox("Aircraft", ["B777", "A320", "B737"])
        with col2:
            st.time_input("Actual Arrival")
            st.selectbox("Route", ["KHI-ISB", "KHI-LHE", "ISB-KHI"])
            st.number_input("Passengers", min_value=0, max_value=400)
        
        if st.button("Submit Flight Data"):
            st.success("✅ Flight data recorded!")
    
    with tab2:
        st.subheader("Record Maintenance")
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Aircraft ID", "N-1001")
            st.selectbox("Maintenance Type", ["A-Check", "C-Check", "Repair"])
            st.text_input("Component", "Engine 1")
        with col2:
            st.number_input("Duration (hours)", min_value=0.0, step=0.5)
            st.selectbox("Status", ["Completed", "In Progress", "Scheduled"])
            st.text_input("Technician ID", "TECH-001")
        
        if st.button("Submit Maintenance"):
            st.success("✅ Maintenance record saved!")

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #888; font-size: 12px'>
    <p>🛫 AirOps Pro v1.0.0 | Enterprise Aviation Operations Platform</p>
    <p>Made for Pakistani Aviation | Designed for Global Impact</p>
</div>
""", unsafe_allow_html=True)
```

4. Click **"Commit changes"** (at bottom)
5. Message: `Create main app`
6. Click **"Commit directly to main branch"**

---

## ✅ STEP 4: Create requirements.txt File

1. Click **"Add file"** → **"Create new file"**
2. Filename: `requirements.txt`
3. Paste this:
```
streamlit==1.28.1
pandas==2.0.3
numpy==1.24.3
plotly==5.17.0
