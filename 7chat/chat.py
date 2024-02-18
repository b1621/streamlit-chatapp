import streamlit as st
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['chat']
collection = db['user']

def chat():
    st.title("chat app")

    st.header("Welcom to Chat App")

    st.write(st.session_state)