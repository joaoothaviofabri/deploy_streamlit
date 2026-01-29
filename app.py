import streamlit as st

st.title("Meu primeiro Deploy")

slider = st.slider("Selecione um ano: ", min_value=1995, max_value=2024)
st.write(f"O ano selecionado foi: {slider}")

st.select_slider("Selecione um ano: ", options=[1995, 1996, 2010, 2011, 2012, 2013, 2023, 2024])