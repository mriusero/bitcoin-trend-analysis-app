import streamlit as st

import pandas as pd
import numpy as np
import cufflinks as cf
import seaborn as sns
import plotly.express as px

st.subheader("Evolution of stock prices:")

# Importer la table des stocks de la base de données data de Plotly
df_stocks = px.data.stocks()

companies_options = df_stocks.columns[1:]

companies = st.sidebar.multiselect("Companies selected:",companies_options)
fig_lines = px.line(df_stocks, x='date', y=companies,
       title='Companies stocks')
st.plotly_chart(fig_lines)

st.subheader("Tips amount per day")
df_tips = px.data.tips()

size = st.slider("Size of clients", 1,df_tips['size'].max())
fig_bars = px.bar(df_tips[df_tips['size'] == size], x='day', y='tip', color='sex', title='Tips by Sex on Each Day',
      labels={'tip': 'Tip Amount', 'day': 'Day of the Week'})
st.plotly_chart(fig_bars)