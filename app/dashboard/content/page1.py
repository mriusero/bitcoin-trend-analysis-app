import streamlit as st
from ..components import create_candlestick_chart
from ..functions import resample

def page_1(market_df):
    # Title
    st.markdown('<div class="title">Market Historical</div>', unsafe_allow_html=True)

    # Introduction

    description = """
                    This dataframe .... description du dataset et introduction de la page

    """
    st.markdown(description)

    # DataFrame
    st.markdown('<div class="header">DataFrame</div>', unsafe_allow_html=True)
    col1, col2 = st.columns([5,3])
    with col1:
        st.dataframe(market_df)
        st.markdown("""**data origin:** https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data""")
    with col2:
        dataset_info = """              
        *              ------ Bitcoin market historical DataFrame ------
              <class 'pandas.core.frame.DataFrame'>
              Index: 76996 entries, 4780269 to 4857376
              Data columns (total 8 columns):
               #   Column             Non-Null Count  Dtype              
              ---  ------             --------------  -----              
               0   Timestamp          76996 non-null  datetime64[ns, UTC]
               1   Open               76996 non-null  float64            
               2   High               76996 non-null  float64            
               3   Low                76996 non-null  float64            
               4   Close              76996 non-null  float64            
               5   Volume_(BTC)       76996 non-null  float64            
               6   Volume_(Currency)  76996 non-null  float64            
               7   Weighted_Price     76996 non-null  float64            
              dtypes: datetime64[ns, UTC](1), float64(7)
              memory usage: 5.3 MB                                 
        """
        st.markdown(dataset_info)

    frequency = st.selectbox("Select a period", ['60min', '6H', '12H', 'Daily', 'Weekly'])

    display_data = resample(market_df, frequency)
    candlestick_chart = create_candlestick_chart(display_data)
    st.plotly_chart(candlestick_chart)