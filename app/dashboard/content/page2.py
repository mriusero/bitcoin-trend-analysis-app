import streamlit as st

def page_2(tweet_data):
    st.markdown('<div class="title">Bitcoin Tweets Historical Dataset</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">Ceci est une description</div>', unsafe_allow_html=True)

    st.dataframe(tweet_data)

