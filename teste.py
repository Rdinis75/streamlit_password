import pandas as pd
import streamlit as st
import os


st.title("PAssword Token")

st.subheader("Hope it works!")

password_guess = st.text_input('What is the Password?')

if password_guess != st.secrets["password"]:
    st.stop()

st.sidebar.text("Password is ok")


st.markdown("Please keep going")
