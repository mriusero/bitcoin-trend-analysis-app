import streamlit as st
from ..components import create_table
def page_2(tweet_data):
    st.markdown('<div class="title">Bitcoin Tweets Historical Dataset</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">Ceci est une description</div>', unsafe_allow_html=True)
    tweet_df = create_table(tweet_data)
    st.dataframe(tweet_df)

