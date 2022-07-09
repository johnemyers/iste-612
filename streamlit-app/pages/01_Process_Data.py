import streamlit as st
import nltk
from pdfminer.high_level import extract_text
from nltk.corpus import wordnet

nltk.download('wordnet')

st.sidebar.image( "./images/process.png", use_column_width=True)
st.sidebar.write('<style>body { margin: 0; font-family: Arial, Helvetica, sans-serif;} .header{padding: 10px 16px; background: #555; color: #f1f1f1; position:fixed;top:0;} .sticky { position: fixed; top: 0; width: 100%;} </style><div class="header" id="myHeader">FOIA Document Analysis</div>', unsafe_allow_html=True)


style = open( "./pages/html/style.html")
st.markdown( style.read(), unsafe_allow_html=True )

chevron = open( "./pages/html/process.html")
st.markdown(chevron.read(), unsafe_allow_html=True)

dict = {''}

uploaded_files = st.file_uploader("Choose a file", type=['pdf'], accept_multiple_files=True)

length = len(uploaded_files)

process_progress = st.progress(0)

fileNum = 1
readInFiles = False;
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
    process_progress.progress( fileNum/length )
    fileNum += 1
    readInFiles = True
    
if readInFiles:
  st.success( "Imported " + str(fileNum) + " PDF files.  Dictionary size is " + str(len(dict)))

