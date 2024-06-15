import pandas as pd
import streamlit as st

from .preprocessing import preprocessing
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from .utils import duration_to_seconds, seconds_to_duration, word_chaining_and_count

def get_sentiment(tweet):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(tweet)
    return scores['compound']

def calculate_sentiment(df):

    sentiment_df = df.copy()
    message_text = st.text("Analyse de sentiment ... 0.00%")
    columns_to_cast = ['source', 'user_location', 'user_description', 'text', 'hashtags']
    sentiment_df[columns_to_cast] = sentiment_df[columns_to_cast].astype(str)
    sentiment_df['user_since']=sentiment_df['user_since'].apply(duration_to_seconds)
    sentiment_df['source'] = sentiment_df['source'].apply(lambda x: '[' + x.lower().replace(' ', '_') + ']')
    sentiment_df['user_location'] = sentiment_df['user_location'].apply(lambda x: '[' + x.lower().replace(' ', '_') + ']')
    nb_tweet = len(sentiment_df['text'])
    chunk_size = 2500
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

    return global_df.to_csv(f"./data/sentiment/sentiment_analysis.csv")
def aggregate_sentiment(df, frequency):
    frequency_mapping = {
        '60min': 'h',
        '6H': '6h',
        '12H': '12h',
        'Weekly': 'W',
        'Daily': 'D'
    }
    global_df = df.groupby(pd.Grouper(key='date', freq=frequency_mapping[frequency])).agg(
             {
            'sentiment_text': 'mean',
            'sentiment_user': 'mean',
            'user_since':'mean',
            'text':['sum','count'],
            'user_description':'sum',
            'user_followers':'sum',
            'user_friends': 'sum',
            'user_favourites':'sum',
            'user_verified':'sum',
            'user_location':'sum',
            'source': 'sum',
            'hashtags': 'sum'
             }
    ).reset_index()
    global_df.dropna(inplace=True)
    global_df.columns = ['date',
                         'text_sentiment_mean',
                         'user_sentiment_mean',
                         'user_since_mean',
                         'text', 'tweet_sum',
                         'user_description',
                         'followers_sum',
                         'friends_sum',
                         'favorites_sum',
                         'verified_sum',
                         'location_sum',
                         'source_sum',
                         'hashtags_sum']
    global_df['user_since_mean'] = global_df['user_since_mean'].apply(seconds_to_duration)
    global_df['words'] = global_df['text'] + global_df['user_description']
    global_df = global_df.assign(
        metalocation=global_df['location_sum'].apply(word_chaining_and_count),
        metasource=global_df['source_sum'].apply(word_chaining_and_count),
        metahashtags=global_df['hashtags_sum'].apply(word_chaining_and_count),
        metawords=global_df['words'].apply(word_chaining_and_count)
    )
    global_df.drop(columns=['location_sum', 'source_sum', 'hashtags_sum', 'text', 'user_description', 'words'], inplace=True)
    return global_df



