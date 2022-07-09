import streamlit as st

st.sidebar.image( "./images/query.png", use_column_width=True)
st.sidebar.write('<style>body { margin: 0; font-family: Arial, Helvetica, sans-serif;} .header{padding: 10px 16px; background: #555; color: #f1f1f1; position:fixed;top:0;} .sticky { position: fixed; top: 0; width: 100%;} </style><div class="header" id="myHeader">FOUO Document Analysis</div>', unsafe_allow_html=True)

style = open( "./pages/html/style.html")
st.markdown( style.read(), unsafe_allow_html=True )

chevron = open( "./pages/html/query.html")
st.markdown(chevron.read(), unsafe_allow_html=True)

st.text_input( "Terms of Query" )
st.button( "Search" )
