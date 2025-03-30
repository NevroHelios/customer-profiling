import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_icon=":shark:", page_title="Customer Prodiling", layout='wide')

# with st.sidebar:
url = "https://wallpapers.com/images/hd/bocchi-the-rock-surprised-reaction-uf98jl11d34v5h6c.jpg"
st.image(url, width=200)
st.title("Customer Profiling")

