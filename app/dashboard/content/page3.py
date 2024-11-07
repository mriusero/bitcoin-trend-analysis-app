import streamlit as st
from ..functions import prepare_data, predict, duration_to_seconds, load_csv, aggregate_sentiment


def page_3(market_data, tweet_data):
    st.markdown('<div class="title">Bitcoin Trend Analysis App</div>', unsafe_allow_html=True)
    st.markdown('<div class="header">#3 Analytics</div>', unsafe_allow_html=True)

    concept = ("""
### Concept_
    Here is a Linear Regresssion Model trainable with 4 data categories (OHLC, Trading volumes, Sentiment score, Context values).
    The analysis start on 2021-02-05, end on 2021-03-31, for a total duration of 53 days 13:07:56.    
    """)
    st.markdown(concept)


    display_dataframe = ("""
### DataFrame_
    """)
    st.markdown(display_dataframe)
    st.dataframe(prepare_data(market_data, frequency='60min'))

    analytics_description = ("""
#### (1) Select X_
              
    * [multiselect] Select_X = [
                                  'Open', 'High', 'Low', 'Close',                                                            
                                  'Volume_(BTC)', 'Volume_(Currency)', 'Weighted_Price',                                                    
                                  'text_sentiment_mean', 'user_sentiment_mean',                                                       
                                  'user_since_mean', 'tweet_sum', 'followers_sum', 'friends_sum', 'favorites_sum', 'verified_sum'     
                               ]
#### (2) Select Y_                 
      
    * [selectbox] Select_Y = [
                                'Open', 'High', 'Low', 'Close',                                                             
                                'Volume_(BTC)', 'Volume_(Currency)', 'Weighted_Price',                                                    
                                'text_sentiment_mean', 'user_sentiment_mean',                                                     
                                'user_since_mean', 'tweet_sum', 'followers_sum', 'friends_sum', 'favorites_sum', 'verified_sum'     
                             ]    
      
#### (3) Aggregation frequency_

    * [selectbox] frequency_map = {
                                       "60min": "60min",
                                       "6H": "6H",
                                       "12H": "12H",
                                       "Daily": "Daily",
                                       "Weekly": "Weekly"
                                   }
    
#### (4) Test size_

    * [slider] selected_test_size = (
                                        'Test size (%)', 1, 100, 20)
                                    )
    """)
    st.markdown(analytics_description)


    model_UI = ("""
### Model_
    Choose a training configuration and see results !
        
    """)
    st.markdown(model_UI)

    if 'frequency' not in st.session_state:
        st.session_state.frequency = "60min"

    df_sentiment = prepare_data(market_data, st.session_state.frequency)
    columns_list = df_sentiment.columns.tolist()
    columns_to_exclude = ['metalocation', 'metahashtags', 'metawords', 'metasource', 'date']
    selection_list = [column for column in columns_list if column not in columns_to_exclude]

    # Initialize default values for X_selected and Y_selected
    default_X_selected = [selection_list[0]] + selection_list[-8:]
    default_Y_selected = selection_list[3]

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        X_selected = st.multiselect('Select X:', selection_list, default_X_selected)
    with col2:
        Y_selected = st.selectbox('Select Y:', selection_list, index=selection_list.index(default_Y_selected))
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

    #if st.button('Predict'):
    df_sentiment['user_since_mean'] = df_sentiment['user_since_mean'].apply(duration_to_seconds)
    predict(df_sentiment, test_size, X_selected, Y_selected)



