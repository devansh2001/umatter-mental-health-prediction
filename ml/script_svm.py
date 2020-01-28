from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import datetime
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


class NaiveBayesClassification:

    naive_bayes = None
    vectorized_data_1 = None

    def __init__(self, data_source):
        self.vectorized_data_1 = self.prepare_data(data_source)
        self.naive_bayes = self.train_naive_bayes(vectorized_data=self.vectorized_data_1)
        self.get_accuracy()
        # print(self.get_prediction(['I like apples']))

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
        vectorizor = CountVectorizer()
        print('Tokenizing training data ...')
        X_train_vectorized = vectorizor.fit_transform(X_train)
        print('Tokenized training data in ' + str(datetime.datetime.utcnow() - t0))
        t0 = datetime.datetime.utcnow()
        print('Tokenizing testing data ...')
        X_test_vectorized = vectorizor.transform(X_test)
        print('Tokenized testing data in ' + str(datetime.datetime.utcnow() - t0))
        return {'X_train_vectorized': X_train_vectorized, 'X_test_vectorized': X_test_vectorized, 'Y_train': Y_train, 'Y_test': Y_test}

    def train_naive_bayes(self, vectorized_data):
        t0 = datetime.datetime.utcnow()
        naive_bayes = MultinomialNB()
        print('Training NB data ...')
        naive_bayes.fit(vectorized_data['X_train_vectorized'], vectorized_data['Y_train'])
        print('Tokenized testing data in ' + str(datetime.datetime.utcnow() - t0))
        return naive_bayes

    def get_accuracy(self):
        prediction = self.naive_bayes.predict(self.vectorized_data_1['X_test_vectorized'])
        print(self.vectorized_data_1['X_test_vectorized'][0])
        print('Accuracy score: ', accuracy_score(self.vectorized_data_1['Y_test'], prediction))

    def get_prediction(self, data):
        # tokenized_input = self.tokenize_testing_data([data])
        vectorizor = CountVectorizer()
        print(data)
        my_texts = ['I hate apples', 'Wow! Great movie']
        tokenized_input = vectorizor.transform(my_texts)
        print(tokenized_input)
        prediction = self.naive_bayes.predict(tokenized_input)
        print(prediction)
        return prediction


nb = NaiveBayesClassification(data_source='./RawData/training_data_final.csv')
print(nb.get_prediction(['I love this class', 'Wow I am so excited']))

# print(X_test)
# my_texts = ['I hate apples', 'Wow! Great movie']
# my_texts_vectorized = vectorizer.transform(my_texts)
# prediction = naive_bayes.predict(my_texts_vectorized)

# print(prediction)
# print('Accuracy score: ', accuracy_score(Y_test, prediction))
