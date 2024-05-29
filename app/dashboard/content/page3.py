import streamlit as st

from ..functions import preprocessing, aggregate_sentiment

def page_3(market_data, tweet_data):
    st.markdown('<div class="title">SDA_2024</div>', unsafe_allow_html=True)
    st.markdown('<div class="header">#3 Sentiment Analysis</div>', unsafe_allow_html=True)

    st.markdown('<div class="subheader">Initial data_ </div>', unsafe_allow_html=True)
    st.dataframe(tweet_data)




    st.markdown('<div class="subheader">Preprocessing_ </div>', unsafe_allow_html=True)

    st.markdown("")
    clicked1 = st.button("►")
    if clicked1:
        preprocessed_df = preprocessing(tweet_data)
        st.session_state['preprocessed_df'] = preprocessed_df
        st.dataframe(preprocessed_df)

    st.markdown('<div class="subheader">Sentiment analysis_ </div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        frequency = st.selectbox("Select a period", ['60min', '6H', '12H', 'Daily', 'Weekly'])
    with col2:
        size = st.selectbox("Select the size analyse", ['10%', '5%', '1%'])
        datasize = len(tweet_data['text']) + 1

        if size == '10%':
            arg_size = round(datasize * 0.1)
        elif size == '5%':
            arg_size = round(datasize * 0.05)
        elif size == '1%':
            arg_size = round(datasize * 0.01)

    st.markdown("Launch sentiment analysis (sample):")
    clicked2 = st.button("Sentiment analysis")
    if clicked2:
        if 'preprocessed_df' in st.session_state:
            preprocessed_df = st.session_state['preprocessed_df']
            daily_sentiment = aggregate_sentiment(preprocessed_df.head(arg_size), frequency)
            st.dataframe(daily_sentiment)
        else:
            st.error("Please run the preprocessing step first by clicking the 'See' button.")