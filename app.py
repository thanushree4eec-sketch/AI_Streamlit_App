
import streamlit as st

st.title("AI Enabled Web Application")

st.write("Welcome to my cloud application!")

name = st.text_input("Enter your name")

if st.button("Submit"):
    if name:
        st.success(f"Hello, {name}!")
    else:
        st.warning("Please enter your name.")
