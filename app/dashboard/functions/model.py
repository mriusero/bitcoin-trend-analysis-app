import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

from .utils import load_csv, resample
from .sentiment_analysis import aggregate_sentiment
from ..components import create_candlestick_chart2
from .performance import visualise_performance


def prepare_data(market_data, frequency):
    """
    Prepares market data for analysis by resampling based on a specified frequency and merging with sentiment data.

    :param market_data: pd.DataFrame
        DataFrame containing the market data.
    :param frequency: str
        Resampling frequency (e.g., 'D' for daily, 'H' for hourly).
    :return: pd.DataFrame
        Merged DataFrame of market data and sentiment data with dates as index.
    """
    # Resample market data based on the provided frequency
    df_A = resample(market_data, frequency)
    df_A.reset_index(drop=False, inplace=True)  # Reset index after resampling
    df_A.rename(columns={'Timestamp': 'date'}, inplace=True)  # Rename timestamp column to 'date' for merging

    # Load and preprocess sentiment data
    df_C = load_csv(f"./data/sentiment/sentiment_analysis.csv")
    df_C.drop(df_C.columns[0], axis=1, inplace=True)  # Drop unnamed first column if present
    df_B = aggregate_sentiment(df_C, frequency)  # Aggregate sentiment data based on frequency

    # Merge market data with sentiment data on 'date' column
    df = pd.merge(df_A, df_B, on='date', how='left')
    df = df.fillna(0)  # Fill any NaN values with 0 for consistency

    return df


def predict(df, test_size, X_selected, Y_selected):
    """
    Trains a linear regression model on selected features to predict target values and displays performance metrics.

    :param df: pd.DataFrame
        DataFrame containing features and target data.
    :param test_size: float
        Proportion of the dataset to be used as test data (e.g., 0.2 for 20%).
    :param X_selected: list
        List of column names to be used as features (predictors).
    :param Y_selected: str
        Column name of the target variable.
    :return: None
        Outputs predictions and performance metrics directly to the Streamlit app interface.
    """
    X = df[X_selected]  # Select features and target data from DataFrame
    y = df[Y_selected].squeeze()  # Squeeze in case target is a single column DataFrame

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)  # Split data into training and testing sets

    model = LinearRegression()  # Initialize and train the linear regression model
    model.fit(X_train, y_train)  # Model training

    predictions = model.predict(X_test)  # Generate predictions on the test set and calculate residuals
    residuals = y_test - predictions

    rmse = mean_squared_error(y_test, predictions, squared=False)  # Compute root mean squared error (RMSE) for model evaluation

    st.markdown("### Predictions") # Display predictions and residuals in Streamlit
    df['prediction'] = model.predict(X)  # Add predictions to the DataFrame for full dataset
    candlestick_chart = create_candlestick_chart2(df)  # Generate candlestick chart with predictions
    st.plotly_chart(candlestick_chart)

    # Display model performance metrics and coefficients in Streamlit
    st.markdown(f"""
### Performance
    * RMSE: {rmse}
    * Coefficients: {model.coef_}
    """)

    visualise_performance(model, X, y, y_test, predictions, residuals)
