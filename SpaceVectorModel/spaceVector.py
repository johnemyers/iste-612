import os

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk

#nltk.download('stopwords')
#nltk.download('punkt')
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity

print( os.getcwd() )

#path = 'C:/Users/UvirA/Documents/GitHub/iste-612'
#os.chdir(path)
#for f in os.listdir('./data-exploration-python'):
#    print(f)

df = pd.read_excel('./data-exploration-python/dataSummary.xlsx')
#df = pd.read_excel(r'C:\Users\UvirA\Documents\GitHub\iste-612\data-exploration-python\dataSummary.xlsx')    #reading the summary df that contains the text of each document
texts = df['text'].tolist()
stop_words = set(stopwords.words('english')) #English stopwords from nltk package
cleaned_text = []

#function to tokenize the document, returns list of words
def tokenize_text(doc_text):
    tokens = nltk.word_tokenize(doc_text)
    return tokens

#function to stem the words to its root word, returns a list of stemmed words
def word_Stemmer(token_list):
    ps = nltk.stem.PorterStemmer()
    stemmed = []
    for word in token_list:
        stemmed.append(ps.stem(word))
    return stemmed

#Function to remove the stop words, uses English stop words from nltk package
def remove_stopwords(doc_text):
    cleaned_text = []
    for words in doc_text:
        if words not in stop_words:
            cleaned_text.append(words)
    return cleaned_text

#Preprocess the input texts for the documents
for doc in texts:
    tokens = tokenize_text(doc)
    doc_text = remove_stopwords(tokens)
    final_text = word_Stemmer(doc_text)
    final_text = ' '.join(final_text)
    cleaned_text.append(final_text)

#Vetorizer to calculate the tfidf vector fort the documents
vectorizer = TfidfVectorizer()
vectorizer.fit(cleaned_text)
doc_vector = vectorizer.transform(cleaned_text) #tfidf vector for the documents
#print(doc_vector.shape)

query = 'space and unidentified' #input query, to be modified to get the input from UI
query = tokenize_text(query) #tokenize query
query = remove_stopwords(query) #remove stopwords
q = []

#stem the words in the query
for w in word_Stemmer(query):
    q.append(w)
q = ' '.join(q)
query_vector = vectorizer.transform([q]) #vector for the query

# Calculate Cosine similarities
cosineSimilarities = cosine_similarity(doc_vector, query_vector).flatten()

#Retrieving top 10 documents, parameters to be modified to accept no.of. documents from the UI.
related_docs_indices = cosineSimilarities.argsort()[:-10:-1]
#print(related_docs_indices)

#Printing the docID for ranked document,
# This will be returned to the UI from which the user can be access the document(stretch goal)
for i in related_docs_indices:
    docId = df['fileName'][related_docs_indices]
print(docId)
# X = vectorizer.fit_transform(texts)
# print(X.shape)
