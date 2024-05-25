from collections import Counter
import regex

import pandas as pd

def load_csv(file_path):
    df = pd.read_csv(file_path)
    if "Timestamp" in df.columns:
        df["Timestamp"] = pd.to_datetime(df["Timestamp"], utc=True)
    elif "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], utc=True)
    return df

def resample_for_candlesticks(df, frequency):
    frequency_mapping = {
        'Hourly': 'h',
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

def word_chaining_and_count(df):
    combined_text = ''
    for col in df.columns:
        combined_text += ' '.join(df[col].astype(str)) + ' '

    word_counts = Counter(combined_text.split())
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: (x[1], x[0]), reverse=True)

    # Création d'une liste de dictionnaires
    word_count_dicts = [{'word': word, 'count': count} for word, count in sorted_word_counts]
    # Convertir la liste de dictionnaires en DataFrame
    result_df = pd.DataFrame(word_count_dicts)

    # Créer une deuxième liste avec les mots dont le count est 1
    words_with_count_one = result_df[result_df['count'] <= 2]['word'].tolist()
    # Filtrer les mots par ordre alphabétique inférieur à 'z'
    #filtered_words = [word for word in words_with_count_one if regex.match(r'^[a-z]+$', word)]
    print("##################################### FILTERED WORDS\n")
    print(words_with_count_one)
    return result_df
