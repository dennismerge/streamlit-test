import streamlit as st
import os

st.title("Hej och välkommen!")
st.write("Det här är en enkel app i Streamlit.")

namn = st.text_input("Vad heter du?")
nummer = st.slider("Välj ett tal:", 1, 10)

if namn:
    st.write(f"Hej {namn}!")
    st.write(f"Ditt valda tal är {nummer}.")
