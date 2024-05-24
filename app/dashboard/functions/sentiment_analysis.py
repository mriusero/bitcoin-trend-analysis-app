import re
import pandas as pd
from .resources import stop_words_list
from nltk.stem import SnowballStemmer
from collections import Counter
def preprocessing(text):
    if pd.isnull(text):
        return text
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # Emoticons
                               u"\U0001F300-\U0001F5FF"  # Symboles & pictogrammes
                               u"\U0001F680-\U0001F6FF"  # Transport & symboles de cartes
                               u"\U0001F700-\U0001F77F"  # Symboles alchimiques
                               u"\U0001F780-\U0001F7FF"  # Symboles géométriques
                               u"\U0001F800-\U0001F8FF"  # Suppléments de symboles graphiques
                               u"\U0001F900-\U0001F9FF"  # Suppléments de symboles et de pictogrammes
                               u"\U0001FA00-\U0001FA6F"  # Suppléments de symboles pictographiques supplémentaires
                               u"\U0001FA70-\U0001FAFF"  # Suppléments de symboles pictographiques supplémentaires
                               u"\U00002702-\U000027B0"  # Divers symboles
                               u"\U000024C2-\U0001F251"  # Symboles alphanumériques
                               "]+", flags=re.UNICODE)
    punctuation_pattern = re.compile(r'[^\w\s]', re.UNICODE)
    https_pattern = re.compile(r'httpstco\w{8,10}', re.UNICODE)
    digit_pattern = re.compile(r'(\d)', re.UNICODE)

    text = text.lower()
    text = emoji_pattern.sub(r'', text)
    text = punctuation_pattern.sub(r'', text)
    text = https_pattern.sub(r'', text)
    text = digit_pattern.sub(r'', text)

    return text

def stop_words(text):
    if pd.isnull(text):
        return text

    ENstopWords = stop_words_list()
    ENfiltered_text = ' '.join([word for word in text.split() if word not in ENstopWords])

    FRstopWords = stop_words_list()
    filtered_text = ' '.join([word for word in ENfiltered_text.split() if word not in FRstopWords])

    return filtered_text
def stemmatise_text(text):
    stemmer = SnowballStemmer("english")
    try:
        stemmed_text = " ".join([stemmer.stem(word) for word in text.split()])
        return stemmed_text
    except Exception as e:
        print("Error during stemming:", e)
        return stemmed_text

def word_chaining_and_count(df, text_columns):
    combined_text = ''
    for col in text_columns:
        if col in df.columns:
            combined_text += ' '.join(df[col]) + ' '

    word_list = combined_text.split()

    word_counts = Counter(word_list)
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: (x[1], x[0]))

    return sorted_word_counts


def text_mining(tweet_data):

    text_columns = ('user_name', 'text')  # 'user_name',  'user_location', 'user_description', 'hashtags', 'source'
    df = tweet_data.loc[:, text_columns].copy()
    for col in text_columns:
        if col in df.columns:
            df[col] = df[col].apply(preprocessing)
            df[col] = df[col].apply(stop_words)
            df[col] = df[col].apply(stemmatise_text)

    sorted_word_counts = word_chaining_and_count(df, text_columns)
    print("################# COUNT ######################")
    print(sorted_word_counts)

    return df