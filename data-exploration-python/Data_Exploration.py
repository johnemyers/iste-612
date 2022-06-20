import sys

import pandas as pd
import openpyxl
from pdfminer.high_level import extract_text
import os
import nltk
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import re
import matplotlib.pyplot as plt3
import numpy as np

nltk.download('wordnet')
nltk.download('omw-1.4')

wiki_lst = []
title = []
pages = []
lineCount = []
counts = []


totalFiles = 0
eliminatedFiles = 0

df = pd.DataFrame()
dfAllData = pd.DataFrame()

from nltk.corpus import wordnet

dict = {'dict'}

for filename in os.listdir('./data/CIA-MY-OCR/'):
    f = os.path.join('./data/CIA-MY-OCR/', filename)
    if os.path.isfile(f):
        docString = ""
        s = extract_text(f)
        split = s.split()
        lines = s.split("\n")
        validLines = []
        for line in lines:
            if (bool(re.match('(?=.*[0-9])', line)) | (bool(re.match('(?=.*[a-zA-Z])',line)))):
                validLines.append(line)
        wordCount = 0
        for w in split:
            if len(w) > 2 & len(wordnet.synsets(w)) > 0:
                docString += w.lower() + " "
                wordCount += 1
                dict.add(w.lower())

        # extracting text from page
        if wordCount > 2:
            print("Added file " + filename + " with " + str(len(docString.split())) + " words.")
            wiki_lst.append(docString)
            title.append(filename)
            counts.append(wordCount)
            lineCount.append(len(validLines))

            totalFiles += 1
        else:
            eliminatedFiles += 1

        print("On File " + str(totalFiles) + " and eliminated " + str(eliminatedFiles))
        sys.stdout.flush()

# print( dict )
print("Dictionary of length " + str(len(dict)))
#Data frame that contains all the required details
dfAllData['text'] = wiki_lst
dfAllData['fileName'] = title
dfAllData['wordCount'] = counts
dfAllData['lineCount'] = lineCount

#dfAllData.to_excel(r'C:\Users\UvirA\Documents\GitHub\iste-612\checkpoint-2\dataSummary.xlsx')

plt.plot(dfAllData['lineCount'])
plt.xlabel("DocumentID")
plt.ylabel("lineCount")
plt.title("Line Count Series PLot")

# show plot
plt.tight_layout()
plt.show()

# Line count vs Documents plot
#plt3.figure(dpi=800)
plt3.hist(counts, bins='auto')
plt3.title("Histogram of Document Line Count")
ax = plt3.gca()
ax.set_xlabel("Number of lines")
ax.set_ylabel("Number of Documents");

# show plot
plt3.tight_layout()
plt3.show()


#plt2.figure(dpi=800)
plt2.rcParams.update({'font.size': 8})
import advertools as adv

df = pd.DataFrame(wiki_lst, columns=['value'])
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
plt2.show()

dfAllData['wordCount'].describe()
#counts[].describe()

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
K = range(2, 20)
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
