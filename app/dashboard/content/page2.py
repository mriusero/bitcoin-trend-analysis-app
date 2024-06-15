import streamlit as st
from ..functions import preprocessing, aggregate_sentiment, shape_wordcloud, load_csv, calculate_statistics, seconds_to_duration
from ..components import gaussian_curve
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
                    
        * Type "string" (5)   
           - user_name           : The name of the user, as they’ve defined it.
           - user_location       : The user-defined location for this account’s profile.
           - user_description    : The user-defined UTF-8 string describing their account.
           - text                : The actual UTF-8 text of the Tweet
           - hashtags            : All the other hashtags posted in the tweet along with #Bitcoin & #btc

        * Type "numerical" (3)
           - user_followers      : The number of followers an account currently has.
           - user_friends        : The number of friends an account currently has.
           - user_favourites     : The number of favorites an account currently has.
        
        * Type "datetime" (2) 
           - user_created        : Time and date, when the account was created.
           - date                : UTC time and date when the Tweet was created.
        
        * Type "dichotomous" (2)
           - user_verified       : When true, indicates that the user has a verified account
           - is_retweet          : Indicates whether this Tweet has been Retweeted by the authenticating user

        * Type "categorical" (1)        
           - source              : Utility used to post the Tweet, Tweets from the Twitter website have a source value - web 
                         """
        st.text(description)
    with col2:
        st.text("")
        st.text("")
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
    st.markdown('<div class="subheader">Dataframe_ </div>', unsafe_allow_html=True)
    st.text("")
    st.dataframe(tweet_data)

    st.markdown('<div class="subheader">Preprocessing_ </div>', unsafe_allow_html=True)
    st.text("")
    description = """       
            (1) Preprocessing on textual data ('source', 'user_location', 'user_description', 'text', 'hashtags'):
                - Hashtags conversion
                - Text normalization
                - Regex patterns filtering (emojis, punctuation, url, digits, mentions, worlds_alphabets, symbols...)
                - Stopwords suppression (EN + FR) 
                - Stemming
                
            (2) Merge with non-textual data ('user_created', 'user_followers', 'user_friends', 'user_favourites', 'user_verified'):
                - Account experience calculation --> 'user_since'
                  """
    st.text(description)
    st.text("")
    #preprocessed_df = preprocessing(tweet_data)
    preprocessed_df = load_csv(f"./data/sentiment/preprocessed_data.csv")
    preprocessed_df.drop(preprocessed_df.columns[0], axis=1, inplace=True)
    st.dataframe(preprocessed_df)

    st.markdown('<div class="subheader">Sentiment analysis_ </div>', unsafe_allow_html=True)
    col1, col2 = st.columns([6,2])
    with col1:
        frequency = st.selectbox("Select a frequency", ['60min', '6H', '12H', 'Daily', 'Weekly'])
        st.text("")
        description = """       
                    (1) Sentiment score calculation per period with VaderSentiment (SentimentIntensityAnalyzer): 
                        - user_description --> user_sentiment_mean
                        - text  --> text_sentiment_mean

                    (2) Aggregation of associated values :
                        - user_since     -->  user_since_mean
                        - user_followers -->  followers_sum
                        - user_friends   -->  friends_sum
                        - user_favorites -->  favorites_sum
                        - user_verified  -->  verified_sum

                    (3) Metadata collection with occurence counting : 
                        - text & user_description -> metawords
                        - hashtags --> metahashtags
                        - location --> metalocation
                        - source   --> metasource
                          """
        st.text(description)
        st.text("")

        #daily_sentiment = aggregate_sentiment(preprocessed_df, frequency)
        daily_sentiment = load_csv(f"./data/sentiment/sentiment_analysis_({frequency}).csv")
        daily_sentiment.drop(daily_sentiment.columns[0], axis=1, inplace=True)
        st.dataframe(daily_sentiment)

        st.markdown('<div class="subheader">Statistics_ </div>', unsafe_allow_html=True)
        st.text("")
        columns_stats = ['text_sentiment_mean', 'user_sentiment_mean', 'user_since_mean', 'tweet_sum', 'followers_sum',
                         'friends_sum', 'favorites_sum']
        statistics = calculate_statistics(daily_sentiment[columns_stats])
        statistics['user_since_mean'] = statistics['user_since_mean'].apply(seconds_to_duration)
        st.dataframe(statistics)

        st.markdown('<div class="subheader">Wordcloud_ </div>', unsafe_allow_html=True)
        st.text("")
        colA, colB = st.columns(2)

        with colA:
            theme = "metawords"
            st.text("#Metawords_ (user_description + text)")
            df_sentiment = load_csv(f"./data/sentiment/sentiment_analysis_({frequency}).csv")
            wordcloud = shape_wordcloud(df_sentiment, theme)
            st.image(wordcloud)

            theme = "metalocation"
            st.text("#Metalocation_ (user_location)")
            df_sentiment = load_csv(f"./data/sentiment/sentiment_analysis_({frequency}).csv")
            wordcloud = shape_wordcloud(df_sentiment, theme)
            st.image(wordcloud)

        with colB:
            theme = "metahashtags"
            st.text("#Metahashtags_ (hashtags)")
            df_sentiment = load_csv(f"./data/sentiment/sentiment_analysis_({frequency}).csv")
            wordcloud = shape_wordcloud(df_sentiment, theme)
            st.image(wordcloud)

            theme = "metasource"
            st.text("#Metasource_ (source)")
            df_sentiment = load_csv(f"./data/sentiment/sentiment_analysis_({frequency}).csv")
            wordcloud = shape_wordcloud(df_sentiment, theme)
            st.image(wordcloud)

    with col2:
        columns_dict = ['user_sentiment_mean', 'text_sentiment_mean', 'tweet_sum', 'followers_sum', 'friends_sum','favorites_sum', 'verified_sum']
        figures = []

        for cols in columns_dict:
            selected_columns = daily_sentiment[cols]
            fig = gaussian_curve(selected_columns)
            figures.append(fig)

        st.text("")
        st.pyplot(figures[0])
        st.text("")
        st.pyplot(figures[1])
        st.pyplot(figures[2])
        st.pyplot(figures[3])
        st.pyplot(figures[4])
        st.pyplot(figures[5])
        st.pyplot(figures[6])

















