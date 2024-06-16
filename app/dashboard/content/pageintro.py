import streamlit as st
def page_intro():
    st.markdown('<div class="title">SDA_2024</div>', unsafe_allow_html=True)
    context = """
# #Context_      

    Bitcoin ₿ is a cryptocurrency invented in 2008 by an unknown person or group of people using the name Satoshi Nakamoto. Its use began 
    in 2009 when its implementation was released as open-source software.
    
    Bitcoin is a decentralized digital currency, without a central bank or single administrator, that can be sent from user to user on the 
    peer-to-peer bitcoin network without the need for intermediaries. Transactions are verified by network nodes through cryptography and 
    recorded in a public distributed ledger called a blockchain. 
    
    On November 30, 2020, Bitcoin reached a new all-time high of $19,860, surpassing the previous record from December 2017. On January 19, 
    2021, Elon Musk added #Bitcoin to his Twitter profile and tweeted, "In retrospect, it was inevitable" causing the price to rise by 
    nearly $5,000 in an hour to reach $37,299.
    """
    st.markdown(context)
    project = """
# #Project_

    This project is carry out in Sorbonne Data Analytics learning context with for target data management, data vizualisation & text mining.
    
      (1) The first step is the Data Management phase, carried out on jupyter_notebook with Pandas : 
      
              - Analysis and cleaning of the first dataset : Bitcoin Market History 
              - Analysis and cleaning of the second dataset : Bitcoin Twitter History
              - Cross time period identification and dataframe export for analysis
              
      (2) The second step is the Data Visualisation phase, carried out on both dataframes :
      
              - Preprocessing with nltk (SnowballStemmer, Stopwords) 
              - Adding value through new variables creation (Sentiment analysis with VaderSentiment, Times series aggregation, Wordcloud ...)             
              - Statistics calculation and trends visualisation with Numpy, Scipy, Matplotlib 
              
      (3) Analytics study of correlation between 'Bitcoin Market History' & 'Bitcoin Twitter History':
      
              - Modular Linear Regression Model creation with sklearn and streamlit widgets
              - Prediction comparison to market with Dash Plotly 
              - Prediction performance vizualisation with Numpy, Scipy, Matplotlib, Seaborn
    """
    st.markdown(project)