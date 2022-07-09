import streamlit as st

st.sidebar.image( "./images/query.png", use_column_width=True)

style = open( "./pages/html/style.html")
st.markdown( style.read(), unsafe_allow_html=True )

chevron = open( "./pages/html/query.html")
st.markdown(chevron.read(), unsafe_allow_html=True)
