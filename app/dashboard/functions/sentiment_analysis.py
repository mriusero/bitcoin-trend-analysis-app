import pandas as pd
import streamlit as st

from .preprocessing import preprocessing
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from .utils import word_chaining_and_count

def get_sentiment(tweet):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(tweet)
    return scores['compound']

def aggregate_sentiment(preprocessed_df, frequency):
    frequency_mapping = {
        '60min': 'h',
        '6H': '6h',
        '12H': '12h',
        'Weekly': 'W',
        'Daily': 'D'
    }
    if frequency in frequency_mapping:

        # GET SENTIMENT
        message_text = st.text("Analyse de sentiment ... 0.00%")

        sentiment_df = preprocessed_df.copy()
        sentiment_df['user_location'] = sentiment_df['user_location'].apply(lambda x: '[' + x.lower().replace(' ', '_') + ']')

        nb_tweet = len(sentiment_df['text'])
        chunk_size = 1000
        nb_chunks = nb_tweet // chunk_size + 1

        global_df = pd.DataFrame()

        for i in range(nb_chunks):
            start_idx = i * chunk_size
            end_idx = min((i + 1) * chunk_size, nb_tweet)

            chunk_df = sentiment_df.iloc[start_idx:end_idx]
            chunk_df.loc[:, 'sentiment_text'] = chunk_df['text'].apply(get_sentiment)
            chunk_df.loc[:,'sentiment_user'] = chunk_df['user_description'].apply(get_sentiment)

            if not chunk_df.empty:
                global_df = pd.concat([global_df, chunk_df], ignore_index=False)

            progress = end_idx
            percentage = round((progress / nb_tweet) * 100, 2)
            message_text.text(f"Analyse de sentiment ({progress}/{nb_tweet} tweets) {percentage}%")

        global_df = global_df.groupby(pd.Grouper(key='date', freq=frequency_mapping[frequency])).agg(
                 {
                'sentiment_text': 'mean',
                'sentiment_user': 'mean',
                'text':['sum','count'],
                'user_description':'sum',
                'user_followers':'sum',
                'user_verified':'sum',
                'user_location':'sum'
                 }
        ).reset_index()
        global_df.dropna(inplace=True)
        global_df.columns = ['date', 'text_sentiment_mean', 'user_sentiment_mean', 'text', 'nb_tweet', 'user_description', 'followers_sum', 'verified_sum', 'metalocation']
        global_df['metawords']= global_df['text'] + global_df['user_description']
        global_df.drop(columns=['text', 'user_description'], inplace=True)
        global_df['metawords'] = global_df['metawords'].apply(word_chaining_and_count)
        global_df['metalocation'] = global_df['metalocation'].apply(word_chaining_and_count)
    return global_df
    #Ajouter la somme des followers (nombre de fois ou le sentiment à été propagé)

#def text_analysis(tweet_df, frequency):
#    preprocessed_df = preprocessing(tweet_df)
#    daily_sentiment = aggregate_sentiment(preprocessed_df, frequency)
#
#    return  preprocessed_df, daily_sentiment


