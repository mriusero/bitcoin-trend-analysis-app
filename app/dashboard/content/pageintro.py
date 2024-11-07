import streamlit as st


def page_intro():
    """
    Displays an introductory page for the Bitcoin Trend Analysis App using Streamlit.
    The function includes context about Bitcoin and project objectives within a learning
    framework involving data management, visualization, and text mining.

    It uses Streamlit's markdown capabilities to render HTML and Markdown content, including:
      - An application title styled in HTML.
      - A background description of Bitcoin's history and market trends.
      - A detailed project description outlining the analysis phases.
    """

    # Display application title with custom HTML styling
    st.markdown('<div class="title">Bitcoin Trend Analysis App</div>', unsafe_allow_html=True)

    # Background context on Bitcoin's origin, use case, and historical price trends
    context = """
# Context      

    Bitcoin ₿ is a cryptocurrency invented in 2008 by an unknown person or group of people using the name Satoshi Nakamoto. Its use began 
    in 2009 when its implementation was released as open-source software.

    Bitcoin is a decentralized digital currency, without a central bank or single administrator, that can be sent from user to user on the 
    peer-to-peer bitcoin network without the need for intermediaries. Transactions are verified by network nodes through cryptography and 
    recorded in a public distributed ledger called a blockchain. 

    On November 30, 2020, Bitcoin reached a new all-time high of $19,860, surpassing the previous record from December 2017. On January 19, 
    2021, Elon Musk added #Bitcoin to his Twitter profile and tweeted, "In retrospect, it was inevitable," causing the price to rise by 
    nearly $5,000 in an hour to reach $37,299.
    """

    # Render context section
    st.markdown(context)

    # Project goals and phases in the context of data management, visualization, and predictive analytics
    project = """
    # Project

    This project is carried out in a learning context, aiming to improve skills in data management, data visualization, and text mining.

    (1) The first step is the Data Management phase, conducted in a Jupyter notebook with Pandas:

        - Analysis and cleaning of the first dataset: Bitcoin Market History.
        - Analysis and cleaning of the second dataset: Bitcoin Twitter History.
        - Identification of overlapping time periods and export of a merged dataframe for analysis.

    (2) The second step is the Data Visualization phase, performed on both dataframes:

        - Preprocessing with nltk (SnowballStemmer, Stopwords).
        - Adding value through new variable creation (Sentiment analysis with VaderSentiment, time series aggregation, WordClouds).
        - Statistical analysis and trend visualization using Numpy, Scipy, and Matplotlib.

    (3) Analytical study of correlations between 'Bitcoin Market History' and 'Bitcoin Twitter History':

        - Creation of a Modular Linear Regression Model using sklearn and Streamlit widgets.
        - Comparison of predictions to actual market data with Dash Plotly.
        - Visualization of prediction performance using Numpy, Scipy, Matplotlib, and Seaborn.
    """

    # Render project description section
    st.markdown(project)
