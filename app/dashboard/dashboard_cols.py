import streamlit as st

import pandas as pd
import numpy as np
import chart_studio.plotly as py
import cufflinks as cf
import seaborn as sns
import plotly.express as px


# Importer la table des stocks & tips de la base de données data de Plotly
df_stocks = px.data.stocks()
df_tips = px.data.tips()


# Creation de deux colonnes
col1, col2 = st.columns(2) # st.columns([1,1])

# Plot le premier graphe dans la première colonne
with col1:
    st.subheader("Evolution of stock prices:")
    companies_options = df_stocks.columns[1:]
    companies = st.sidebar.multiselect("Companies selected:",companies_options)
    
    fig_lines = px.line(df_stocks, x='date', y=companies,
       title='Companies stocks')
    
    fig_lines.update_layout(width=500, height=300)
    st.plotly_chart(fig_lines)


# Plot le deuxièmz graphe dans la deuxième colonne
with col2:
    st.subheader("Tips amount per day")      
    size = st.slider("Size of clients", 1,df_tips['size'].max())

    fig_bars = px.bar(df_tips[df_tips['size'] == size], x='day', y='tip', color='sex', title='Tips by Sex on Each Day',
      labels={'tip': 'Tip Amount', 'day': 'Day of the Week'})
    
    fig_bars.update_layout(width=500, height=300)
    st.plotly_chart(fig_bars)

  