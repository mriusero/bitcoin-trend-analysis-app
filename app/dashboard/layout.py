import streamlit as st
import plotly.express as px
from .components import create_table
import os
def load_css():
    css_path = os.path.join(os.path.dirname(__file__), 'styles.css')
    with open(css_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def create_layout(market_data, tweet_data):
    st.set_page_config(page_title="My streamlit dashboard")
    load_css()
    page = st.sidebar.radio("Select a page", ["Dataset description", "Empty page"])

    if page == "Dataset description":
        page_1(market_data, tweet_data)
    elif page == "Empty page":
        page_2()

def page_1(market_data, tweet_data):
    st.title('Bitcoin Sentiment Analysis')
    st.markdown('<div class="title">Bitcoin Sentiment Analysis</div>', unsafe_allow_html=True)
    #st.header('Bitcoin Market Historical Data')
    market_df = create_table(market_data)
    st.dataframe(market_df)

    st.header('Bitcoin Tweets Historical Data')
    tweets_df = create_table(tweet_data)
    st.dataframe(tweets_df)

def page_2():
    st.markdown("<h1 style='color: green;'>Visualisations</h1>", unsafe_allow_html=True)
    st.title('Empty page 2')




