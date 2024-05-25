import re
import regex
import pandas as pd
from .resources import stop_words_list
from nltk.stem import SnowballStemmer
import ast
from collections import Counter


def cleaning(text):
    if pd.isnull(text):
        return text
    else:
        patterns = {
            "emoji": re.compile("["
                                            "\U0001F600-\U0001F64F"  # Emoticônes
                                            "\U0001F300-\U0001F5FF"  # Symboles et pictogrammes divers
                                            "\U0001F680-\U0001F6FF"  # Transport et symboles de cartes
                                            "\U0001F700-\U0001F77F"  # Symboles alchimiques
                                            "\U0001F780-\U0001F7FF"  # Symboles géométriques supplémentaires
                                            "\U0001F800-\U0001F8FF"  # Supplément symboles divers et pictogrammes
                                            "\U0001F900-\U0001F9FF"  # Supplément symboles et pictogrammes 2
                                            "\U0001FA00-\U0001FA6F"  # Supplément symboles et pictogrammes 3
                                            "\U0001FA70-\U0001FAFF"  # Supplément symboles et pictogrammes 4
                                            "\U00002702-\U000027B0"  # Divers symboles et pictogrammes (partiel)
                                            "\U000024C2-\U0001F251"  # Enclos des caractères CJK (partiel)
                                            "\U0001F0CF"             # Playing Card Black Joker
                                            "\u200d"                 # Zero Width Joiner
                                            "\u2100-\u214F"
                                            "\u1D00-\u1DFF"
                                            "\u02B0-\u02FF" #Modify Letters
                                            "]+", re.UNICODE),
            "punctuation": regex.compile(r'[^\p{L}\p{N}\s]', regex.UNICODE),
            "https": re.compile(r'httpstco\w{8,10}', re.UNICODE),
            "digit": re.compile(r'\d', re.UNICODE),
            "url": re.compile(r'http\S+', re.UNICODE),
            "mention": re.compile(r'@\w+', re.UNICODE),
            "russian_alphapets": regex.compile(r'[а-яёА-ЯЁ]+', re.UNICODE),
            "persan_alphapets": regex.compile(r'[آ-ی]+', re.UNICODE),
            "alphabet_grec": regex.compile(r'[α-ωΑ-Ω]+', re.UNICODE),
            "alphabet_hindi": regex.compile(r'[ँ-ःअ-ऋए-ऑओ-नप-रल-ळव-ह]+', re.UNICODE),
            "alphabet_thaï": regex.compile(r'[ก-๙]+', re.UNICODE),
            "alphabet_rúnico": regex.compile(r'[\u16A0-\u16EA]+', re.UNICODE),
            "finish": regex.compile(r'a-z', re.UNICODE)
        }
        text = text.lower()
        for pattern in patterns.values():
            text = pattern.sub('', text)

        return text

        ###Voir encodage du texte utf-8 pour filtrer correctement

def stop_words(text):
    if pd.isnull(text):
        return text
    #English
    ENstopWords = stop_words_list()
    ENfiltered_text = ' '.join([word for word in text.split() if word not in ENstopWords])
    #French
    FRstopWords = stop_words_list()
    filtered_text = ' '.join([word for word in ENfiltered_text.split() if word not in FRstopWords])
    return filtered_text

def stemmatise(text):
    stemmer = SnowballStemmer("english")
    try:
        stemmed_text = " ".join([stemmer.stem(word) for word in text.split()])
        return stemmed_text
    except Exception as e:
        print("Error during stemming:", e)
        return stemmed_text


def convert_hashtags(text):
    try:
        hashtags = ast.literal_eval(text)
        if isinstance(hashtags, list):
            return ' '.join(hashtags)
    except (ValueError, SyntaxError):
        pass
    return text

def preprocessing(tweet_data):
    tweet_data['hashtags'] = tweet_data['hashtags'].apply(convert_hashtags)

    text_columns = ('source', 'user_location', 'user_name', 'user_description', 'text','hashtags')  #,  'user_name',  , ,
    df = tweet_data.loc[:, text_columns].copy()
    for col in text_columns:
        if col in df.columns:
            df[col] = df[col].apply(lambda x: stemmatise(stop_words(cleaning(x))))
    return df






