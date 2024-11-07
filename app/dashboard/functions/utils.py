from collections import Counter
from datetime import timedelta
import pandas as pd

def load_csv(file_path):
    """
    Load a CSV file into a pandas DataFrame. It automatically handles 'Timestamp' or 'date' columns and converts them to datetime.
    :param file_path: Path to the CSV file to be loaded.
    :return: A pandas DataFrame with datetime conversion applied to 'Timestamp' or 'date' column.
    """
    df = pd.read_csv(file_path)
    if "Timestamp" in df.columns:
        df["Timestamp"] = pd.to_datetime(df["Timestamp"], utc=True)
    elif "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], utc=True)
    return df

def resample(df, frequency):
    """
    Resample the DataFrame to a specified frequency ('60min', '6H', '12H', 'Weekly', 'Daily').
    :param df: The input pandas DataFrame containing the data to be resampled.
    :param frequency: The frequency to resample the data. Options include '60min', '6H', '12H', 'Weekly', 'Daily'.
    :return: A pandas DataFrame resampled at the specified frequency with relevant aggregated statistics.
    """
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
    """
    Counts the frequency of words in a given text and returns a sorted string of word counts.
    :param text_count: A string of text in which word counts need to be calculated.
    :return: A string with words and their counts, formatted as '[word, count]'.
    """
    text_count = text_count.replace('[','')
    text_count = text_count.replace(']',' ')
    word_counts = Counter(text_count.split())
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: (x[1], x[0]), reverse=True)
    sorted_word_counts_str = ' '.join([f'[{word}, {count}]' for word, count in sorted_word_counts])
    return sorted_word_counts_str

def calculate_statistics(df):
    """
    Calculates basic statistics (min, median, mean, std, max) for the numerical columns in the DataFrame.
    :param df: The input DataFrame with numerical data.
    :return: A pandas DataFrame containing calculated statistics (min, median, mean, std, max).
    """
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
    """
    Converts a duration string (e.g., '1 days 03:15:45') into the total number of seconds.
    :param duration_str: The duration as a string, e.g., '1 days 03:15:45'.
    :return: The duration in total seconds (float). If the string is not in the expected format, returns None.
    """
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
    """
    Converts a duration in seconds to a readable string format ('X days HH:MM:SS').
    :param seconds: The duration in seconds (float).
    :return: A string representing the duration in the format 'X days HH:MM:SS'.
    """
    duration = timedelta(seconds=seconds)
    days = duration.days
    hours, remainder = divmod(duration.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{days} days {hours:02}:{minutes:02}:{seconds:02}"
