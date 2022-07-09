import streamlit as st
import nltk
from pdfminer.high_level import extract_text
from nltk.corpus import wordnet

nltk.download('wordnet')


style = open( "./pages/html/style.html")
st.markdown( style.read(), unsafe_allow_html=True )

chevron = open( "./pages/html/process.html")
st.markdown(chevron.read(), unsafe_allow_html=True)

dict = {'dict'}

uploaded_files = st.file_uploader("Choose a file", type=['pdf'], accept_multiple_files=True)

length = len(uploaded_files)

process_progress = st.progress(0)

fileNum = 1
for uploaded_file in uploaded_files:
    with st.spinner('Parsing Text of File # ' + str(fileNum) + " ...." ):
      docString = ""
      s = extract_text(uploaded_file)
      split = s.split()
    wordCount = 0
    for w in split:
      if len(w) > 2 & len(wordnet.synsets(w)) > 0:
        docString += w.lower() + " "
        wordCount += 1
        dict.add(w.lower())
        print( w.lower() )
    process_progress.progress( fileNum/length )
    fileNum += 1


