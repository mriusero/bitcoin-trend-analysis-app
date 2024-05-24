import streamlit as st
from ..components import create_table, create_candlestick_chart
from ..functions import resample

def page_1(df):
    st.markdown('<div class="title">Bitcoin Market Historical Dataset</div>', unsafe_allow_html=True)

    market_df = create_table(df)
    st.dataframe(market_df)

    frequency = st.selectbox("Select a period", ['Hourly', '6H', '12H', 'Daily', 'Weekly'])

    display_data = resample(df, frequency)
    candlestick_chart = create_candlestick_chart(display_data)
    st.plotly_chart(candlestick_chart)