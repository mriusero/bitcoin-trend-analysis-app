import streamlit as st
from ..components import create_candlestick_chart1, gaussian_curve, volume_curve
from ..functions import resample

def page_1(market_data):
    st.markdown('<div class="title">SDA_2024</div>', unsafe_allow_html=True)
    st.markdown('<div class="header">#1 BTC Market History [dataset A]</div>', unsafe_allow_html=True)

    st.markdown('<div class="subheader">Description_</div>', unsafe_allow_html=True)
    st.text("")
    description = """
            Start date (UTC) | 2021-02-05 10:52:04+00:00
            End date   (UTC) | 2021-03-31 00:00:00+00:00
            Period     (UTC) | 53 days 13:07:56
            
            --> [Open]______________________prix d'ouverture au début de la fenêtre temporelle
            --> [High]______________________prix le plus élevé dans la fenêtre temporelle
            --> [Low]_______________________prix le plus bas dans la fenêtre temporelle
            --> [Close]_____________________prix de clôture à la fin de la fenêtre temporelle
            --> [Volume_(BTC)]______________volume de BTC échangé dans cette fenêtre
            --> [Volume_(Currency)]_________volume de la devise correspondante échangée dans cette fenêtre
            --> [Weighted_Price]____________vwap (prix moyen pondéré par le volume)           
                 """

    st.text(description)
    st.markdown("""**data origin:** https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data""")
    # DataFrame
    st.markdown('<div class="subheader">DataFrame_ </div>', unsafe_allow_html=True)
    st.text("")

    col1, col2 = st.columns([5,3])
    with col1:
        st.dataframe(market_data)
        st.text("--> see app/data/exploration/dataset_exploration.ipynb for initial dataset")

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

    st.markdown('<div class="subheader">Columns_ </div>', unsafe_allow_html=True)
    st.text("")

    num_figures = 4
    figures = []
    for i in range(1, num_figures + 1):
        fig = gaussian_curve(market_data.iloc[:, i])
        figures.append(fig)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.pyplot(figures[0])
    with col2:
        st.pyplot(figures[2])
    with col3:
        st.pyplot(figures[1])
    with col4:
        st.pyplot(figures[3])

    st.markdown('<div class="subheader">Market_ </div>', unsafe_allow_html=True)
    #st.text("Please select a frequency:")
    frequency = st.selectbox("", ['60min', '6H', '12H', 'Daily', 'Weekly'])

    display_data = resample(market_data, frequency)

    candlestick_chart = create_candlestick_chart1(display_data)
    st.plotly_chart(candlestick_chart)

    fig_btc, fig_currency = volume_curve(display_data)
    col1, col2 = st.columns(2)
    with col1:
        st.pyplot(fig_btc)
    with col2:
        st.pyplot(fig_currency)

