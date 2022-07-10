import os
import streamlit as st
import nltk
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity

#personal space not used
#path = 'C:/Users/UvirA/Documents/GitHub/iste-612'
#os.chdir(path)

class vectorSpace:

    #Class Variables
    df = st.session_state.dfAllData # this should be generated as part of
    # preprocessing step. Could be converted to instance variable depending on need. to be changed to possibly refer to a dataframe
    #created within the Process_Data or Data_Exploration.
    stop_words = set(stopwords.words('english')) # English stopwords from nltk package

    #initializer to create instance variables
    def __init__(self):
        print( "IN INIT()")
        self.doc_vector = None #vector space for all the doc text.
        self.texts = st.session_state.dfAllData['text'].tolist() #list of texts of all the documents in the collection.
        print( self.texts )
        self.cleaned_text = [] #cleansed text after removing stop words and performing stemming.

    # function to tokenize and preprocess the texts in the documents
    def preprocessDoc(self):
        for doc in self.texts:
            tokens = self.tokenize_text(doc)
            doc_text = self.remove_stopwords(tokens)
            final_text = self.word_Stemmer(doc_text)
            final_text = ' '.join(final_text)
            self.cleaned_text.append(final_text)

    # function to tokenize each document text.
    def tokenize_text(self,doc_text):
        tokens = nltk.word_tokenize(doc_text)
        return tokens

    # function to stem the words to its root word, returns a list of stemmed words
    def word_Stemmer(self,token_list):
        ps = nltk.stem.PorterStemmer()
        stemmed = []
        for word in token_list:
            stemmed.append(ps.stem(word))
        return stemmed

    # Function to remove the stop words, uses English stop words from nltk package
    def remove_stopwords(self, doc_text):
        cleaned_text = []
        for words in doc_text:
            if words not in vectorSpace.stop_words:
                cleaned_text.append(words)
        return cleaned_text

    # Function that performs ranked retrieval for the input query and no.of. documents needed for retrieval.
    # if rank is not passed , default of 10 documents will be retrieved.
    def queryVectorizer(self, query, rank=10):
        print( "Querying for " + query )
        self.preprocessDoc()
        vectorizer = TfidfVectorizer()
        vectorizer.fit(self.cleaned_text)   #fitting the vectorizer to cleansed text
        self.doc_vector = vectorizer.transform(self.cleaned_text)
        query = self.tokenize_text(query)  # tokenize query
        query = self.remove_stopwords(query)  # remove stopwords
        q = []
        for w in self.word_Stemmer(query):
            q.append(w)
        q = ' '.join(q)
        query_vector = vectorizer.transform([q])  # vector for the query

        # Calculate Cosine similarities
        cosineSimilarities = cosine_similarity(self.doc_vector, query_vector).flatten()

        related_docs_indices = cosineSimilarities.argsort()[:-(rank+1):-1] # retrieve index from the documents

        # retrieving the document name and content for each indices from the dataframe.
        for i in related_docs_indices:
            docId = st.session_state.dfAllData[['fileName','text']].iloc[related_docs_indices]
        filteredDoc = pd.DataFrame(docId)
        filteredDoc.columns = ['File Name', 'Content']
        return (filteredDoc)    #returning the dataframe of filename and content to display on the UI.

if __name__ == '__main__': # solely for testing purpose, should be used as package than a main class.
    v = vectorSpace()
    print(v.queryVectorizer("russian space"))
