import pandas as pd
from pdfminer.high_level import extract_text
import os
import nltk


nltk.download( 'wordnet')
nltk.download( 'omw-1.4')

wiki_lst=[]
title=[]

totalPages = 0
totalFiles = 0
eliminatedFiles = 0

from nltk.corpus import wordnet

dict = { 'dict' }

for filename in os.listdir( './data/CIA-MY-OCR/' ):
    f = os.path.join('./data/CIA-MY-OCR/', filename )
    if os.path.isfile( f ):
        docString = ""
        s = extract_text( f )
        # creating a pdf file object 
        
        split = s.split()
        for w in split:
              if len(w) > 2 & len(wordnet.synsets( w )) > 0:
                  docString+=w.lower() + " "
                  dict.add( w.lower() )
                  
            
        # extracting text from page 
        if len(docString.split()) > 5:
            wiki_lst.append( docString )
            title.append( filename )

            totalFiles+=1
        else:
            eliminatedFiles += 1

        print( "On File " + str(totalFiles) + " and eliminated " + str(eliminatedFiles))
        sys.stdout.flush()
print( "Parsed " + str(totalPages) + " Total Pages" )
print( "Parsed " + str(totalFiles) + " Total Files" )

print( dict )
print( str(len(dict)))

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(wiki_lst)

#print(vectorizer.get_feature_names())
print(X.shape)
plt = {}
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

Sum_of_squared_distances = []
K = range(2,20)
for k in K:
    km = KMeans(n_clusters=k, max_iter=200, n_init=10)
    km = km.fit(X)
    Sum_of_squared_distances.append(km.inertia_)

plt.plot(K, Sum_of_squared_distances, 'bx-')
plt.xlabel('k')
plt.ylabel('Sum_of_squared_distances')
plt.title('Elbow Method For Optimal k')
plt.show()

true_k = 6
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=200, n_init=10)
model.fit(X)
labels=model.labels_
wiki_cl=pd.DataFrame(list(zip(title,labels)),columns=['title','cluster'])
print(wiki_cl.sort_values(by=['cluster']))

from wordcloud import WordCloud
result={'cluster':labels,'wiki':wiki_lst}
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
    plt.show()

