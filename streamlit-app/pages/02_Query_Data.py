import streamlit as st
import os


st.sidebar.image("./images/query.png", use_column_width=True)
st.sidebar.write(
    '<style>body { margin: 0; font-family: Arial, Helvetica, sans-serif;} .header{padding: 10px 16px; background: #555; color: #f1f1f1; position:fixed;top:0;} .sticky { position: fixed; top: 0; width: 100%;} </style><div class="header" id="myHeader">FOIA Document Analysis</div>',
    unsafe_allow_html=True)

style = open("./pages/html/style.html")
st.markdown(style.read(), unsafe_allow_html=True)

chevron = open("./pages/html/query.html")
st.markdown(chevron.read(), unsafe_allow_html=True)

try:
    x = st.session_state.dfAllData
    ready = True
except AttributeError:
    ready = False
    st.warning("Please start by processing PDF files and then try again.")
    


# if processing is completed perform the retrieval else ask the user to perform processing.
if ready:
    from vectorSpaceModel.vectorSpace import vectorSpace  # generate Vector space model
    v = vectorSpace()
    query = st.text_input("Terms of Query", value="")  # Query term to be searched for in the document collections.
    rank = st.number_input("no.of. documents", 1, 600)  # no.of. documents to be retrieved.
    if st.button("Search"): # Check if button clicked
        if (query != '') & (rank > 0): #Check if there is a search term entered and no.of. documents to retrieve is > 0
            st.dataframe(v.queryVectorizer(query, rank)) #fit a vector space model and retrieve the document names and content.
        else:
            st.warning("Please enter atleast one search term/atleast 1 document to retrieve") # warning to user
