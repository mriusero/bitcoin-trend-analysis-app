import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import numpy as np

from sklearn.model_selection import train_test_split, learning_curve
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

from .utils import load_csv, resample
from .visualise import visualise_performance

def prepare_data(market_data, frequency):
    df_A = resample(market_data, frequency)
    df_A.reset_index(drop=False, inplace=True)
    df_A['av_price'] = round(df_A[['Open', 'High', 'Low', 'Close']].mean(axis=1),2)
    df_A.rename(columns={'Timestamp': 'date'}, inplace=True)
    df_B = load_csv(f"./data/sentiment/sentiment_analysis_({frequency}).csv")
    del df_B["Unnamed: 0"]
    return pd.merge(df_A, df_B, on='date')

def predict(market_data, frequency):
    df = prepare_data(market_data, frequency)

    X = df[['Open', 'text_sentiment_mean', 'user_sentiment_mean', 'nb_tweet', 'followers_sum', 'verified_sum']]
    y = df['Close']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()

    # Définir une taille pour les figures
    fig_size = (10, 6)

    # Sélection des colonnes spécifiques
    colonnes_a_utiliser = ['Open', 'text_sentiment_mean', 'user_sentiment_mean', 'nb_tweet', 'followers_sum', 'verified_sum']
    df_filtree = df[colonnes_a_utiliser]

    # Matrice de corrélation
    fig_corr, ax_corr = plt.subplots(figsize=fig_size)
    sns.heatmap(df_filtree.corr(), annot=True, cmap='coolwarm', ax=ax_corr)
    ax_corr.set_title('Matrice de corrélation')


    train_sizes, train_scores, test_scores = learning_curve(model, X, y, cv=5)
    train_scores_mean = np.mean(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    fig_learn, ax_learn = plt.subplots()
    ax_learn.plot(train_sizes, train_scores_mean, label="Training score")
    ax_learn.plot(train_sizes, test_scores_mean, label="Cross-validation score")
    ax_learn.set_xlabel("Training Size")
    ax_learn.set_ylabel("Score")
    ax_learn.set_title("Courbe d'apprentissage")
    ax_learn.legend()


    col1, col2 = st.columns(2)
    with col1:
        st.pyplot(fig_corr)
    with col2:
        st.pyplot(fig_learn)

    model.fit(X_train, y_train) #Entrainement du model
    predictions = model.predict(X_test)

    rmse = mean_squared_error(y_test, predictions, squared=False)
    print("RMSE:", rmse)
    print("Coefficients:", model.coef_)

    df['prediction'] = model.predict(df[['Open', 'text_sentiment_mean', 'user_sentiment_mean', 'nb_tweet', 'followers_sum', 'verified_sum']])

    visualise_performance(y_test, predictions, df)

    return df
