import os
import streamlit as st

def load_css():
    css_path = os.path.join(os.path.dirname(__file__), 'styles.css')
    with open(css_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def app_layout(market_data, tweet_data):
    from .content import page_intro, page_0, page_1, page_2, page_3

    st.set_page_config(
        page_title="SDA 2024 - Marius Ayrault",
        page_icon=":shark:",
        layout='wide',
        initial_sidebar_state="auto",
        menu_items={
            'About': "#Github Repository :\n\nhttps://github.com/mriusero/projet-sda-dash-streamlit/blob/main/README.md"
        }
    )

    load_css()
    page = st.sidebar.radio("projet-sda-dash-streamlit", ["Introduction", "#0_ Data Management", "#1_ BTC Market History [A]", "#2_ BTC Twitter History [B]", "#3_ Analytics"])

    if page == "Introduction":
        page_intro()
    elif page == "#0_ Data Management":
        page_0()
    elif page == "#1_ BTC Market History [A]":
        page_1(market_data)
    elif page == "#2_ BTC Twitter History [B]":
        page_2(tweet_data)
    elif page == "#3_ Analytics":
        page_3(market_data, tweet_data)








