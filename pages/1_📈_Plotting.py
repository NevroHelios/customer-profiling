import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff

st.set_page_config(page_icon=":shark:", page_title="Customer Prodiling", layout='wide')

# load data
# @st.cache_data
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

st.dataframe(data.head())

# plots

st.markdown("""### Age distribution""")
# st.title("Age distribution")
fig = px.histogram(data, x='Age', nbins=30, title='Age distribution'
                   , labels={'Age': 'Age', 'count': 'Number of customers'},
                   text_auto=True)
st.plotly_chart(fig)



st.markdown("""### Income & Age & Education""")
# grouped_data = data.groupby(['Education', 'Age'])['Income'].mean().reset_index()

# fig = go.Figure()
# for education in grouped_data['Education'].unique():
#     subset = grouped_data[grouped_data['Education'] == education]
#     fig.add_trace(go.Scatter(
#         x=subset['Age'], 
#         y=subset['Income'],
#         mode='lines',
#         name=education,
#     ))

# fig.update_layout(
#     title='Income distribution by Age Grouped by Education',
#     width=1200,
#     height=400,
#     xaxis=dict(title='Age', showgrid=True, gridwidth=0.5, gridcolor='lightgrey'),
#     yaxis=dict(title='Income', showgrid=True, gridwidth=0.5, gridcolor='lightgrey'),
#     legend=dict(title='Education', x=1.02, y=1, xanchor='left'),
# )
# st.plotly_chart(fig)
st.image('charts/ageVsInc.png')


st.markdown("""### Total Purchases by Income Grouped by Family Size""")
# grouped_data = data.groupby(['Family_Size', 'TotalPurchases'])['Income'].mean().reset_index()
# fig = go.Figure()
# for family_size in grouped_data['Family_Size'].unique():
#     subset = grouped_data[grouped_data['Family_Size'] == family_size]
#     fig.add_trace(go.Scatter(
#         x=subset['TotalPurchases'], 
#         y=subset['Income'],
#         mode='lines',
#         name=str(family_size),
#         line=dict(width=3),
#         hovertext=f"family: {str(family_size)}"
#     ))

# fig.update_layout(
#     title='Income distribution by Total Purchases Grouped by Family Size',
#     width=1200,
#     height=400,
#     xaxis=dict(title='Total Purchases', showgrid=True, gridwidth=0.5, gridcolor='lightgrey'),
#     yaxis=dict(title='Income', showgrid=True, gridwidth=0.5, gridcolor='lightgrey'),
#     legend=dict(title='Family Size', x=1.02, y=1, xanchor='left'),
#     # colorway=px.colors.sequential.Inferno,
# )
# st.plotly_chart(fig)
st.image('charts/IncVsPur.png')


st.markdown("""### Total Purchases by Income Grouped by Marital Status""")

st.image('charts/image.png')