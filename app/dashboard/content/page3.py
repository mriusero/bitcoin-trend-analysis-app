import streamlit as st
from ..components import create_circular_graph
from ..functions import text_analysis
def page_3(tweet_df):

    st.markdown('<div class="title">Bitcoin Tweet Sentiment Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="header">Twitter data</div>', unsafe_allow_html=True)

    st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
    st.dataframe(tweet_df)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="header">Preprocessing</div>', unsafe_allow_html=True)
    st.markdown("""
                - conversion en minuscules
                - suppression des emojis, url, @mention
                - suppression des stopwords (english, french)
                - stemmatisation
                """)

    preprocessed_df, occurence_df = text_analysis(tweet_df)
    st.dataframe(preprocessed_df)

    st.markdown('<div class="header">occurences:</div>', unsafe_allow_html=True)
    st.dataframe(occurence_df)

    #circular_graph = create_circular_graph(occurence_df)
    #st.plotly_chart(circular_graph)