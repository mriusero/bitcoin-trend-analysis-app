import streamlit as st

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import learning_curve
import numpy as np
import scipy.stats as stats

def visualise_performance(y_test, predictions, df):

    # Diagramme de dispersion des valeurs prédites par rapport aux valeurs réelles
    fig1, ax1 = plt.subplots()
    ax1.scatter(y_test, predictions)
    ax1.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], '--', color='red')
    ax1.set_xlabel('Valeurs réelles')
    ax1.set_ylabel('Valeurs prédites')
    ax1.set_title('Diagramme de dispersion des valeurs prédites par rapport aux valeurs réelles')

    # Diagramme de dispersion des résidus par rapport aux valeurs prédites
    residuals = y_test - predictions
    fig2, ax2 = plt.subplots()
    ax2.scatter(predictions, residuals)
    ax2.axhline(y=0, color='r', linestyle='-')
    ax2.set_xlabel('Valeurs prédites')
    ax2.set_ylabel('Résidus')
    ax2.set_title('Diagramme de dispersion des résidus par rapport aux valeurs prédites')

    # Histogramme des résidus
    fig3, ax3 = plt.subplots()
    ax3.hist(residuals, bins=30)
    ax3.set_xlabel('Résidus')
    ax3.set_ylabel('Fréquence')
    ax3.set_title('Histogramme des résidus')

    # Courbe de densité des résidus
    fig4, ax4 = plt.subplots()
    sns.kdeplot(residuals, shade=True, ax=ax4)
    ax4.set_xlabel('Résidus')
    ax4.set_ylabel('Densité')
    ax4.set_title('Courbe de densité des résidus')

    # Diagramme QQ
    fig5 = plt.figure()
    stats.probplot(residuals, dist="norm", plot=plt)
    plt.title('Diagramme QQ des résidus')

    # Disposer les graphiques en colonnes
    col1, col2, col3 = st.columns(3)

    with col1:
        st.pyplot(fig1)
        st.pyplot(fig2)
    with col2:
        st.pyplot(fig3)
    with col3:
        st.pyplot(fig4)
        st.pyplot(fig5)

    # Afficher les métriques
    st.write("RMSE:", mean_squared_error(y_test, predictions, squared=False))
    st.write("R2 Score:", r2_score(y_test, predictions))

