import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import time

st.set_page_config(page_icon=":shark:", page_title="Customer Prodiling", layout='wide')

with st.sidebar:
    st.write("## 📋 Menu")
    st.write("### 📊 Data Analysis")
    st.write("1. 👥 [Customer Demographics](#customer-demographics-purchase-behavior)")
    st.write("2. 🛒 [Purchase Behavior](#purchase-behavior-analysis)")
    st.write("3. 🚀 [Campaign Response](#campaign-response-analysis)")
    st.write("### 📁 Data")
    st.write("4. 📑 [Data](#data-head)")


# load data
@st.cache_data
def load_data():
    data = pd.read_csv('data/marketing_campaign.csv', sep='	')
    data['Dt_Customer'] = pd.to_datetime(data['Dt_Customer'], format="mixed")
    data.loc[:, 'Age'] = data['Dt_Customer'].dt.year - data['Year_Birth']
    data['Marital_Status'] = data['Marital_Status'].replace(['YOLO', 'Alone', 'Absurd'], 'Single')
    data['Marital_Status'] = data['Marital_Status'].replace(['Widow'], 'Divorced')
    data['Marital_Status'] = data['Marital_Status'].replace(['Together'], 'Married')
    dct = {'Single': 1, 'Married': 2, 'Divorced': 1}
    parent_count = data['Marital_Status'].map(dct)
    kiddos_home = data['Kidhome'] + data['Teenhome']
    data['Family_Size'] = parent_count + kiddos_home
    purchase_types = ['NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases']
    data['TotalPurchases'] = data[purchase_types].sum(axis=1)
    expences = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
    data['TotalExpences'] = data[expences].sum(axis=1)
    return data

data = load_data()

# plots

# Customer Demographics Analysis
st.header("Customer Demographics & Purchase Behavior")

# Age Distribution
st.subheader("Age Distribution")
fig = px.histogram(data, x='Age', nbins=30, 
                  labels={'Age': 'Age (years)', 'count': 'Number of customers'},
                  color_discrete_sequence=['#3366CC'],
                  text_auto=True)
fig.update_layout(bargap=0.1, 
                 title_font_size=20,
                 xaxis_title_font_size=16,
                 yaxis_title_font_size=16)
st.plotly_chart(fig, use_container_width=True)

# Income & Age & Education
st.subheader("Income by Age and Education Level")
with st.container():
    col1, col2 = st.columns([3, 1])
    with col1:
        st.image('charts/ageVsInc.png')
    with col2:
        st.markdown("""
        **Key Insights:**
        - Lower education (Basic) correlates with lower income
        - Age has minimal impact on income levels
        - Higher education generally leads to higher income across all age groups
        """)

# Purchase Behavior by Demographics
st.header("Purchase Behavior Analysis")

# Total Purchases by Income Grouped by Family Size
st.subheader("Purchase Patterns by Family Size")
st.image("charts/incVsPur.png")
st.markdown("""
**Key Insights:**
- Family size of 6: Limited purchases (≤25) regardless of income
- Family size of 2: Highest purchases when income exceeds average ($40k-$80k)
- Family size of 5 & 4: Variable purchase patterns
- Family size of 3: Shows steady growth with increasing income
""")

# Purchases by Marital Status
st.subheader("Purchase Behavior by Marital Status")
st.image('charts/image.png')
st.markdown("""
**Key Insights:**
- Married customers have highest purchase rates
- Single customers have moderate purchase rates
- Divorced customers have lowest purchase rates
""")


st.subheader("Campaign Response Analysis")
st.image('charts/IncVsRec.png')

cols_of_choice = ['Income', 'MntWines', 'MntFruits', 'MntMeatProducts', 
                 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds', 
                 'AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 
                 'AcceptedCmp4', 'AcceptedCmp5', 'Response']

grouped_by_response = data[cols_of_choice].groupby('Response').mean()

st.dataframe(grouped_by_response.style.highlight_max(axis=0, color='lightgreen')
             .format(precision=2), use_container_width=True)

st.markdown("""
**Key Finding:**
Customers who responded to campaigns show:
- Higher income levels
- Greater spending across all product categories
- Higher acceptance rates for previous campaigns
""")

st.markdown("""## Data """)
st.dataframe(data.head())
st.write("Data Shape: ", data.shape)
col1, col2 = st.columns(2)
with col1:
    st.write("Data Columns: ", data.columns.tolist())
with col2:
    st.write("Data Types: ", data.dtypes)