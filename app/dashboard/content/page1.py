import streamlit as st
from ..components import create_candlestick_chart1, gaussian_curve, combined_volume_curve
from ..functions import resample, calculate_statistics

def page_1(market_data):
    st.markdown('<div class="title">SDA_2024</div>', unsafe_allow_html=True)
    st.markdown('<div class="header">#1 BTC Market History [dataset A]</div>', unsafe_allow_html=True)
    st.text("")

    col1, col2 = st.columns([3,2])

    with col1:
       st.markdown('<div class="subheader">Description_</div>', unsafe_allow_html=True)
       st.text("")
       description = """
                Start date (UTC) | 2021-02-05 10:52:04+00:00
                End date   (UTC) | 2021-03-31 00:00:00+00:00
                Period     (UTC) | 53 days 13:07:56   
                
                  - timestamp          : start time of time window
                  - Open               : open price at start time window
                  - High               : high price within time window              
                  - Low                : low price within time window              
                  - Close              : close price at end of time window            
                  - Volume_(BTC)       : volume of BTC transacted in this window      
                  - Volume_(Currency)  : Volume of corresponding currency transacted in this window 
                  - Weighted_Price     : Volume Weighted Average Price [VWAP]
                     """
       st.text(description)
       st.text("")
       st.markdown('<div class="subheader">Statistics_</div>', unsafe_allow_html=True)
       statistics = calculate_statistics(market_data)
       st.markdown(
           """
           <style>
           .dataframe tbody tr th:only-of-type {
               vertical-align: middle;
           }

           .dataframe tbody tr th {
               vertical-align: top;
           }

           .dataframe thead th {
               text-align: right;
           }

           /* Définir les largeurs des colonnes */
           .col0 { width: 100px; }
           .col1 { width: 200px; }
           .col2 { width: 100px; }
           .col3 { width: 150px; }
           .col4 { width: 100px; }
           .col5 { width: 100px; }
           .col6 { width: 150px; }
           </style>
           """,
           unsafe_allow_html=True
       )
       st.text("")
       st.dataframe(statistics)

       st.markdown('<div class="subheader">Dataframe_ </div>', unsafe_allow_html=True)
       st.text("")
       st.dataframe(market_data)

       st.markdown('<div class="subheader">Frequency_ </div>', unsafe_allow_html=True)
       frequency = st.selectbox("", ['60min', '6H', '12H', 'Daily', 'Weekly'])
       display_data = resample(market_data, frequency)

       st.markdown('<div class="subheader">Trading volumes__ </div>', unsafe_allow_html=True)
       st.text("")
       fig = combined_volume_curve(display_data)
       st.pyplot(fig)

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
        st.text("")
        st.text("")

        columns_dict = ['Open', 'High', 'Low', 'Close']
        figures = []

        for cols in columns_dict:
            selected_columns = market_data[cols]
            fig = gaussian_curve(selected_columns)
            figures.append(fig)

        col1, col2, col3 = st.columns([1,25,1])
        with col2:
            st.pyplot(figures[0])
            st.text("")
            st.text("")
            st.pyplot(figures[1])
            st.text("")
            st.text("")
            st.pyplot(figures[2])
            st.text("")
            st.text("")
            st.text("")
            st.pyplot(figures[3])

    st.markdown('<div class="subheader">Market_ </div>', unsafe_allow_html=True)
    candlestick_chart = create_candlestick_chart1(display_data)
    st.plotly_chart(candlestick_chart)