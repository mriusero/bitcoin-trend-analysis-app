import streamlit as st
from ..functions import aggregate_sentiment,  shape_wordcloud, load_csv, calculate_statistics, seconds_to_duration, preprocessing, calculate_sentiment
from ..components import gaussian_curve
def page_2(tweet_data):
    st.markdown('<div class="title">SDA_2024</div>', unsafe_allow_html=True)                                #TITLE
    st.markdown('<div class="header">#2 BTC Twitter History [B]</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([3,1])
    with col1:
        st.text("")                             #DESCRIPTION
        description = """
### Description_
      
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
        st.markdown(description)

    with col2:                                  #DATAFRAME INFO
        st.text("")
        st.text("")
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

                                    #DATAFRAME
    st.markdown("""                 
### Dataframe_
                """)
    st.dataframe(tweet_data)
                                            #PREPROCESSING
    preprocessing_ = """            
### Preprocessing_
           
    (1) Preprocessing on textual data ('source', 'user_location', 'user_description', 'text', 'hashtags'):
    
            - Hashtags conversion
            - Text normalization
            - Regex patterns filtering (emojis, punctuation, url, digits, mentions, worlds_alphabets, symbols...)
            - Stopwords suppression (EN + FR) 
            - Stemming
        
    (2) Merge with non-textual data ('user_created', 'user_followers', 'user_friends', 'user_favourites', 'user_verified'):
    
            - Account experience calculation --> 'user_since' 
                  """
    st.markdown(preprocessing_)
    st.text("")
                                        #PREPROCESSED DATA
    preprocessed_data = ("""
### Preprocessed data_
    """)
    st.markdown(preprocessed_data)
    #preprocessed_df = preprocessing(tweet_data)                                #Run script Vs
    preprocessed_df = load_csv(f"./data/sentiment/preprocessed_data.csv")       #Load results
    preprocessed_df.drop(preprocessed_df.columns[0], axis=1, inplace=True)
    st.dataframe(preprocessed_df)

    col1, col2 = st.columns([6,2])
    with col1:
                                        #SENTIMENT ANALYSIS
        sentiment_analysis = ("""
### Sentiment analysis_
        """)
        st.markdown(sentiment_analysis)
        frequency = st.selectbox("Select a frequency:", ['60min', '6H', '12H', 'Daily', 'Weekly'])
        sentiment_analysis_description = f"""     
    freq : '{frequency}'            

        (1) Sentiment score calculation per period with VaderSentiment (SentimentIntensityAnalyzer): 
            
                - user_description  -->  user_sentiment_mean
                - text              -->  text_sentiment_mean
                   
        (2) Aggregation of associated values :
            
                - user_since       -->   user_since_mean
                - user_followers   -->   followers_sum
                - user_friends     -->   friends_sum
                - user_favorites   -->   favorites_sum
                - user_verified    -->   verified_su
                
        (3) Metadata collection with occurence counting : 
            
                - text & user_description   -->  metawords
                - hashtags                  -->  metahashtags
                - location                  -->  metalocation
                - source                    -->  metasource
                          """
        st.markdown(sentiment_analysis_description)

                               #SENTIMENT DATA
        sentiment_data = ("""       
### Sentiment data_
        """)
        st.markdown(sentiment_data)
        #calculate_sentiment(preprocessed_df)                                       #Run script Vs
        sentiment_data = load_csv(f"./data/sentiment/sentiment_analysis.csv")       #Load results
        sentiment_data.drop(sentiment_data.columns[0], axis=1, inplace=True)
        period_sentiment = aggregate_sentiment(sentiment_data, frequency)
        st.dataframe(period_sentiment)


                                    #STATISTICS
        statistics_title = ("""
### Statistics_       
        """)
        st.markdown(statistics_title)
        columns_stats = [
            'text_sentiment_mean',
            'user_sentiment_mean',
            'user_since_mean',
            'tweet_sum',
            'followers_sum',
            'friends_sum',
            'favorites_sum'
        ]
        statistics = calculate_statistics(period_sentiment[columns_stats])
        statistics['user_since_mean'] = statistics['user_since_mean'].apply(seconds_to_duration)
        st.dataframe(statistics)


                                        #WORDCLOUD
        wordcloud_title = ("""                                                  
### Wordcloud_       
        """)
        st.markdown(wordcloud_title)

        colA, colB = st.columns(2)
        with colA:
            theme = "metawords"
            st.text("#Metawords_ ['user_description', 'text']")
            wordcloud = shape_wordcloud(period_sentiment, theme)
            st.image(wordcloud)

            theme = "metalocation"
            st.text("#Metalocation_ ['user_location']")
            wordcloud = shape_wordcloud(period_sentiment, theme)
            st.image(wordcloud)

        with colB:
            theme = "metahashtags"
            st.text("#Metahashtags_ ['hashtags']")
            wordcloud = shape_wordcloud(period_sentiment, theme)
            st.image(wordcloud)

            theme = "metasource"
            st.text("#Metasource_ ['source']")
            wordcloud = shape_wordcloud(period_sentiment, theme)
            st.image(wordcloud)



    with col2:                                      #Numerical Dispersion
        numerical_dispersion_title = ("""
### Numerical dispersion_
        """)
        st.markdown(numerical_dispersion_title)

        columns_dict = ['user_sentiment_mean', 'text_sentiment_mean', 'tweet_sum', 'followers_sum', 'friends_sum','favorites_sum', 'verified_sum']
        figures = []

        for cols in columns_dict:
            selected_columns = period_sentiment[cols]
            fig = gaussian_curve(selected_columns)
            figures.append(fig)

        st.markdown("")
        st.pyplot(figures[0])
        st.markdown("")
        st.markdown("")
        st.pyplot(figures[1])
        st.markdown("")
        st.markdown("")
        st.pyplot(figures[2])
        st.markdown("")
        st.markdown("")
        st.pyplot(figures[3])
        st.markdown("")
        st.markdown("")
        st.pyplot(figures[4])
        st.markdown("")
        st.markdown("")
        st.pyplot(figures[5])
        st.markdown("")
        st.markdown("")
        st.pyplot(figures[6])

















