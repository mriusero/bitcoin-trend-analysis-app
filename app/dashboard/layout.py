import os
import streamlit as st

def load_css():
    """
    Loads and applies the custom CSS styles from a 'styles.css' file.

    The CSS file is expected to be in the same directory as this script.
    The styles are applied to the Streamlit app using the `st.markdown` method.
    """
    css_path = os.path.join(os.path.dirname(__file__), 'styles.css')
    with open(css_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def app_layout(market_data, tweet_data):
    """
    Defines the layout and navigation of the Streamlit app.

    This function sets the page configuration, loads the CSS, and handles the navigation
    between different pages in the app. Each page displays relevant content based on
    the user's selection in the sidebar.

    :param market_data: Data related to the BTC market (e.g., market history).
    :type market_data: pd.DataFrame
    :param tweet_data: Data related to Twitter history (e.g., tweet statistics).
    :type tweet_data: pd.DataFrame
    """
    from .content import page_intro, page_0, page_1, page_2, page_3

    st.set_page_config(
        page_title="SDA 2024 - Marius Ayrault",
        page_icon=":shark:",
        layout='wide',
        initial_sidebar_state="auto"
    )
    load_css()
    page = st.sidebar.radio("Table of content_", ["Introduction", "#0_ Data Management", "#1_ BTC Market History [A]", "#2_ BTC Twitter History [B]", "#3_ Analytics"])

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