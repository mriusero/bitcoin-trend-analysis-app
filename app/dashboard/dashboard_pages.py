import streamlit as st

import pandas as pd
import numpy as np
import cufflinks as cf
import seaborn as sns
import plotly.express as px

import streamlit as st


st.set_page_config(page_title="My streamlit dashboard")
# Importer la table des stocks & tips de la base de données data de Plotly
df_stocks = px.data.stocks()
df_tips = px.data.tips()

# Page 1
def page1():
    st.title("Statistiques descriptives")
    st.subheader('Statistiques descriptives pour les stocks:')
    st.write(df_stocks.describe())

    st.subheader('Statistiques descriptives pour les tips:')
    st.write(df_tips.describe())

# Page 2
def page2():
    st.markdown("<h1 style='color: red;'>Visualisations</h1>", unsafe_allow_html=True)
    st.subheader("Evolution des prix des stocks:")
    companies_options = df_stocks.columns[1:]
    companies = st.multiselect("Entreprises séléctionnées:",companies_options, default=list(companies_options))
    
    fig_lines = px.line(df_stocks, x='date', y=companies,
       title='Actions des entreprises')
    
    fig_lines.update_layout(width=500, height=300)
    st.plotly_chart(fig_lines)

# Sidebar navigation
page = st.sidebar.radio("Select a page", ["Statistiques descriptives", "Visualisations"])

# Display selected page
if page == "Statistiques descriptives":
    page1()
elif page == "Visualisations":
    page2()
