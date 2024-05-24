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