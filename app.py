import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide", page_title="SolarGuardian 2.0")

st.title("🔆 SolarGuardian 2.0 - Real-Time Solar Monitoring")

# Load data
try:
    df = pd.read_csv("data/realtime_data.csv")

    # Show latest data
    st.subheader("📊 Latest 10 Entries")
    st.dataframe(df.tail(10))

    # Plot
    fig = px.line(df.tail(100), x="timestamp", y="energy_generated", title="Energy Generated Over Time")
    st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.error("⚠️ Error loading data. Make sure `data/realtime_data.csv` exists.")
