import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

from .utils import load_csv, resample

def prepare_data(market_data, frequency):
    df_A = resample(market_data, frequency)
    df_A.reset_index(drop=False, inplace=True)
    df_A.rename(columns={'Timestamp': 'date'}, inplace=True)
    df_B = load_csv(f"./data/sentiment/sentiment_analysis_({frequency}).csv")
    del df_B["Unnamed: 0"]
    return pd.merge(df_A, df_B, on='date')

def predict(market_data, frequency):
    df = prepare_data(market_data, frequency)
    return df

