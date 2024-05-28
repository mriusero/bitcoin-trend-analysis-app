import os
import streamlit as st

def load_css():
    css_path = os.path.join(os.path.dirname(__file__), 'styles.css')
    with open(css_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def app_layout(market_data, tweet_data):
    from .content import page_0, page_1, page_2, page_3, page_4, page_5, page_6

    st.set_page_config(
        page_title=" ~ BTC Sentiment Analysis ~ ",
        page_icon=":shark:",
        layout='wide',
        initial_sidebar_state="auto",
        menu_items={
            'About': "#Github Repository :\n\nhttps://github.com/mriusero/projet-sda-dash-streamlit/blob/main/README.md"
        }
    )

    load_css()
    page = st.sidebar.radio(" ~ BTC Sentiment Analysis ~ ", ["Introduction", "#1_ BTC Market History [dataset A]", "#2_ BTC Twitter History [dataset B]", "#3_ Preprocessing", "#4_ Sentiment analysis", "#5_ Price prediction", "Conclusion"])

    if page == "Introduction":
        page_0()
    elif page == "#1_ BTC Market History [dataset A]":
        page_1(market_data)
    elif page == "#2_ BTC Twitter History [dataset B]":
        page_2(tweet_data)
    elif page == "#3_ Preprocessing":
        page_3(market_data, tweet_data)
    elif page == "#4_ Sentiment analysis":
        page_4(market_data, tweet_data)
    elif page == "#5_ Price prediction":
        page_5(market_data, tweet_data)
    elif page == "Conclusion":
        page_6(market_data, tweet_data)







