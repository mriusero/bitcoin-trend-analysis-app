from collections import Counter
import pandas as pd
import re

def load_csv(file_path):
    df = pd.read_csv(file_path)
    if "Timestamp" in df.columns:
        df["Timestamp"] = pd.to_datetime(df["Timestamp"], utc=True)
    elif "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], utc=True)
    return df

def resample(df, frequency):
    frequency_mapping = {
        '60min': 'h',
        '6H': '6h',
        '12H': '12h',
        'Weekly': 'W',
        'Daily': 'D'
    }
    if frequency in frequency_mapping:
        display_data = df.resample(frequency_mapping[frequency], on='Timestamp').agg(
            {'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last'})
    else:
        display_data = df
    return display_data

def word_chaining_and_count(text_count):
    text_count = text_count.replace('[','')
    text_count = text_count.replace(']',' ')
    word_counts = Counter(text_count.split())
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: (x[1], x[0]), reverse=True)
    sorted_word_counts_str = ' '.join([f'[{word}, {count}]' for word, count in sorted_word_counts])
    return sorted_word_counts_str


