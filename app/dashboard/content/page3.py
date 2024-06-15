import streamlit as st
from ..functions import prepare_data, predict, duration_to_seconds


def page_3(market_data, tweet_data):
    st.markdown('<div class="title">SDA_2024</div>', unsafe_allow_html=True)
    st.markdown('<div class="header">#3 Price prediction</div>', unsafe_allow_html=True)

    st.markdown('<div class="subheader">Model_</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">  </div>', unsafe_allow_html=True)

    if 'frequency' not in st.session_state:
        st.session_state.frequency = "60min"

    df_sentiment = prepare_data(market_data, st.session_state.frequency)
    columns_list = df_sentiment.columns.tolist()
    columns_to_exclude = ['metalocation', 'metahashtags', 'metawords', 'metasource', 'date']
    selection_list = [column for column in columns_list if column not in columns_to_exclude]

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        X_selected = st.multiselect('Select X:', selection_list)
    with col2:
        Y_selected = st.selectbox('Select Y:', selection_list)
    with col3:
        frequency_map = {
            "60min": "60min",
            "6H": "6H",
            "12H": "12H",
            "Daily": "Daily",
            "Weekly": "Weekly"
        }
        selected_frequency = st.selectbox("Select Frequency:", frequency_map,
                                          index=list(frequency_map.keys()).index(st.session_state.frequency))
        st.session_state.frequency = selected_frequency
    with col4:
        selected_test_size = st.slider('Test size (%)', 1, 100, 20)
        test_size = selected_test_size / 100

    if st.button('Predict'):
        df_sentiment['user_since_mean'] = df_sentiment['user_since_mean'].apply(duration_to_seconds)
        predict(df_sentiment, test_size, X_selected, Y_selected)



