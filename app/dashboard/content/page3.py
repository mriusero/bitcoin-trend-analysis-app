import streamlit as st
from ..components import create_candlestick_chart
from ..functions import text_analysis, resample_for_candlesticks
def page_3(market_data, tweet_data):

    st.markdown('<div class="title">Bitcoin Tweet Sentiment Analysis</div>', unsafe_allow_html=True)

    st.markdown('<div class="header">Twitter data</div>', unsafe_allow_html=True)
    st.dataframe(tweet_data)

    st.markdown('<div class="header">Sentiment Analysis</div>', unsafe_allow_html=True)
    frequency = st.selectbox("Select a period", ['Hourly', '6H', '12H', 'Daily', 'Weekly'])

    display_data = resample_for_candlesticks(market_data, frequency)
    candlestick_chart = create_candlestick_chart(display_data)
    st.plotly_chart(candlestick_chart)

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

    clicked = st.button("Launch Analyse")

    # Vérification si le bouton est cliqué
    if clicked:
        #st.write("Le bouton a été cliqué !")
        preprocessed_df, daily_sentiment = text_analysis(tweet_data.head(arg_size), frequency)
        st.dataframe(daily_sentiment)





