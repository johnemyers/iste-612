import streamlit as st
import nltk
from pdfminer.high_level import extract_text
from nltk.corpus import wordnet
import matplotlib.pyplot as plt2
import advertools as adv
import pandas as pd
import numpy as np

#nltk.download('wordnet')
print( "Invoked Process Data" )

st.sidebar.image( "./images/process.png", use_column_width=True)
st.sidebar.write('<style>body { margin: 0; font-family: Arial, Helvetica, sans-serif;} .header{padding: 10px 16px; background: #555; color: #f1f1f1; position:fixed;top:0;} .sticky { position: fixed; top: 0; width: 100%;} </style><div class="header" id="myHeader">FOIA Document Analysis</div>', unsafe_allow_html=True)


style = open( "./pages/html/style.html")
st.markdown( style.read(), unsafe_allow_html=True )

chevron = open( "./pages/html/process.html")
st.markdown(chevron.read(), unsafe_allow_html=True)

dict = {''}

st.session_state.pdf_lst = []
st.session_state.titles = []
st.session_state.counts = []

st.session_state.dfAllData = pd.DataFrame()


uploaded_files = st.file_uploader("Choose a file", type=['pdf'], accept_multiple_files=True)
process_progress = st.progress(0)
fileNum = 1
readInFiles = False;
for uploaded_file in uploaded_files:
    length = len(uploaded_files)
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
    # extracting text from page
    if wordCount > 2:
        st.session_state.pdf_lst.append(docString)
        st.session_state.titles.append(uploaded_file.name)
        st.session_state.counts.append(wordCount)
        print( uploaded_file.name + " " + str(wordCount ) )

    process_progress.progress( fileNum/length )
    fileNum += 1
    readInFiles = True
    
if readInFiles:
  st.success( "Imported " + str(fileNum) + " PDF files.  Dictionary size is " + str(len(dict)))
  
  st.session_state.dfAllData['text'] = st.session_state.pdf_lst
  st.session_state.dfAllData['fileName'] = st.session_state.titles
  st.session_state.dfAllData['wordCount'] = st.session_state.counts
#  st.session_state.dfAllData['lineCount'] = lineCount
  
  df = pd.DataFrame(st.session_state.pdf_lst, columns=['value'])
  word_freq = adv.word_frequency(text_list=df['value'])
  
  frequency = word_freq.sort_values(by='abs_freq', ascending=False).head(25)
  
  # rearrange your data
  labels = frequency['word']
  values = frequency['abs_freq']
  
  indexes = np.arange(len(labels))
  
  plt2.barh(indexes, values)
  
  # add labels
  
  plt2.yticks(indexes, labels, rotation=0)
  plt2.title("Top 25 Frequent Words & Terms")
  
  ax = plt2.gca()
  ax.set_xlabel("Frequency of Word/Term")
  ax.set_ylabel("Word/Term")
  
  plt2.tight_layout()  # pad=1.08, h_pad=None, w_pad=None, rect=None)
  
  st.pyplot( plt2 )



