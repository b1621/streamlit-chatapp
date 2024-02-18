import streamlit as st
from pymongo import MongoClient
from bson import json_util

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['streamlit']
collection = db['user']

# Streamlit Login Page
st.title("Login Page")

# Print the name of the connected database
st.write("Connected to MongoDB database:", db.name)

# List all collections in the connected database
collection_names = db.list_collection_names()

# Print collection names
st.write("Collections in the database:")
for collection_name in collection_names:
    st.write(collection_name)
    print('collection names ', collection_name)


username = st.text_input("username")
password = st.text_input("Password", type='password')

# print("input username = ",username)
# print("input password = ",password)

# print("collection ", collection)
# Printing all users in the terminal
all_users = collection.find()
print("print all users ")
for user in all_users:
    print(user)
if st.button("Login"):
    # Query MongoDB for user
    user = collection.find_one({"username": username})
    print("user = ", user)
    if user:
        if user["password"] == password:
            st.success("Logged in as {}".format(username))
        else:
            st.error("Incorrect password")
    else:
        st.error("User not found")

    all_users = collection.find()
    print("print all users ")
    for user in all_users:
        print(user)
