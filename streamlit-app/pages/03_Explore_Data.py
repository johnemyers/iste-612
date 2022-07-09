import streamlit as st
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

st.sidebar.image( "./images/explore.png", use_column_width=True)
st.sidebar.write('<style>body { margin: 0; font-family: Arial, Helvetica, sans-serif;} .header{padding: 10px 16px; background: #555; color: #f1f1f1; position:fixed;top:0;} .sticky { position: fixed; top: 0; width: 100%;} </style><div class="header" id="myHeader">FOIA Document Analysis</div>', unsafe_allow_html=True)

style = open( "./pages/html/style.html")
st.markdown( style.read(), unsafe_allow_html=True )

chevron = open( "./pages/html/explore.html")
st.markdown(chevron.read(), unsafe_allow_html=True)

ready = False

try:
    x = st.session_state.pdf_lst
    maxK = len(x)
    if maxK > 1:
      ready = True
    else:
      st.warning( "Please process more than one PDF file and then try again." )
except AttributeError:
    ready = False
    st.warning( "Please start by processing PDF files and then try again." )

if ready:
  from sklearn.feature_extraction.text import TfidfVectorizer
  
  vectorizer = TfidfVectorizer()
  
  X = vectorizer.fit_transform(st.session_state.pdf_lst)
  #
  # #print(vectorizer.get_feature_names())
  # print(X.shape)
  # plt = {}
  import matplotlib.pyplot as elbowplt
  from sklearn.cluster import KMeans
  
  #
  Sum_of_squared_distances = []
  if( maxK > 20 ):
    maxK = 20
  K = range(1, maxK)
  for k in K:
      km = KMeans(n_clusters=k, max_iter=200, n_init=10)
      km = km.fit(X)
      Sum_of_squared_distances.append(km.inertia_)
  
  elbowplt.plot(K, Sum_of_squared_distances, 'bx-')
  elbowplt.xlabel('k')
  elbowplt.ylabel('Sum_of_squared_distances')
  elbowplt.title('Elbow Method For Optimal k')
  st.pyplot( elbowplt )
  
  true_k = st.slider( "Number of Clusters", min_value=0, max_value=maxK, value=0 )
  
  
  
  if true_k > 0:
    model = KMeans(n_clusters=true_k, init='k-means++', max_iter=200, n_init=10)
    model.fit(X)
    labels=model.labels_
    wiki_cl=pd.DataFrame(list(zip(st.session_state.titles,labels)),columns=['title','cluster'])
    print(wiki_cl.sort_values(by=['cluster']))
    
    from wordcloud import WordCloud
    result={'cluster':labels,'wiki':st.session_state.pdf_lst}
    result=pd.DataFrame(result)
    for k in range(0,true_k):
        s=result[result.cluster==k]
        text=s['wiki'].str.cat(sep=' ')
        text=text.lower()
        text=' '.join([word for word in text.split()])
        wordcloud = WordCloud(width=800, height=400, max_words=80, background_color="white").generate(text)
        print('Cluster: {}'.format(k))
        titles=wiki_cl[wiki_cl.cluster==k]['title']
        print('NumDocs: {}'.format(len(titles)))
    #    print(titles.to_string(index=False))
        plt.figure(figsize=(14,6))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        st.pyplot(plt)
