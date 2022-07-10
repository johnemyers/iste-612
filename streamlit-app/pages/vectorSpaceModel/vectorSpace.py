import nltk
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity


#path = 'C:/Users/UvirA/Documents/GitHub/iste-612'
#os.chdir(path)

class vectorSpace:
    df = pd.read_excel('C:/Users/UvirA/Documents/GitHub/iste-612/data-exploration-python/dataSummary.xlsx')
    # df = pd.read_excel(r'C:\Users\UvirA\Documents\GitHub\iste-612\data-exploration-python\dataSummary.xlsx')    #reading the summary df that contains the text of each document
    stop_words = set(stopwords.words('english'))
      # English stopwords from nltk package


    def __init__(self):
        self.doc_vector = None
        self.texts = self.df['text'].tolist()
        self.cleaned_text = []

    def preprocessDoc(self):
        for doc in self.texts:
            tokens = self.tokenize_text(doc)
            doc_text = self.remove_stopwords(tokens)
            final_text = self.word_Stemmer(doc_text)
            final_text = ' '.join(final_text)
            self.cleaned_text.append(final_text)


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

    def queryVectorizer(self, query, rank=10):
        self.preprocessDoc()
        vectorizer = TfidfVectorizer()
        vectorizer.fit(self.cleaned_text)
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

        related_docs_indices = cosineSimilarities.argsort()[:-(rank+1):-1]
        #print(related_docs_indices)

        # Printing the docID for ranked document,
        # This will be returned to the UI from which the user can be access the document(stretch goal)
        for i in related_docs_indices:
            docId = self.df[['fileName','text']].iloc[related_docs_indices]
        filteredDoc = pd.DataFrame(docId)
        filteredDoc.columns = ['File Name', 'Content']
        return (filteredDoc)

if __name__ == '__main__':
    v = vectorSpace()
    print(v.queryVectorizer("russian space"))