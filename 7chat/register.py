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
        if not new_username or not new_password:
            st.error("Please enter both username and password.")
        else:

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
                # time.sleep(3)
                # route to login page
                # Rerun the app to redirect to login page
                # st.experimental_rerun()
                st.session_state.page = 'Login'
                # Rerun the app to reflect the changes
                st.experimental_rerun()
    st.markdown("---")
    st.markdown(" have an account?")
    if st.button("login to your Account"):
        st.session_state.page = 'Login'
        # Rerun the app to reflect the changes
        st.experimental_rerun()

    # Check if the link is clicked
    # if st.markdown("Already have an account? [Login to your Account](#)"):
    #     # If the link is clicked, switch page to 'Login' and rerun the app
    #     st.session_state.page = 'Login'
    #     # Rerun the app to reflect the changes
    #     st.experimental_rerun()

    # if st.markdown("Already have an account? <a href='#'>Login to your Account</a>", unsafe_allow_html=True):
    #     # If the link is clicked, switch page to 'Login' and rerun the app
    #     st.session_state.page = 'Login'
    #     # Rerun the app to reflect the changes
    #     st.experimental_rerun()


