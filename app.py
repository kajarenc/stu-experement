import streamlit as st

st.title("Hello World")

st.write(st.user_info)

x = st.slider("x", 0, 100)


st.write(x ** 2)
