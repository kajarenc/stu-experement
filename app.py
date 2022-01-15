import streamlit as st

st.title("Hello World")

x = st.slider("x", 0, 100)

st.write(x ** 2)
