import streamlit as st
from ..functions import text_mining
def page_3(tweet_df):
    st.markdown('<div class="title">Bitcoin Tweet Sentiment Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="header">Text Mining</div>', unsafe_allow_html=True)
    st.markdown('<div class="subheader">Phase 1</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">La première étape consiste à réaliser les différentes opérations de text mining</div>', unsafe_allow_html=True)
    st.dataframe(tweet_df)

    df = text_mining(tweet_df)

    colonnes = df.columns.tolist()

    # Utilisation d'un widget pour réorganiser les colonnes
    nouvel_ordre = st.multiselect(
        'Réorganisez les colonnes', colonnes, default=colonnes
    )

    # Si un nouvel ordre est sélectionné, réorganiser les colonnes du DataFrame
    if nouvel_ordre:
        df = df[nouvel_ordre]

    # Affichage du DataFrame réorganisé
    st.write("DataFrame réorganisé :")
    st.dataframe(df)