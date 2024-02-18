import streamlit as st
import time 

st.balloons()
st.progress(10)

with st.spinner('Wait for it...'):
        time.sleep(10)

