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
    df_A = resample(market_data, frequency)
    df_A.reset_index(drop=False, inplace=True)
    df_A.rename(columns={'Timestamp': 'date'}, inplace=True)

    df_C = load_csv(f"./data/sentiment/sentiment_analysis.csv")
    df_C.drop(df_C.columns[0], axis=1, inplace=True)
    df_B = aggregate_sentiment(df_C, frequency)

    df = pd.merge(df_A, df_B, on='date', how='left')
    df = df.fillna(0)

    return df


def predict(df, test_size, X_selected, Y_selected):

    X = df[X_selected]
    y = df[Y_selected].squeeze()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    model = LinearRegression()

    model.fit(X_train, y_train) #Entrainement du model
    predictions = model.predict(X_test)
    residuals = y_test - predictions

    rmse = mean_squared_error(y_test, predictions, squared=False)

                                    #PREDICTIONS
    predictions_data = ("""
### Predictions_
    """)
    st.markdown(predictions_data)
    df['prediction'] = model.predict(X)
    candlestick_chart = create_candlestick_chart2(df)
    st.plotly_chart(candlestick_chart)

                                    #COEFICIENTS_
    coefficients_data = (f"""
### Performance_
* RMSE: {rmse}
* Coefficients: {model.coef_}
                         """)
    st.markdown(coefficients_data)
    visualise_performance(model, X, y, y_test, predictions, residuals)













