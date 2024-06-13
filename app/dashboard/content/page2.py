import streamlit as st
from ..functions import preprocessing, aggregate_sentiment, shape_wordcloud, load_csv
def page_2(tweet_data):
    st.markdown('<div class="title">SDA_2024</div>', unsafe_allow_html=True)
    st.markdown('<div class="header">#2 BTC Twitter History [dataset B]</div>', unsafe_allow_html=True)

    st.markdown('<div class="subheader">Description_</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.text("")
        description = """       
        
        Start date (UTC) | 2021-02-05 10:52:04+00:00
        End date   (UTC) | 2021-03-31 00:00:00+00:00
        Period     (UTC) | 53 days 13:07:56    
                    
        [user_name]         -->     le nom de l'utilisateur.
        [user_location]     -->     la localisation définie par l'utilisateur.
        [user_description]  -->     la description du profil de l'utilisateur.
        [user_created]      -->     date et heure de création du compte.
        [user_followers]    -->     le nombre de followers du compte.
        [user_friends]      -->     le nombre d'amis du compte.
        [user_favourites]   -->     le nombre de favoris du compte.
        [user_verified]     -->     (booléen) true indique que l'utilisateur a un compte vérifié.
        [date]              -->     date et heure UTC de l'édition du tweet.
        [text]              -->     le tweet.
        [hashtags]          -->     les hashtags postés dans le tweet.
        [source]            -->     moyen d'édition du tweet.
        [is_retweet]        -->     (booléen) true indique qu'il s'agit d'un retweet.'   
                         """

        st.text(description)
    with col2:
        dataset_info = """
        *             ------ Bitcoin tweets historical DataFrame ------
            
              <class 'pandas.core.frame.DataFrame'>
              Index: 48583 entries, 0 to 48582
              Data columns (total 13 columns):
               #   Column            Non-Null Count  Dtype              
              ---  ------            --------------  -----              
               0   user_name         48583 non-null  object             
               1   user_location     48583 non-null  object             
               2   user_description  48583 non-null  object             
               3   user_created      48583 non-null  object             
               4   user_followers    48583 non-null  object             
               5   user_friends      48583 non-null  object             
               6   user_favourites   48583 non-null  object             
               7   user_verified     48583 non-null  object             
               8   date              48583 non-null  datetime64[ns, UTC]
               9   text              48583 non-null  object             
               10  hashtags          48583 non-null  object             
               11  source            48583 non-null  object             
               12  is_retweet        48583 non-null  object             
              dtypes: datetime64[ns, UTC](1), object(12)
              memory usage: 5.2+ MB
        """
        st.markdown(dataset_info)

    st.dataframe(tweet_data)

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
        preprocessed_df = preprocessing(tweet_data)
        st.dataframe(preprocessed_df)

        daily_sentiment = aggregate_sentiment(preprocessed_df.head(arg_size), frequency)
        st.dataframe(daily_sentiment)

    st.markdown('<div class="subheader">Wordcloud_ </div>', unsafe_allow_html=True)
    st.text("")
    col1, col2 = st.columns(2)

    with col1:
        theme = "metalocation"
        st.text("#Metalocation_ (user_location)")
        df_sentiment = load_csv(f"./data/sentiment/sentiment_analysis_({frequency}).csv")
        wordcloud = shape_wordcloud(df_sentiment, theme)
        st.image(wordcloud)

    with col2:
        theme = "metawords"
        st.text("#Metawords_ (user_description + text)")
        df_sentiment = load_csv(f"./data/sentiment/sentiment_analysis_({frequency}).csv")
        wordcloud = shape_wordcloud(df_sentiment, theme)
        st.image(wordcloud)
