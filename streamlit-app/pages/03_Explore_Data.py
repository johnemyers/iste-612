import streamlit as st

st.sidebar.image( "./images/explore.png", use_column_width=True)

style = open( "./pages/html/style.html")
st.markdown( style.read(), unsafe_allow_html=True )

chevron = open( "./pages/html/explore.html")
st.markdown(chevron.read(), unsafe_allow_html=True)
