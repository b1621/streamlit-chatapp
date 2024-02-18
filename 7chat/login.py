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
        if not username or not password:
            st.error("Please enter both username and password.")
        else:
            # Query MongoDB for user
            user = collection.find_one({"username": username})

            if user:
                if user["password"] == password:
                    st.success("Logged in as {}".format(username))
                    st.session_state.page = 'Chat'
                    # Rerun the app to reflect the changes
                    st.experimental_rerun()
                else:
                    st.error("Incorrect password")
            else:
                st.error("User not found")
        
    st.markdown("---")
    st.markdown("Don't have an account?")
    if st.button("Create Account"):
        st.session_state.page = 'Register'
        # Rerun the app to reflect the changes
        st.experimental_rerun()
