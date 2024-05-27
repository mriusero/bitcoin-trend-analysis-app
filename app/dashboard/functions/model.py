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
from ..components import create_candlestick_chart2


def prepare_data(market_data, frequency):
    df_A = resample(market_data, frequency)
    df_A.reset_index(drop=False, inplace=True)

    date_limit = pd.Timestamp('2021-03-12 23:59:14+00:00')
    df_A = df_A[df_A['Timestamp'] < date_limit]

    df_A['av_price'] = round(df_A[['Open', 'High', 'Low', 'Close']].mean(axis=1),2)
    df_A.rename(columns={'Timestamp': 'date'}, inplace=True)
    df_B = load_csv(f"./data/sentiment/sentiment_analysis_({frequency}).csv")
    del df_B["Unnamed: 0"]
    df = pd.merge(df_A, df_B, on='date', how='left')
    df = df.fillna(0)
    return df

def predict(market_data, frequency, test_size):
    df = prepare_data(market_data, frequency)

    X = df[['Open', 'text_sentiment_mean', 'user_sentiment_mean', 'nb_tweet', 'followers_sum', 'verified_sum']]
    y = df['Close']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    model = LinearRegression()

    # Sélection des colonnes spécifiques
    colonnes_a_utiliser = ['Open', 'text_sentiment_mean', 'user_sentiment_mean', 'nb_tweet', 'followers_sum', 'verified_sum']
    df_filtree = df[colonnes_a_utiliser]


    model.fit(X_train, y_train) #Entrainement du model
    predictions = model.predict(X_test)

    rmse = mean_squared_error(y_test, predictions, squared=False)

    print("RMSE:", rmse)
    print("Coefficients:", model.coef_)
    st.markdown('<div class="subheader">Prediction_</div>', unsafe_allow_html=True)
    df['prediction'] = model.predict(df[['Open', 'text_sentiment_mean', 'user_sentiment_mean', 'nb_tweet', 'followers_sum', 'verified_sum']])

    display_data = resample(df, frequency)
    candlestick_chart = create_candlestick_chart2(df)

    st.plotly_chart(candlestick_chart)
    #st.dataframe(df)

    #clicked = st.button("See performances") ##############################
    #if clicked:

    blue_on_graph = '#1F77B4'
    red_on_graph = '#B40426'
    bakcgroung = '#262730'

    #Matrice de corrélation
    fig_corr, ax_corr = plt.subplots(figsize=(6,6))
    heatmap = sns.heatmap(df_filtree.corr(), annot=True, cmap='coolwarm', ax=ax_corr, annot_kws={"color": "white"})
    ax_corr.set_title('Correlation Matrix_', color="white", size="20", loc='right')
    fig_corr.patch.set_facecolor('None')
    ax_corr.tick_params(axis='x', colors='white')
    ax_corr.tick_params(axis='y', colors='white')
    plt.setp(ax_corr.get_xticklabels(), color="white")
    plt.setp(ax_corr.get_yticklabels(), color="white")
    cbar = heatmap.collections[0].colorbar
    plt.setp(cbar.ax.yaxis.get_ticklabels(), color='white', fontsize=10)


    # Learning curve
    train_sizes, train_scores, test_scores = learning_curve(model, X, y, cv=5)
    train_scores_mean = np.mean(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    fig_learn, ax_learn = plt.subplots(figsize=(3, 2))
    ax_learn.plot(train_sizes, train_scores_mean, label="Training score", color=red_on_graph)
    ax_learn.plot(train_sizes, test_scores_mean, label="Cross-validation score", color=blue_on_graph)
    ax_learn.set_xlabel("Training Size", color="white", size='5')
    ax_learn.set_ylabel("Score", color='white', size='5')
    ax_learn.set_title("Learning Curve_", color="white", size='10', loc='right')
    plt.setp(ax_learn.get_xticklabels(), color="white", size='5')
    plt.setp(ax_learn.get_yticklabels(), color="white", size='5')
    # Définir la couleur du cadre (spines)
    for spine in ax_learn.spines.values():
        spine.set_edgecolor('none')
    ax_learn.set_facecolor('none')
    ax_learn.legend(fontsize=5)
    fig_learn.patch.set_facecolor('none')
    ax_learn.grid(True, color='white', linestyle='-', linewidth=0.1)
    fig_learn.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)


    # Diagramme de dispersion des valeurs prédites par rapport aux valeurs réelles
    fig1, ax1 = plt.subplots(figsize=(8,8))
    ax1.scatter(y_test, predictions)
    ax1.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], '-', color=red_on_graph)
    ax1.set_title('valeurs prédites / valeurs réelles', color='white', fontsize=26, loc='left')
    ax1.patch.set_facecolor('none')
    ax1.set_xlabel('Valeurs réelles', color='white', fontsize=22)
    ax1.set_ylabel('Valeurs prédites', color='white', fontsize=22)
    ax1.grid(True, color='gray', linestyle='--', linewidth=0.5)

    for spine in ax1.spines.values():
        spine.set_edgecolor('lightgrey')

    plt.setp(ax1.get_xticklabels(), color="white", size='14')
    plt.setp(ax1.get_yticklabels(), color="white", size='14')

    fig1.patch.set_facecolor('none')
    fig1.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)






    # Diagramme de dispersion des résidus par rapport aux valeurs prédites
    residuals = y_test - predictions
    fig2, ax2 = plt.subplots(figsize=(4,2))
    ax2.scatter(predictions, residuals, color=blue_on_graph)
    ax2.axhline(y=0, color='r', linestyle='-')
    ax2.set_xlabel('Valeurs prédites', color='white', fontsize=10)
    ax2.set_ylabel('Résidus',color='white', fontsize=10)
    ax2.set_title('Residuals Scatterplot vs. Predicted Values_', color='white')
    ax2.set_facecolor('#262730')
    fig2.patch.set_facecolor('none')

    for spine in ax2.spines.values():
        spine.set_edgecolor('none')

    plt.setp(ax2.get_xticklabels(), color="white", size='5')
    plt.setp(ax2.get_yticklabels(), color="white", size='5')
    fig2.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)




    # Histogramme des résidus
    fig3, ax3 = plt.subplots(figsize=(7,5))
    ax3.hist(residuals, bins=30)
    ax3.set_xlabel('Résidus')
    ax3.set_ylabel('Fréquence')
    ax3.set_title('Histogramme des résidus')

    # Courbe de densité des résidus
    fig4, ax4 = plt.subplots(figsize=(5,4))
    sns.kdeplot(residuals, shade=True, ax=ax4)
    ax4.set_xlabel('Résidus')
    ax4.set_ylabel('Densité')
    ax4.set_title('Courbe de densité des résidus')

    # Diagramme QQ
    fig5, ax5 = plt.subplots(figsize=(8,8))
    stats.probplot(residuals, dist="norm", plot=ax5)
    plt.title('Diagramme QQ des résidus', color='white', fontsize=26, loc='left')
    fig5.set_facecolor('none')
    ax5.set_facecolor('none')

    ax5.xaxis.label.set_color('white')
    ax5.xaxis.label.set_fontsize(22)
    ax5.yaxis.label.set_color('white')
    ax5.yaxis.label.set_fontsize(22)

    ax5.tick_params(axis='x', colors='white')  # Couleur rouge pour les graduations de l'axe x
    ax5.tick_params(axis='y', colors='white')  # Couleur bleue pour les graduat

    for spine in ax5.spines.values():
        spine.set_edgecolor('lightgrey')

    ax5.grid(True, color='gray', linestyle='--', linewidth=0.5)
    fig1.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)



    ##LAYOUT
    col1, col2 = st.columns([5,4])
    with col1:
        #st.markdown('<div class="subheader">Residuals Scatterplot vs. Predicted Values_</div>', unsafe_allow_html=True)


        colA, colB = st.columns(2)
        with colA:

            st.pyplot(fig1)
            st.pyplot(fig5)
        #with colB:
            #st.pyplot(fig4)
            #st.pyplot(fig3)


    with col2:
        #st.markdown('<div class="subheader">                      Learning Curve_</div>', unsafe_allow_html=True)
        st.pyplot(fig_learn)
        st.pyplot(fig_corr)

        st.pyplot(fig2)










