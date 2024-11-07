import streamlit as st
def page_0():
    st.markdown('<div class="title">Bitcoin Trend Analysis App</div>', unsafe_allow_html=True)
    st.markdown("# #0 Data Management_")
    st.text("Here is the Jupyter Notebook of data management phase, starting from 'kaggle.com' original datasets.")
    st.text("______________________________________________________________________________________________________________________________________________")

    notebook_path = './data/exploration/dataset_exploration.md'
    def display_notebook_as_markdown(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            markdown_text = f.read()
        st.markdown(markdown_text)

    display_notebook_as_markdown(notebook_path)