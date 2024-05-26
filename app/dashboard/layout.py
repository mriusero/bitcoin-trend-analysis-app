import os
import streamlit as st

def load_css():
    css_path = os.path.join(os.path.dirname(__file__), 'styles.css')
    with open(css_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def app_layout(market_data, tweet_data):
    from .content import page_0, page_1, page_2, page_3

    st.set_page_config(
        page_title="Bitcoin Sentiment Analysis",
        page_icon=":shark:",
        layout='wide',
        initial_sidebar_state="auto",
        menu_items={
            'About': "#Github Repository :\n\nhttps://github.com/mriusero/projet-sda-dash-streamlit/blob/main/README.md"
        }
    )

    load_css()
    page = st.sidebar.radio("Bitcoin Sentiment Analysis", ["Introduction", "Market Historical", "Bitcoin Tweets Historical Dataset", "Text_mining"])

    if page == "Introduction":
        page_3(market_data, tweet_data)
    elif page == "Market Historical":
        page_1(market_data)
    elif page == "Bitcoin Tweets Historical Dataset":
        page_2(tweet_data)
    elif page == "Text_mining":
        page_3(market_data, tweet_data)







