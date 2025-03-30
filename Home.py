import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_icon=":shark:", page_title="Customer Prodiling", layout='wide')

# with st.sidebar:
url = "https://wallpapers.com/images/hd/bocchi-the-rock-surprised-reaction-uf98jl11d34v5h6c.jpg"
st.image(url, width=200)
st.title("👥 Customer Profiling")
st.write("## 👋 Welcome to Customer Profiling Dashboard")
st.write("This is my first project about Customer Profiling, so have a look!. ✨")
st.write('Use the sidebar to navigate through different analyses and insights. 🧭')

st.markdown("""
### ✅ Features:
- 👤 Customer Demographics Analysis
- 🛒 Purchase Behavior Patterns
- 🔍 Customer Segmentation
- 📈 Sales Trends Visualization

Use the sidebar to navigate through different analyses and insights.
""")

st.info("👈 Select an option from the sidebar to get started!")
