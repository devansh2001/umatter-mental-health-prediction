from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import datetime
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


class NaiveBayesClassification:

    naive_bayes = None

    def __init__(self, data_source):
        vectorized_data = self.prepare_data(data_source)
        self.naive_bayes = self.train_naive_bayes(vectorized_data)

    def tokenize_training_data(self, data):
        vectorizer = CountVectorizer()
        tokenized_data = vectorizer.fit_transform(data)
        return tokenized_data

    def tokenize_testing_data(self, data):
        vectorizer = CountVectorizer()
        tokenized_data = vectorizer.transform(data)
        return tokenized_data

    def prepare_data(self, data_source):
        t0 = datetime.datetime.utcnow()
        print('Reading data...')
        data = pd.read_csv(data_source, usecols=[1, 2], header=0)
        print('Completed reading in ' + str(datetime.datetime.utcnow() - t0))
        t0 = datetime.datetime.utcnow()
        print('Splitting data...')
        X_train, X_test, Y_train, Y_test = train_test_split(data['tweet'], data['sentiment'], test_size=0.01, random_state=1)
        print('Completed splitting in ' + str(datetime.datetime.utcnow() - t0))
        t0 = datetime.datetime.utcnow()
        print('Tokenizing training data ...')
        X_train_vectorized = self.tokenize_training_data(X_train)
        print('Tokenized training data in ' + str(datetime.datetime.utcnow() - t0))
        t0 = datetime.datetime.utcnow()
        print('Tokenizing testing data ...')
        vectorized = CountVectorizer()
        X_test_vectorized = vectorized.fit_transform(X_test)
        print('Tokenized testing data in ' + str(datetime.datetime.utcnow() - t0))
        return {'X_train_vectorized': X_train_vectorized, 'X_test_vectorized': X_test_vectorized, 'Y_train': Y_train, 'Y_test': Y_test}

    def train_naive_bayes(self, vectorized_data):
        t0 = datetime.datetime.utcnow()
        naive_bayes = MultinomialNB()
        print('Training NB data ...')
        naive_bayes.fit(vectorized_data['X_train_vectorized'], vectorized_data['Y_train'])
        print('Tokenized testing data in ' + str(datetime.datetime.utcnow() - t0))
        return naive_bayes

    def get_prediction(self, data):
        tokenized_input = self.tokenize_testing_data([data])
        prediction = self.naive_bayes.predict(tokenized_input)
        return prediction


nb = NaiveBayesClassification(data_source='./RawData/training_data_final.csv')
nb.get_prediction('I like apples')

# print(X_test)
# my_texts = ['I hate apples', 'Wow! Great movie']
# my_texts_vectorized = vectorizer.transform(my_texts)
# prediction = naive_bayes.predict(my_texts_vectorized)

# print(prediction)
# print('Accuracy score: ', accuracy_score(Y_test, prediction))
