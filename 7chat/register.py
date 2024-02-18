import streamlit as st
from pymongo import MongoClient
import time 

client = MongoClient('mongodb://localhost:27017/')
db = client['chat']
collection = db['user']

def register():
    st.title("Registration Page")

    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type='password')
    conf_password = st.text_input("Confirm Password", type='password')

    if st.button("Register"):
        # Check if username already exists
        existing_user = collection.find_one({"username": new_username})
        if existing_user:
            st.error("Username already exists. Please choose a different one.")
        elif new_password != conf_password:
            st.error("Password doesn't match")
        else:
            # Insert new user into MongoDB
            new_user = {"username": new_username, "password": new_password}
            collection.insert_one(new_user)
            st.success("Account created successfully!")
            time.sleep(3)
            # route to login page
            # Rerun the app to redirect to login page
            st.experimental_rerun()
            




