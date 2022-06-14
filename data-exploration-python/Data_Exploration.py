import pandas as pd
from pdfminer.high_level import extract_text
import os
import nltk
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
import numpy as np


nltk.download( 'wordnet')
nltk.download( 'omw-1.4')

wiki_lst=[]
title=[]
pages=[]

counts=[]

totalPages = 0
totalFiles = 0
eliminatedFiles = 0

df=pd.DataFrame()

from nltk.corpus import wordnet

dict = { 'dict' }

for filename in os.listdir( './data/CIA-MY-OCR/' ):
    f = os.path.join('./data/CIA-MY-OCR/', filename )
    if os.path.isfile( f ):
        docString = ""
        s = extract_text( f )
        # creating a pdf file object 
        pgCount = 0
        tokens = []
        split = s.split()
        for w in split:
              if len(w) > 2 & len(wordnet.synsets( w )) > 0:
                  docString+=w.lower() + " "
                  dict.add( w.lower() )
                  pgCount+=1
                  tokens.append( w.lower() )
                  
            
        # extracting text from page 
        if len(docString.split()) > 2:
            wiki_lst.append( docString )
            title.append( filename )
            counts.append( pgCount )
            totalFiles+=1
        else:
            eliminatedFiles + 1

        print( "On File " + str(totalFiles) + " and eliminated " + str(eliminatedFiles))
        sys.stdout.flush()
print( "Parsed " + str(totalPages) + " Total Pages" )
print( "Parsed " + str(totalFiles) + " Total Files" )

print( dict )
print( str(len(dict)))

plt.figure(dpi=800)
plt.hist(counts, bins='auto')
plt.title( "Histogram of Document Word Count")
ax = plt.gca()
ax.set_xlabel( "Number of Words")
ax.set_ylabel("Number of Documents");

# show plot
plt.tight_layout()
plt.show()


plt2.figure(dpi=800)
plt2.rcParams.update({'font.size': 8})
import advertools as adv

df = pd.DataFrame(wiki_lst, columns =[ 'value'])
word_freq = adv.word_frequency(text_list=df['value'])

frequency = word_freq.sort_values(by='abs_freq', ascending=False).head(25)

# rearrange your data
labels = frequency['word']
values = frequency['abs_freq']

indexes = np.arange(len(labels))


plt2.barh(indexes, values)

# add labels

plt2.yticks(indexes , labels, rotation=0)
plt2.title( "Top 25 Frequent Words & Terms")

ax = plt2.gca()
ax.set_xlabel( "Frequency of Word/Term")
ax.set_ylabel("Word/Term");

plt2.tight_layout() #pad=1.08, h_pad=None, w_pad=None, rect=None)
plt2.show()

counts[].describe()


df = pd.DataFrame(counts, columns =[ 'value'])

df['value'].describe()

Q1 = df['value'].quantile(0.25)
Q3 = df['value'].quantile(0.75)
IQR = Q3 - Q1    #IQR is interquartile range. 

filter = (df['value'] >= Q1 - IQR) & (df['value'] <= Q3 + IQR)
df = df.loc[filter]  
plt3.clf()
ax = plt3.gca()
plt3.boxplot( df  )
plt3.show()


from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
 
X = vectorizer.fit_transform(wiki_lst)
# 
# #print(vectorizer.get_feature_names())
# print(X.shape)
# plt = {}
import matplotlib.pyplot as elbowplt
from sklearn.cluster import KMeans
# 
Sum_of_squared_distances = []
K = range(2,20)
for k in K:
  km = KMeans(n_clusters=k, max_iter=200, n_init=10)
  km = km.fit(X)
  Sum_of_squared_distances.append(km.inertia_)
 
elbowplt.plot(K, Sum_of_squared_distances, 'bx-')
elbowplt.xlabel('k')
elbowplt.ylabel('Sum_of_squared_distances')
elbowplt.title('Elbow Method For Optimal k')
elbowplt.show()
# 
# true_k = 12
# model = KMeans(n_clusters=true_k, init='k-means++', max_iter=200, n_init=10)
# model.fit(X)
# labels=model.labels_
# wiki_cl=pd.DataFrame(list(zip(title,labels)),columns=['title','cluster'])
# print(wiki_cl.sort_values(by=['cluster']))
# 
# from wordcloud import WordCloud
# result={'cluster':labels,'wiki':wiki_lst}
# result=pd.DataFrame(result)
# for k in range(0,true_k):
#     s=result[result.cluster==k]
#     text=s['wiki'].str.cat(sep=' ')
#     text=text.lower()
#     text=' '.join([word for word in text.split()])
#     wordcloud = WordCloud(width=800, height=400, max_words=80, background_color="white").generate(text)
#     print('Cluster: {}'.format(k))
#     titles=wiki_cl[wiki_cl.cluster==k]['title']
#     print('NumDocs: {}'.format(len(titles)))
# #    print(titles.to_string(index=False))
#     plt.figure(figsize=(14,6))
#     plt.imshow(wordcloud, interpolation="bilinear")
#     plt.axis("off")
#     plt.show()

