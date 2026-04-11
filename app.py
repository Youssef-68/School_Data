# Student Performance Dashboard
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Set page configuration
st.set_page_config(page_title="Student Dashboard", layout="wide")
file_path = Path("education_cleaned.csv")
df = pd.read_csv(file_path)
st.title("Student Performance Dashboard")

@st.cache_data
def load_data():
    return pd.read_csv(file_path)

df = load_data()
st.markdown("""
Welcome to the dashboard.  
Use the sidebar to navigate between pages.
""")

# Summary Metrics
st.divider()
col1, col2, col3 = st.columns(3)
col1.metric("Total Students", len(df))
col2.metric("Average Score", round(df["Average_Score"].mean(), 2))
col3.metric("Average Age", round(df["Student_Age"].mean(), 2))
st.divider()

# Charts Row 1
c1, c2 = st.columns(2)

with c1:
    st.subheader("Score Distribution")
    fig1, ax1 = plt.subplots()
    ax1.hist(df["Average_Score"], bins=20)
    ax1.set_xlabel("Score")
    ax1.set_ylabel("Students")
    st.pyplot(fig1)

with c2:
    st.subheader("Age Distribution")
    fig2, ax2 = plt.subplots()
    ax2.hist(df["Student_Age"], bins=20)
    ax2.set_xlabel("Age")
    ax2.set_ylabel("Students")
    st.pyplot(fig2)

st.divider()
