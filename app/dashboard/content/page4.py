import streamlit as st
from ..functions import preprocessing, aggregate_sentiment
import pandas as pd
def page_4(tweet_data):
    st.markdown('<div class="title">SDA_2024</div>', unsafe_allow_html=True)
    st.markdown('<div class="header">#4 Sentiment analysis</div>', unsafe_allow_html=True)

    st.markdown('<div class="subheader">Description_</div>', unsafe_allow_html=True)

    st.markdown('<div class="subheader">Twitter data_ </div>', unsafe_allow_html=True)
    st.dataframe(tweet_data)

    st.markdown('<div class="subheader">Process_</div>', unsafe_allow_html=True)

    st.markdown('<div class="subheader">Results_ </div>', unsafe_allow_html=True)
    frequency = st.selectbox("Select a period", ['60min', '6H', '12H', 'Daily', 'Weekly'])

    size = st.selectbox("Select the size analyse", ['100%', '50%', '25%', '10%', '1%'])
    datasize = len(tweet_data['text']) + 1

    if size == '100%':
        arg_size = datasize
    elif size == '50%':
        arg_size = round(datasize * 0.5)
    elif size == '25%':
        arg_size = round(datasize * 0.25)
    elif size == '10%':
        arg_size = round(datasize * 0.1)
    elif size == '1%':
        arg_size = round(datasize * 0.01)

    clicked1 = st.button("Launch Analyse")
    if clicked1:
        preprocessed_df = preprocessing(tweet_data)
        daily_sentiment = aggregate_sentiment(preprocessed_df.head(arg_size), frequency)
        st.dataframe(daily_sentiment)

