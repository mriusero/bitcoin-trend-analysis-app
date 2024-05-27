import streamlit as st
from ..components import create_candlestick_chart2
from ..functions import text_analysis, predict, resample
import pandas as pd
def page_5(market_data, tweet_data):
    st.markdown('<div class="title">SDA_2024</div>', unsafe_allow_html=True)
    st.markdown('<div class="header">#5 Price prediction</div>', unsafe_allow_html=True)

    #st.markdown('<div class="subheader">Description_</div>', unsafe_allow_html=True)
    #st.markdown('<div class="text">  </div>', unsafe_allow_html=True)
#
    #st.markdown('<div class="subheader">Process_</div>', unsafe_allow_html=True)
    #st.markdown('<div class="text">  </div>', unsafe_allow_html=True)

    st.markdown('<div class="subheader">Model_</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">  </div>', unsafe_allow_html=True)

    num_columns = 5
    frequency_map = {
        "60min": "60min",
        "6H": "6H",
        "12H": "12H",
        "Daily": "Daily",
        "Weekly": "Weekly"
    }
    frequencies = list(frequency_map.keys())

    # Diviser les fréquences en groupes pour les afficher sur plusieurs colonnes
    frequency_groups = [frequencies[i:i + num_columns] for i in range(0, len(frequencies), num_columns)]

    # Afficher les radios et le slider sur plusieurs colonnes
    for i, group in enumerate(frequency_groups):
        cols = st.columns(len(group))
        for j, (col, frequency) in enumerate(zip(cols, group)):
            # Vérifier si c'est la dernière colonne
            if i == len(frequency_groups) - 1 and j == len(group) - 5:
                selected_frequency = col.selectbox("Select Frequency:", group,
                                               key=frequency)  # Utiliser frequency comme clé unique
            elif i == len(frequency_groups) - 1 and j == len(group) - 4:
                selected_option1 = col.multiselect('Select Option 1:', ['Option 1', 'Option 2',
                                                                        'Option 3'])  # Ajouter le multiselect dans la troisième colonne
            elif i == len(frequency_groups) - 1 and j == len(group) - 3:
                selected_option2 = col.multiselect('Select Option 2:', ['Option 1', 'Option 2',
                                                                        'Option 3'])
            elif i == len(frequency_groups) - 1 and j == len(group) - 2:
                selected_test_size = col.slider('Test size (%)', 1, 100, 20)  # Afficher le slider dans l'avant-dernière colonne
                test_size = selected_test_size / 100


    # Récupérer la fréquence sélectionnée
    if 'selected_frequency' not in locals():
        selected_frequency = st.radio("", frequencies)

    if selected_frequency:
        frequency = frequency_map[selected_frequency]
    else:
        frequency = 'No frequency selected'
        st.text(f"Please select a frequency")

    predict(market_data, frequency, test_size)

