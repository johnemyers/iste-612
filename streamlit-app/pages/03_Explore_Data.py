import streamlit as st

style = open( "./pages/html/style.html")
st.markdown( style.read(), unsafe_allow_html=True )

chevron = open( "./pages/html/explore.html")
st.markdown(chevron.read(), unsafe_allow_html=True)
