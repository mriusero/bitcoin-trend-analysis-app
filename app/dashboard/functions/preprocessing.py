import re
import regex
import pandas as pd
import nltk
import streamlit as st
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
import ast

# Initialisation globale des stopwords pour éviter de le refaire à chaque appel
nltk.download('stopwords')
EN_stopwords = stopwords.words('english')
FR_stopwords = stopwords.words('french')
STOP_WORDS = set(EN_stopwords + FR_stopwords)

#Initialisation du Stemmer
STEMMER = SnowballStemmer("english")

# Compilation des regex une fois pour toutes
PATTERNS = {
    "emoji": re.compile("["
                        "\U0001F600-\U0001F64F"
                        "\U0001F300-\U0001F5FF"
                        "\U0001F680-\U0001F6FF"
                        "\U0001F700-\U0001F77F"
                        "\U0001F780-\U0001F7FF"
                        "\U0001F800-\U0001F8FF"
                        "\U0001F900-\U0001F9FF"
                        "\U0001FA00-\U0001FA6F"
                        "\U0001FA70-\U0001FAFF"
                        "\U00002702-\U000027B0"
                        "\U000024C2-\U0001F251"
                        "\U0001F0CF"
                        "\u200d"
                        "\u2100-\u214F"
                        "\u1D00-\u1DFF"
                        "\u02B0-\u02FF"
                        "]+", re.UNICODE),
    "punctuation": regex.compile(r'[^\p{L}\p{N}\s]', regex.UNICODE),
    "https": re.compile(r'httpstco\w{8,10}', re.UNICODE),
    "digit": re.compile(r'\d', re.UNICODE),
    "url": re.compile(r'http\S+', re.UNICODE),
    "mention": re.compile(r'@\w+', re.UNICODE),
    "russian_alphabets": regex.compile(r'[а-яёА-ЯЁ]+', regex.UNICODE),
    "persian_alphabets": regex.compile(r'[آ-ی]+', regex.UNICODE),
    "greek_alphabet": regex.compile(r'[α-ωΑ-Ω]+', regex.UNICODE),
    "hindi_alphabet": regex.compile(r'[ँ-ःअ-ऋए-ऑओ-नप-रल-ळव-ह]+', regex.UNICODE),
    "thai_alphabet": regex.compile(r'[ก-๙]+', regex.UNICODE),
    "runic_alphabet": regex.compile(r'[\u16A0-\u16EA]+', regex.UNICODE),
    "symbols": re.compile(
        r"₇|ⁿⁿ|ⁱⁿ|ⁱ|ᙇ|ᕙ|ᕗ|საქართველო|বছনয|আমর|єє|ϟϟ|ʜʜ|ʜɴʀ|ʙɴɪɴ|ʕ|ʔcinta|ʏʀ|ʋ|ʀʟʀ|ʀʏʀ|ʀʀɪʟʏ|ʀʀɪ|ʀʀ|ʀɴɪ|ʀɴ|ɴʟʏ|ɴʀɴɪʜ|ɴʀɴ|ɴʀ|ɴɢʜ|ɪʟʟʀʀ|ɪʟ|ɪʀɪʀ|ɪʀ|ɢʙʀ|ɢɪɴɢ|ɖ|ƨ|ƒ|ƈԋɳƈҽx|ƀitcoin|şuan|şekerciyapı|şamil|şahsi|łđ|łódź|łódzkie|łtc|ıota|ıcx|üzerin|ütücü|ücretsiz|ñ|ðögè|ðö|ðr|ïs|èl|çok|çizgi|ænęłÿšīû|äöhì|árabe|¼|³'",
        re.UNICODE),
    "finish": re.compile(r'a-z', re.UNICODE),
    "location": re.compile(r'uknwuserloc', regex.UNICODE)
}


def cleaning(text):
    if pd.isnull(text):
        return text
    if isinstance(text, str):
        text = text.encode('utf-8').decode('utf-8')
    text = text.lower()
    for pattern in PATTERNS.values():
        text = pattern.sub('', text)
    return text


def stop_words(text):
    if pd.isnull(text):
        return text
    return ' '.join([word for word in text.split() if word not in STOP_WORDS])


def stemmatise(text):
    try:
        return " ".join([STEMMER.stem(word) for word in text.split()])
    except Exception as e:
        print("Error during stemming:", e)
        return text


def convert_hashtags(text):
    try:
        hashtags = ast.literal_eval(text)
        if isinstance(hashtags, list):
            return ' '.join(hashtags)
    except (ValueError, SyntaxError):
        pass
    return text


def preprocessing(tweet_data):
    message_text = st.text("Preprocessing ... 0.00%")

    tweet_data.loc[:, 'hashtags'] = tweet_data['hashtags'].apply(convert_hashtags)
    text_columns = ['date','user_location', 'user_description', 'text']
    df = tweet_data.loc[:, text_columns].copy()
    df.set_index('date', inplace=True)

    nb_tweet = len(df['text'])

    for i, col in enumerate(text_columns, start=1):
        if col in df.columns:
            df[col] = df[col].apply(lambda x: stemmatise(stop_words(cleaning(x))))

        progress_percentage = (i / nb_tweet * 100)
        message_text.text(f"Preprocessing ... {progress_percentage:.2f}%")

    df.reset_index(inplace=True)
    #tweet_data.set_index('date', inplace=True)

    message_text.text("Preprocessing terminé ! 100.00%")

    df_A_columns = ['date', 'source', 'user_followers', 'user_verified']
    df_A = tweet_data.loc[:, df_A_columns].copy()
    #df_A['user_location'] = df_A['user_location'].apply(lambda x: '[' + x.lower().replace(' ','_') + ']')

    df_B_columns = ['date', 'user_location', 'user_description', 'text']
    df_B = df.loc[:, df_B_columns].copy()

    new_df = pd.merge(df_A, df_B, on='date')
    return new_df
