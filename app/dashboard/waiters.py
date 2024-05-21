import streamlit as st
##streamlit 1.34.0

import time

#Progress bar
my_bar = st.progress(0)
for p in range(10):
    time.sleep(1)
    my_bar.progress(p+1)

# #Spinner
with st.spinner('Waiting...'):
    time.sleep(5)

st.success('Finished')