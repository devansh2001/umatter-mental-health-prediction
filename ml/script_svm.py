from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import datetime
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

t0 = datetime.datetime.utcnow()
print('Reading data...')
data = pd.read_csv('./RawData/training_data_final.csv', usecols=[1, 2], header=0)
print('Completed reading in ' + str(datetime.datetime.utcnow() - t0))

t0 = datetime.datetime.utcnow()
print('Splitting data...')
X_train, X_test, Y_train, Y_test = train_test_split(data['tweet'], data['sentiment'], test_size=0.01, random_state=1)
print('Completed splitting in ' + str(datetime.datetime.utcnow() - t0))

t0 = datetime.datetime.utcnow()
vectorizer = CountVectorizer()
print('Tokenizing training data ...')
X_train_vectorized = vectorizer.fit_transform(X_train)
print('Tokenized training data in ' + str(datetime.datetime.utcnow() - t0))

t0 = datetime.datetime.utcnow()
print('Tokenizing testing data ...')
X_test_vectorized = vectorizer.transform(X_test)
print('Tokenized testing data in ' + str(datetime.datetime.utcnow() - t0))

t0 = datetime.datetime.utcnow()
naive_bayes = MultinomialNB()
print('Training NB data ...')
naive_bayes.fit(X_train_vectorized, Y_train)
print('Tokenized testing data in ' + str(datetime.datetime.utcnow() - t0))

prediction = naive_bayes.predict(X_test_vectorized)

# print(X_test)
# my_texts = ['I hate apples', 'Wow! Great movie']
# my_texts_vectorized = vectorizer.transform(my_texts)
# prediction = naive_bayes.predict(my_texts_vectorized)

print(prediction)
# print('Accuracy score: ', accuracy_score(Y_test, prediction))
