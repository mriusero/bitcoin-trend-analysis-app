import streamlit as st
import subprocess
import os
def page_0():
    st.markdown('<div class="title">SDA_2024</div>', unsafe_allow_html=True)
    st.markdown('<div class="header">#0 Data Management_</div>', unsafe_allow_html=True)
    st.text("Here is the Jupyter Notebook of data management phase, starting from 'kaggle.com' original datasets.")
    st.text("______________________________________________________________________________________________________________________________________________")
    notebook_path = './data/exploration/dataset_exploration.md'
    def afficher_markdown(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            markdown_text = f.read()
        st.markdown(markdown_text)

    afficher_markdown(notebook_path)