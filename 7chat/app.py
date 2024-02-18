import streamlit as st
from pymongo import MongoClient
from login import login
from register import register

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['chat']
collection = db['user']

# Streamlit Navigation
page = st.sidebar.radio("Navigation", ['Login', 'Register'])

if page == 'Login':
    login()

elif page == 'Register':
    register()
