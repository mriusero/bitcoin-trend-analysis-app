from collections import Counter
from datetime import timedelta
import pandas as pd

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
        if 'Timestamp' in df.columns:
            timestamp_column = 'Timestamp'
        elif 'date' in df.columns:
            timestamp_column = 'date'
        display_data = df.resample(frequency_mapping[frequency], on=timestamp_column).agg(
            {'Open': 'first',
             'High': 'max',
             'Low': 'min',
             'Close': 'last',
             'Volume_(BTC)': 'sum',
             'Volume_(Currency)':'sum'
             }
        )
        display_data["Weighted_Price"] = display_data["Volume_(Currency)"] / display_data["Volume_(BTC)"]
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

def calculate_statistics(df):

    if 'user_since_mean' in df.columns:
        df['user_since_mean'] = df['user_since_mean'].apply(duration_to_seconds)
        stat_df = df
    else:
        stat_df = df.select_dtypes(exclude=['datetime', 'datetime64[ns]', 'datetime64[ns, UTC]'])

    results = {
        'MIN': stat_df.min(),
        'MEDIAN': stat_df.median(),
        'MEAN': stat_df.mean(),
        'STD': stat_df.std(),
        'MAX': stat_df.max(),
    }
    statistics = pd.DataFrame(results)
    statistics = statistics.T
    return statistics

def duration_to_seconds(duration_str):
    if isinstance(duration_str, (int, float)):
        return float(duration_str)

    if isinstance(duration_str, str):
        try:
            days, time = duration_str.split(" days ")
            hours, minutes, seconds = map(int, time.split(":"))
            duration = timedelta(days=int(days), hours=hours, minutes=minutes, seconds=seconds)
            return duration.total_seconds() / (24 * 3600)
        except ValueError:
            return None
    else:
        return None

def seconds_to_duration(seconds):
    duration = timedelta(seconds=seconds)
    days = duration.days
    hours, remainder = divmod(duration.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{days} days {hours:02}:{minutes:02}:{seconds:02}"