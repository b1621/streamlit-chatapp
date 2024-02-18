import streamlit as st
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['chat']
collection = db['user']

def login():
    st.title("Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    if st.button("Login"):
        # Query MongoDB for user
        user = collection.find_one({"username": username})

        if user:
            if user["password"] == password:
                st.success("Logged in as {}".format(username))
            else:
                st.error("Incorrect password")
        else:
            st.error("User not found")
